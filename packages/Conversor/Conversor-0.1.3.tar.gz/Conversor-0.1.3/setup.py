from setuptools import setup, find_packages

setup(
    name='Conversor',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Iker',
    author_email='iker.nunez@alumni.mondragon.edu',
    description='El objetivo de este proyecto es desarrollar una librería para Python que facilite la conversión de distintos tipos de medidas.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gorkaelorriaga/nunez_elorriaga/',
    classifiers=[
        'Development Status :: 3 - Alpha',  # Estado de desarrollo del paquete
        'Intended Audience :: Developers',  # Audiencia a la que se dirige el paquete
        'License :: OSI Approved :: MIT License',  # Licencia bajo la que se distribuye el paquete
        'Programming Language :: Python :: 3',  # Versión de Python compatible
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)