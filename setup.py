import os
import sys
from lbry import __name__, __version__
from setuptools import setup, find_packages

BASE = os.path.dirname(__file__)
with open(os.path.join(BASE, 'README.md'), encoding='utf-8') as fh:
    long_description = fh.read()

PLYVEL = []
if sys.platform.startswith('linux'):
    PLYVEL.append('plyvel==1.3.0')

setup(
    name=__name__,
    version=__version__,
    author="LBRY Inc.",
    author_email="hello@lbry.com",
    url="https://lbry.com",
    description="A decentralized media library and marketplace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="lbry protocol media",
    license='MIT',
    python_requires='>=3.9',
    packages=find_packages(exclude=('tests',)),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'lbrynet=lbry.extras.cli:main',
            'lbry-hub=lbry.wallet.server.cli:main',
            'orchstr8=lbry.wallet.orchstr8.cli:main',
            'lbry-hub-elastic-sync=lbry.wallet.server.db.elasticsearch.sync:run_elastic_sync'
        ],
    },
    install_requires=[
        'aiohttp==3.8.1',
        'aioupnp==0.0.18',
        'appdirs==1.4.4',
        'certifi>=2018.11.29',
        'colorama==0.3.7',
        'distro==1.6.0',
        'base58==2.1.1',
        'cffi==1.15.0',
        'cryptography==3.4.7',
        'protobuf==3.17.2',
        'msgpack==1.0.3',
        'prometheus_client==0.12.0',
        'ecdsa==0.17.0',
        'pyyaml==6.0',
        'docopt==0.6.2',
        'hachoir',
        'multidict==5.2.0',
        'coincurve==16.0.0',
        'pbkdf2==1.3',
        'attrs==21.2.0',
        'pylru==1.2.0',
        'elasticsearch==7.10.1',
        'grpcio>=1.43.0'
    ] + PLYVEL,
    extras_require={
        'torrent': ['lbry-libtorrent'],
        'lint': ['pylint==2.10.0'],
        'test': ['coverage'],
    },
    classifiers=[
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
    ],
)
