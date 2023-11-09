import os
import json
from glob import glob
import yaml
import requests
import urllib.error
from itertools import chain
from pathlib import Path, PurePath
from typing import Generator, Tuple, Union

import ipykernel
from jupyter_core.paths import jupyter_runtime_dir, get_home_dir
from traitlets.config import MultipleInstanceError

FILE_ERROR = "Can't identify the notebook {}."
CONN_ERROR = "Unable to access server;\n" \
           + "nci_ipynb requires either no security or password based security."


def _list_maybe_running_servers(runtime_dir=None) -> Generator[dict, None, None]:
    """ Iterate over the server info files of running notebook servers.
    """
    if runtime_dir is None:
        runtime_dir = jupyter_runtime_dir()
    runtime_dir = Path(runtime_dir)

    if runtime_dir.is_dir():
        # Get notebook configuration files, sorted to check the more recently modified ones first
        for file_name in sorted(
            chain(
                runtime_dir.glob('nbserver-*.json'),  # jupyter notebook (or lab 2)
                runtime_dir.glob('jpserver-*.json'),  # jupyterlab 3
            ),
            key=os.path.getmtime,
            reverse=True,
        ):
            try:
                yield json.loads(file_name.read_bytes())
            except json.JSONDecodeError as err:
                # Sometimes we encounter empty JSON files. Ignore them.
                pass


def _get_kernel_id() -> str:
    """ Returns the kernel ID of the ipykernel.
    """
    connection_file = Path(ipykernel.get_connection_file()).stem
    kernel_id = connection_file.split('-', 1)[1]
    return kernel_id


def _get_sessions(srv, password):
    """ Given a server, returns sessions, or HTTPError if access is denied.
        NOTE: Works only when either there is no security or there is token
        based security. An HTTPError is raised if unable to connect to a
        server.
    """
    try:
        base_url = srv['url']
        h = {}
        if password:
            r = requests.post(base_url + 'login', params={
                'password': password
            })
            h = r.request.headers
        return requests.get(base_url + 'api/sessions', headers=h).json()
    except Exception:
        raise urllib.error.HTTPError(CONN_ERROR)


def _find_nb_path() -> Union[Tuple[dict, PurePath], Tuple[None, None]]:
    try:
        kernel_id = _get_kernel_id()
    except (MultipleInstanceError, RuntimeError):
        return None, None  # Could not determine
    
    home_dir = get_home_dir()
    connection_files = os.path.join(home_dir, 'ondemand/data/sys/dashboard/batch_connect/sys/jupyter/ncigadi/output/*/connection.yml')
    
    for conn_file in glob(connection_files):
        with open(conn_file) as f:
            conn_info = yaml.safe_load(f)
        password = conn_info['password']

        for srv in _list_maybe_running_servers():
            try:
                sessions = _get_sessions(srv, password)
                for sess in sessions:
                    if sess['kernel']['id'] == kernel_id:
                        return srv, PurePath(sess['notebook']['path'])
            except Exception:
                pass  # There may be stale entries in the runtime directory
            break
    
    return None, None


def name() -> str:
    """ Returns the short name of the notebook w/o the .ipynb extension,
        or raises a FileNotFoundError exception if it cannot be determined.
    """
    _, path = _find_nb_path()
    if path:
        return path.stem
    raise FileNotFoundError(FILE_ERROR.format('name'))


def path() -> Path:
    """ Returns the absolute path of the notebook,
        or raises a FileNotFoundError exception if it cannot be determined.
    """
    srv, path = _find_nb_path()
    if srv and path:
        return Path(get_home_dir()) / Path('.jupyter-root') / path
    raise FileNotFoundError(FILE_ERROR.format('path'))
