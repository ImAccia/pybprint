from setuptools import setup, find_packages


setup(
    name='pybprint',
    packages=['pybprint'],
    version='1.0',
    license='GPL V3.0',
    author="Alex Acciarri",
    author_email='accia.ale@gmail.com',
    package_dir={'': 'src'},
    url='https://github.com/ImAccia/pybprint',
    keywords='print better color colour colors colours',
    install_requires=[
          'colorama',
      ],

)