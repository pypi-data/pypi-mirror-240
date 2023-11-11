#!/usr/bin/python

from setuptools import setup

setup(name = "er-python-networkmanager",
      version = "2.3",
      author = "Dennis Kaarsemaker",
      author_email = "dennis@kaarsemaker.net",
      maintainer =  "Niels Hvid",
      maintainer_email = "nah@enabled-robotics.com",
      url = "http://github.com/enabled-robotics/python-networkmanager",
      description = "Easy communication with NetworkManager",
      py_modules = ["NetworkManager"],
      install_requires = ["dbus-python", "six"],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: zlib/libpng License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Networking',
      ]
)
