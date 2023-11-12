from setuptools import setup, find_packages

setup(
    name='OpenLibraryProgramacion',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'datetime'
    ],
    entry_points={
        'console_scripts': [
            'programacion_libreria = programacion_libreria.ipynb',
        ],
    },
    author='Julene Arias y Alba Sanz',
    author_email='alba.sanz@alumni.mondragon.edu',
    description='Biblioteca para consultar información sobre libros y sus autores.',
    long_description=open('README.md').read(),
    long_description_content_type='La biblioteca contiene funciones para poder obtener infromación sobre libros y escritores, de manera que, con el título de un libro, se podrían saber cuántos libros ha escrito ese autor en los últimos 5 años, entre muchas otras funcionalidades.',
    url='https://github.com/julenearias/progra_actgrup4.git',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
