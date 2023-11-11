
from setuptools import setup, find_packages

setup(
   name="MCDATA",
   version="0.1",
   packages=find_packages(),
   install_requires=[
       'pandas',
       'numpy',
       'boto3',
   ],
   python_requires='>=3.11.6',
   description="Um pacote Python para pré-processar dados públicos",
)
