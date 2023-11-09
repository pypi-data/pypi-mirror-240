from setuptools import find_packages, setup

setup(
  author='Anthony Kruger',
  author_email='devadmin@impression.cloud',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Information Technology',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'],
  description='Open Keyshare Threshold Scheme',
  install_requires=['cryptography'],
  keywords='keyshare',
  license='MIT',
  long_description='An M of N key sharing project with split/join functionality and offers password protection on individual key shares with fernet encryption.',
  name='openkts',
  package_data={'openkts': ['__init__.py', '__main__.py', 'common.py', 'sss.py']},
  packages=find_packages(),
  version='1.0.8'
)