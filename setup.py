from setuptools import setup, find_packages

version = '1.0.0'

requires = [
    'setuptools',
    'zc.buildout',
    'zc.recipe.egg',
]

setup(name='corejet.recipe.testrunner',
      version=version,
      description="ZC Buildout recipe for creating CoreJet test runners",
      long_description=open("README.txt").read() + "\n" +
                       open("HISTORY.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          ],
      keywords='corejet recipe',
      author='Asko Soukka',
      author_email='asko.soukka@iki.fi',
      url='https://github.com/datakurre/corejet.recipe.testrunner/',
      license='ZPL 2.1',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['corejet', 'corejet.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""
      [zc.buildout]
      default = corejet.recipe.testrunner:TestRunner
      """,
      )
