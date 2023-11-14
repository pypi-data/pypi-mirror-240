from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='MiloScraper',
  version='0.0.4',
  description='an project that works like requests but also works on replit',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Culty',
  author_email='sleepyculty@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='scraper', 
  packages=find_packages(),
  install_requires=['cloudscraper'] 
)
