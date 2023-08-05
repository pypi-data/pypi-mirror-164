from pathlib import Path
from setuptools import setup, find_packages

from aoirint_psdlayer2dirpy import __VERSION__ as VERSION

setup(
  name='aoirint_psdlayer2dirpy',
  version=VERSION, # '0.1.0-alpha', # == 0.1.0-alpha0 == 0.1.0a0

  packages=find_packages(),
  include_package_data=True,

  entry_points = {
    'console_scripts': [
      'psdlayer2dir = aoirint_psdlayer2dirpy.main:main',
    ],
  },

  install_requires=Path('requirements.txt').read_text(encoding='utf-8').splitlines(),

  author='aoirint',
  author_email='aoirint@gmail.com',

  url='https://github.com/aoirint/psdlayer2dirpy',
  description='PSDファイルのレイヤー構造＋画像をディレクトリ構造＋PNGとしてダンプするスクリプト',

  long_description=open('README.md', 'r').read(),
  long_description_content_type='text/markdown',

  classifiers=[
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
  ],
)
