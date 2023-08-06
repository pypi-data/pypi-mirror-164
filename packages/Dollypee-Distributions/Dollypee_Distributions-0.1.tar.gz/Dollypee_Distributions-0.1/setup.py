from setuptools import setup
from pathlib import Path

setup(name='Dollypee_Distributions',
      version='0.1',
      description=Path("README.md").read_text(),
      packages=['distributions'],
      zip_safe=False)
