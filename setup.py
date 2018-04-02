# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.0'


setup(
    name='pywe-component-token',
    version=version,
    keywords='Wechat Weixin Component PreAuthCode',
    description='Wechat Component PreAuthCode Module for Python.',
    long_description=open('README.rst').read(),

    url='https://github.com/sdkwe/pywe-component-preauthcode',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['pywe_component_preauthcode'],
    py_modules=[],
    install_requires=['pywe_base', 'pywe_component_token', 'pywe_exception', 'pywe_storage'],

    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)