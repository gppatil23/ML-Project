from setuptools import find_packages, setup   # automatically find all packages in application
from typing import List

HYPEN_E_DOT = "-e ." #here -e . we written in requirements.txt file to bind that fiile to this file
def get_requiremets(file_path:str)->List[str]:
    '''
    this Function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='Ml Project',
    version='0.0.1',
    author='Gaurav Patil',
    author_email='gppatil2306@gmail.com',
    packages=find_packages(),
    install_requires= get_requiremets('requirements.txt')
)