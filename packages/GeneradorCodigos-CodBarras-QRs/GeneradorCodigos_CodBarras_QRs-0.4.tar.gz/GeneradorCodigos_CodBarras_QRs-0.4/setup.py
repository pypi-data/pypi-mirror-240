from setuptools import setup, find_packages

setup(
    name='GeneradorCodigos_CodBarras_QRs',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'qrcode',
        'Pillow',
        'python-barcode',
    ],
    entry_points={
        'console_scripts': [
            'trabajo_grupal.py=GeneradorCodigos_CodBarras_QRs.trabajo_grupal.py:main',
        ],
    },
    author='Sara & Nahia',
    author_email='sara.crego@alumni.mondragon.edu',
    description='Libreria diseñada para la creación de QRs para tiendas con páginas web, especialmente eCommerce, donde además tiene la posibilidad de generar códigos de barras para cada uno de los distintos productos que están a la venta en la tienda.',
    long_description=open('../../GuardarCodigo_Progra_bda4_Sara_Nahia/README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nahiaunceta/GuardarCodigo_Progra_bda4_Sara_Nahia.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        # Otros clasificadores...
    ]

)
