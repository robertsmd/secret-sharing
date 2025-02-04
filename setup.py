"""
Secret Sharing
==============

"""

from setuptools import setup

setup(
    name='secretsharing',
    version='0.3.7',
    url='https://github.com/robertsmd/secret-sharing',
    license='MIT',
    author='robertsmd',
    author_email='',
    description=("Tools for sharing secrets (like Bitcoin private keys), "
                 "using shamir's secret sharing scheme."),
    packages=[
        'secretsharing',
    ],
    zip_safe=False,
    install_requires=[
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
)
