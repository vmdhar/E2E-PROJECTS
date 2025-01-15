from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    HYPHEN_E_DOT="-e ."
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name="E2E-Projects",
    version="0.0.0.1",
    author="Muralidhar",
    author_email="vmdhar.vvit@gmail.com",
    packages=find_packages(),
    install_requres=get_requirements("requirements.txt")
    
)