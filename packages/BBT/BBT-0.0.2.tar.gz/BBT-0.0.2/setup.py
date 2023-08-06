from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3.7'
]
 
setup(
  name='BBT',
  version='0.0.2',
  description='BBT GAME AND SHELDON JOKES',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Djsmanoj0000',
  author_email='djsmanoj0000@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Game', 
  packages=find_packages(),
  install_requires=[''] 
)