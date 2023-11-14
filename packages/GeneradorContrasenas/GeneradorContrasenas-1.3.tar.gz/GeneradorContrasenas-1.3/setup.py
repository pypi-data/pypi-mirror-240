from distutils.core import setup

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
  name = 'GeneradorContrasenas',         # How you named your package folder (MyLib)
  packages = ['GeneradorContrasenas'],   # Chose the same as "name"
  version = '1.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Generador de una o varias contraseñas personalizadas en base a los requisitos especificados por el usuario',   # Give a short description about your library
  author = 'Nerea Barrueta & Alba Vilches',                   # Type in your name
  author_email = 'nerea.barrueta@alumni.mondragon.edu',      # Type in your E-Mail
  url = 'https://github.com/nereabarrueta/GeneradorContrasenas',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/nereabarrueta/GeneradorContrasenas/archive/refs/tags/V05.tar.gz',    # I explain this later on
  keywords = ['Generar', 'Contrasena', 'Seguridad'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      ],
  long_description = open('README.md', encoding= 'utf-8').read(),
  long_description_content_type = 'text/markdown',
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
],
)