from setuptools import setup

setup(
    name='yaml_creator',
    version='0.1',
    packages=['yaml_creator'],
    install_requires=[
        'pyyaml'
    ],
    author='Andrey Alscher',
    author_email='andrewalscher@gmail.com',
    description='A library for managing Kubernetes resource deployments',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AndrewAlscher/phd_project_full/tree/main/resource_management/yaml_creator/yaml_creator_library',
)