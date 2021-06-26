from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'sql2nosql',
  packages = ['sql2nosql'],
  version = '0.3.31',
  license='MIT',
  description = 'Migrate data from SQL to NoSQL easily',
  author = 'Facundo Padilla',
  author_email = 'facundo.padilla@outlook.com',
  url = 'https://github.com/facundopadilla/sql2nosql',
  download_url = 'https://github.com/facundopadilla/sql2nosql/archive/refs/heads/main.zip',
  keywords = ['sql', 'nosql', 'migrator', 'sql2nosql', 'migrate'],
  install_requires=[
          'simplejson',
          'tqdm',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  include_package_data=True,
  long_description=long_description,
  long_description_content_type='text/markdown'
)