import sys
from setuptools import setup

setup(
   name='auto-tag-anime',
   version='1.0',
   description='adds tags to anime images predicted by DeepDanbooru tensorflow model',
   install_requires=['tensorflow == 2.0', 'numpy', 'pillow', ] + ["iptcinfo"] if "win" in sys.platform else ['xattr'],
) 
