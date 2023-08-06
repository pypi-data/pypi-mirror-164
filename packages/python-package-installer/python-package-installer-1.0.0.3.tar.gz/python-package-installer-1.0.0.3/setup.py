from setuptools import find_packages, setup

setup(
    name="python-package-installer", 
    version="1.0.0.3", 
    description="python package installer", 
    author="SML", 
    author_email="seungminlee92@kakao.com", 
    url="https://github.com/seungminlee92/package_installer", 
    license="MIT", 
    packages=find_packages(), 
    data_files=[], 
    install_requires=[
        "importlib_metadata"
    ]
)
