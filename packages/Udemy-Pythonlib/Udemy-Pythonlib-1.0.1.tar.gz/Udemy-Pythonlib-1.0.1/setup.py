from setuptools import setup

with open("readme.md", "r", encoding="utf-8") as arq:
    readme = arq.read()

setup(name='Udemy-Pythonlib',
      version='1.0.1',
      license='MIT License',
      author='Paulocesar0073',
      long_description=readme,
      long_description_content_type="text/markdown",
      author_email='pauloguitarrasoms@icloud.com',
      keywords='udemy',
      description=u'Intereja com a plataforma udemy de forma mais pratica obtenha detalhes e extraia informações de cursos em que você estar inscritos.',
      packages=['Udemy'],
      install_requires=['requests', 'colorama'], )
