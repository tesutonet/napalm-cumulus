"""setup.py file."""

import uuid

from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

__author__ = 'Gabriele Gerbino <gabrielegerbino@gmail.com>'
__maintainer = 'Tesuto Dev <dev@tesuto.com>'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="napalm-cumulus",
    version="0.2.0-tesuto",
    packages=find_packages(),
    author="Gabriele Gerbino",
    author_email="gabrielegerbino@gmail.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/tesutonet/napalm-cumulus",
    include_package_data=True,
    install_requires=reqs,
)
