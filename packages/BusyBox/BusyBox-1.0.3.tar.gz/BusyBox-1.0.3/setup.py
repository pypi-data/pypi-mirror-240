# coding=utf-8

from setuptools import setup, find_packages


def readme():
    with open('./README.md', encoding="utf-8") as f:
        _long_description = f.read()
        return _long_description


setup(
    name='BusyBox',
    version="1.0.3",
    description=(
        """
            dependency injector
        """
    ),
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords=['inject', 'depend', 'invoke', 'BusyBox'],
    author='Jaysen Leo',
    author_email='jaysenleo@163.com',
    maintainer='Jaysen Leo',
    maintainer_email='jaysenleo@163.com',
    license='MIT License',
    packages=['BusyBox'],
    platforms=["linux", 'windows'],
    url='https://github.com/AngelovLee/BusyBox',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
    ]
)