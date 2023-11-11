# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

import setuptools

from hagworm import __version__


with open(r'README.md', encoding=r'utf8') as stream:
    long_description = stream.read()

setuptools.setup(
    name=r'hagworm',
    version=__version__,
    license=r'Apache License Version 2.0',
    platforms=[r'all'],
    author=r'Shaobo.Wang',
    author_email=r'wsb310@gmail.com',
    description=r'Network Development Suite',
    long_description=long_description,
    long_description_content_type=r'text/markdown',
    url=r'https://gitee.com/wsb310/hagworm',
    packages=setuptools.find_packages(),
    python_requires=r'>=3.7',
    install_requires=[
        r'Cython==3.0.5',
        r'APScheduler==3.10.1',
        r'Pillow==10.1.0',
        r'PyJWT==2.8.0',
        r'PyYAML==6.0.1',
        r'SQLAlchemy==1.3.24',
        r'coredis==4.16.0',
        r'asyncmy==0.2.8',
        r'aiosmtplib==3.0.1',
        r'aio-pika==9.3.0',
        r'cachetools==5.3.0',
        r'confluent-kafka==2.1.1',
        r'cryptography==41.0.5',
        r'elasticsearch==8.1.1',
        r'fastapi==0.95.2',
        r'gunicorn==21.2.0',
        r'grpcio==1.59.2',
        r'hiredis==2.2.3',
        r'httpx==0.25.0',
        r'httptools==0.5.0',
        r'igraph==0.10.6',
        r'loguru==0.7.2',
        r'motor==3.3.1',
        r'msgpack==1.0.5',
        r'ntplib==0.4.0',
        r'psutil==5.9.5',
        r'pyahocorasick==2.0.0',
        r'pytest-asyncio==0.21.0',
        r'python-dateutil==2.8.2',
        r'python-stdnum==1.18',
        r'python-multipart==0.0.6',
        r'qrcode==7.4.2',
        r'requests==2.31.0',
        r'texttable==1.6.7',
        r'ujson==5.7.0',
        r'uvicorn[standard]==0.22.0',
        r'uvloop==0.17.0;sys_platform!="win32"',
        r'xmltodict==0.13.0',
    ],
    classifiers=[
        r'Programming Language :: Python :: 3.7',
        r'License :: OSI Approved :: Apache Software License',
        r'Operating System :: POSIX :: Linux',
    ],
)
