from distutils.core import setup
setup(
  name = 'sql2nosql',         # How you named your package folder (MyLib)
  packages = ['sql2nosql'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Migrate data from SQL to NoSQL easily',   # Give a short description about your library
  author = 'Facundo Padilla',                   # Type in your name
  author_email = 'facundo.padilla@outlook.com',      # Type in your E-Mail
  url = 'https://github.com/facundopadilla/sql2nosql',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/facundopadilla/sql2nosql/archive/refs/heads/main.zip',    # I explain this later on
  keywords = ['sql', 'nosql', 'migrator', 'sql2nosql', 'migrate'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'simplejson',
          'tqdm',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)