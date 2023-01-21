from setuptools import find_packages, setup

setup(
    description="Wrapper over pymongo for reliable usage",
    # Application name:
    name="Lib Mongo",
    
    # Version number (initial):
    version="0.1.0",
    
    # Application author details:
    author="Carlos Martins",
    author_email="csmartins.professional@gmail.com",
    
    # Packages
    # packages=["mongo"],
    packages=find_packages(),
    
    # Include additional files into the package
    include_package_data=True,
    
    # Details
    url="https://github.com/csmartins/libmongo",
    
    #
    # license="LICENSE.txt",
    # description="Wrapper over pymongo for reliable usage",
    
    # long_description=open("README.txt").read(),
    
    # Dependent packages (distributions)
    install_requires=[
        "pymongo",
    ]
)