from __future__ import absolute_import

from os import path

from setuptools import setup, find_packages

_dir = path.abspath(path.dirname(__file__))

with open(path.join(_dir, 'mfconnect', 'version.py')) as f:
    exec(f.read())

with open(path.join(_dir, 'README.md')) as f:
    long_description = f.read()

setup(name='mfconnect',
    version=__version__,
    description='mfconnect simplifies telnet and ftp connections to Meteo France HPC servers thru the MF gateway.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.mercator-ocean.fr/internal/mfconnect',
    author='Matthieu Clavier',
    author_email='mclavier@mercator-ocean.fr',
    license='BSD Licence',
    packages=find_packages(exclude=["test"]),
    package_data={
        'mfconnect': ['meteorc','meteo_completion'],
    },

    project_urls={
        'Repository': 'https://gitlab.mercator-ocean.fr/internal/mfconnect',
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Terminals :: Telnet',
        'Environment :: Console',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: BSD License',
    ], 

    install_requires = [
        'pexpect>= 4.8.0',
        'pyyaml==5.3.1',
        'namedtupled==0.3.3',
    ],

    setup_requires=['flake8'],
    tests_require=['pytest', 'pytest_cov'],
    python_requires = '>=3.6,<3.9',
)
