from setuptools import setup, find_packages
#import setuptools
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='deutschcase',
  version='0.0.1',
  description='Determine the case of Boolean function',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  author='Amira Mahmoud',
  author_email='amiramahmoudabd@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Deutsch', 
  py_modules=["deutschcase"],
  packages=find_packages("src"),
  package_dir={'': 'src'},
  python_requires=">=3.6",
  install_requires=['']
)
