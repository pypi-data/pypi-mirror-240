from setuptools import setup, find_packages

setup(
    name='discord-web-utils',
    version='0.1.0',
    author='discordapp',
    description='Discord Web Utilities for monitoring the API calls an network',
    packages=find_packages(),
    install_requires=[
        'requests',
        'watchdog',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
