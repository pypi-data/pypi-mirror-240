import setuptools
from pathlib import Path

here = Path(__file__).parent
long_description = (here / 'README.md').read_text()

setuptools.setup(
    name='nci_ipynb',
    version='2023.11.0.2',
    author='Edison Guo',
    author_email='edison.guo@anu.edu.au',
    description='Simply returns either notebook filename or the full path to the notebook when run from Jupyter notebook in browser.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='jupyter notebook filename'.split(),
    url='https://github.com/nci/nci_ipynb',
    packages=setuptools.find_packages(),
    package_data={},
    install_requires=['ipykernel'],
    python_requires='>=3.4',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Framework :: Jupyter',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ]
)
