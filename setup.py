# In The Name Of God
# ========================================
# [] File Name : setup.py
#
# [] Creation Date : 16-11-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
'''
setup module for Aolab.LAN.Agent (I1820Agent)
'''

# Always prefer setuptools over distutils
from setuptools import setup


setup(
    name='i1820agent',

    # Versions should comply with PEP440.
    # For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',


    # Author details
    author='Parham Alvani',
    author_email='parham.alvani@gmail.com',

    packages=['I1820', 'I1820.domain'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed.
    # For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        "wheel",
        "paho-mqtt"
    ],

    setup_requires=[
        'pytest-runner',
    ],

    tests_require=[
        'json-rpc',
        'werkzeug',
        'pytest-asyncio',
    ]
)
