#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from pip._internal.req import parse_requirements
import os 

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

try:
    # pip >=20
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.download import PipSession
        from pip.req import parse_requirements

requirements = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt'), session=PipSession())
reqs = [str(requirement.requirement) for requirement in requirements]


setup(
    name='neosign',
    python_requires='>=3.5',
    version='0.2.2',
    description="Utility for signing arbitrary messages with NEP2 Keypairs or WIF",
    long_description="Fun",
    author="City of Zion",
    author_email='python@cityofzion.io',
    url='https://github.com/CityOfZion/neosign',
    packages=find_packages(include=['neosign']),
    include_package_data=True,
    install_requires=reqs,
    entry_points = {
        'console_scripts': [
            'neosign=neosign.sign:main'
        ]
    },
    license="MIT license",
    zip_safe=False,
    keywords='neocore, neo, python, node',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
