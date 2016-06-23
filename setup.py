##############################################################################
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# Author: Sylvain Gubian, PMP SA
##############################################################################
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pytest',
    'rpy2',
    'asciitable',
    'xlsxwriter',
    'sphinx',
    'sphinxleash',
    'sphinx_bootstrap_theme',
    ]

setup(name='gensabench',
      version='0.0.1',
      description='Set of tools for benchmarking GenSA General Simulated Annealing algorithm',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        ],
      author='Sylvain Gubian, PMP SA',
      author_email='sylvain.gubian@pmi.com',
      url='https://github.com/sgubianpm/gensabench',
      keywords='optimization benchmarking simulated annealing',
      packages=find_packages(),
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="bench",
      entry_points = """\
      """,
      )

