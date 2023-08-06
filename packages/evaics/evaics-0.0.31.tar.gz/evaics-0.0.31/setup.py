__version__ = '0.0.31'

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='evaics',
    version=__version__,
    author='Bohemia Automation / Altertech',
    author_email='div@altertech.com',
    description='EVA ICS v4 Python SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alttch/eva4',
    packages=setuptools.find_packages(),
    license='Apache License 2.0',
    install_requires=['elbus>=0.0.14', 'msgpack>=1.0.3'],
    classifiers=('Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Communications'),
)
