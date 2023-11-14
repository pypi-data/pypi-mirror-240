from setuptools import setup, find_packages

setup(
    name='recipemaster',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
        "csv",
        "json"
    ],
    author='AsierPaul',
    author_email='asierpaul@gmail.com',
    description='Este proyecto ha sido realizado por Asier Aranoa y Paul Magunazelaia. El objetivo principal de este proyecto es crear una herramienta que permita a los usuarios obtener recetas de cocina en función de los ingredientes que tienen disponibles en casa.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Paulma09/progra_TrabajoGrupal',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)