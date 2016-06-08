from setuptools import setup

setup(
  name = 'pineapple-runtime',
  version = '0.2.0',
  description = 'Run-time environment for controlling Ableton Live sets via pineapple.',
  url = 'http://github.com/alexanderwallin/pineapple-runtime',
  author = 'Alexander Wallin',
  author_email = 'office@alexanderwallin.com',
  license = 'MIT',
  install_requires = [
    'pylive >= 0.1.5',
    'watchdog >= 0.8.3'
  ]
)
