from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='meross_iot',
    version='0.1.4.3',
    packages=find_packages(exclude=('tests',)),
    url='https://github.com/albertogeniola/MerossIot',
    license='MIT',
    author='Alberto Geniola',
    author_email='albertogeniola@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    description='A simple library to deal with Meross devices. At the moment MSS110, MSS210, MSS310, MSS310H '
                'smart plugs and the MSS425E power strip',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='meross smartplug iot mqtt domotic switch mss310 mss210 mss110 mss425e',
    project_urls={
        'Documentation': 'https://github.com/albertogeniola/MerossIot',
        'Funding': 'https://donate.pypi.org',
        'Source': 'https://github.com/albertogeniola/MerossIot',
        'Tracker': 'https://github.com/albertogeniola/MerossIot/issues',
    },
    install_requires=[
        'paho-mqtt>=1.3.1',
        'requests>=2.19.1'
    ],
    python_requires='>=3.5',
    test_suite='tests'
)
