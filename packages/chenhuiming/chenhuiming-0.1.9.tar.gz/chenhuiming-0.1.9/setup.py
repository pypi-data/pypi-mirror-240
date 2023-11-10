#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import join as os_join, abspath as os_abspath, dirname as os_dirname

here = os_abspath(os_dirname(__file__))
with open(os_join(here, 'README.md')) as f:
    README = f.read()  # 把前面准备好的readme.md读进来，下面会用到

setup(
    name="chenhuiming",  # 名字
    version="0.1.9",  # 版本，自己设
    author="chenhuiming",  # 作者声明
    author_email="1250266701@qq.com",  # 作者邮箱
    description="a private package",  #
    license="MIT",  # 开源协议
    classifiers=[
        'Development Status :: 3 - Alpha',  # {3:Alpha, 4:Beta, 5:Production/Stable}  自定版本性质以及下面各种符合条件
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
PLATFORMS = [  # 支持的平台，如果所有平台都支持，可以填 all
    'all',
],
    packages=find_packages(),
    python_requires='>=3',  # python版本需求
    install_requires=[
        'numpy>=1.18.1',
        'librosa==0.9.2',
        'soundfile',  # excel files resolving
        'scikit-learn',
        'pyarmor',
        # some error type of http requests
        # 'matplotlib>=3.1.3',  # for sub_slt_mdl.mdz
        # 'sklearn>=0.22.1',  # for sub_slt_mdl.mdz
    ],  # 会自动安装的环境
    package_data={'pyzohar': ['samples/*.*']},  # 调用演示数据还是啥，忘记了
    include_package_data=True,
)

