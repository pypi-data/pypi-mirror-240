from setuptools import setup, find_packages

setup(
    name='PyPiston',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'datetime',
        'requests',
        'json',
        'tabulate',
    ],
    author='MarkelUnai',
    author_email='unai.duran@alumni.mondragon.edu',
    description='La librería proporciona una interfaz para interactuar con una API de búsqueda de información sobre coches, gestionando datos de clientes, coches y reservas.',
    url='https://github.com/unaiduran/MarkelUnaiProgra.git',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)