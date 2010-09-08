#!/usr/bin/env python

from distutils.core import setup

setup(name='pyfacebook',
      version='0.1',
      description='Python Client Library for the Facebook API',
      author='Samuel Cormier-Iijima',
      author_email='sciyoshi@gmail.com',
      url='http://github.com/alanzoppa/pyfacebook',
      packages=['pyfacebook', 'pyfacebook.djangofb',
          'pyfacebook.djangofb.default_app'])
