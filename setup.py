
from setuptools import setup, find_packages
import setuptools

# Usage: python setup.py sdist bdist_wheel

links = []  # for repo urls (dependency_links)

with open("requirements.txt") as fp:
    install_requires = fp.read()

DESCRIPTION = "A python client for setuppythonscript."
VERSION = "1.0"

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    
setup(
      name="setuppythonscript", # projet git
      version=VERSION,
      author='Adama DIENG',
      author_email='adama.dieng@digitastuces.com',  
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://github.com/jengsala/setuppythonscript",
      keywords='development, setup, setuptools',
      license="MIT",
      packages=find_packages(),    # List of all python modules to be installed
      platforms=["any"],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      install_requires=install_requires,
      python_requires='>=3.6', 
      py_modules=["setuppythonscript"],
      package_dir={'':'setuppythonscript/src'}, 
      dependency_links=links,
)