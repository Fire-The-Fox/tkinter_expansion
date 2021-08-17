from setuptools import find_packages, setup

with open('README.md') as readme_file:
  README = readme_file.read()

setup(
  name = 'tkinter_expansion',
  packages = ['tkinter_expansion'],
  version = '0.0.1',
  license='MIT',
  description = 'Python package that extends tkinter with custom Designer',
  long_description_content_type="text/markdown",
  long_description=README,
  author = 'Fire-The-Fox',
  author_email = 'gajdos.jan77@gmail.com',
  keywords = ['TKINTER', 'DESIGNER'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)