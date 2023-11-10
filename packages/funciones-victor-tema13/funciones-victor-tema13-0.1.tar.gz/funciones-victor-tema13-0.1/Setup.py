from setuptools import setup

setup(
    # Se especifica el nombre de la librería
    name = 'funciones-victor-tema13',
    # Se especifica el nombre del paquete
    packages = ['funciones'],
    # Se especifica la versión, que va aumentando con cada actualización
    version = '0.1',
    # Se especifica la licencia escogida
    license='MIT',
    # Breve descripción de la librería
    description = 'Libreria ejemplo Tema 13',
    # Nombre del autor
    author = 'Victor Olivares',
    # Email del autor
    author_email = 'xxx@gmail.com',
    # Palabras claves de la librería
    keywords = ['mates', 'operaciones'],

    #Librerías externas que requieren la librería
    classifiers=[
        # Se escoge entre "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        # según el estado de consolidación del paquete
        'Development Status :: 3 - Alpha',
        # Se define el público de la librería
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Se indica de nuevo la licencia
        'License :: OSI Approved :: MIT License',
        #Se definen las versiones de python compatibles con la librería
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)