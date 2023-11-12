# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='Generador_Codbarras_QRs',
    version='0.1',
    license='MIT', 
    packages=find_packages(),
    install_requires=[
        'qrcode',
        'Pillow',
        'python-barcode',
    ],
    entry_points={
        'console_scripts': [
            'trabajo_grupal.py=Generador_Codbarras_QRs.trabajo_grupal.py:main',
        ],
    },
    author='Sara & Nahia',
    author_email='sara.crego@alumni.mondragon.edu',
    description='Libreria diseñada para la creación de QRs para tiendas con páginas web, especialmente eCommerce, donde además tiene la posibilidad de generar códigos de barras para cada uno de los distintos productos que están a la venta en la tienda.',
    long_description=open('../../GuardarCodigo_Progra_bda4_Sara_Nahia/README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nahiaunceta/GuardarCodigo_Progra_bda4_Sara_Nahia.git',
    classifiers=[
            'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
            'Intended Audience :: Developers',      # Define that your audience are developers
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',   # Again, pick a license
            'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'
    ],
    package_data={
        'Generador de codigos (QR, Cod. barras)': ['docs/_build/index.html']
    }
)
