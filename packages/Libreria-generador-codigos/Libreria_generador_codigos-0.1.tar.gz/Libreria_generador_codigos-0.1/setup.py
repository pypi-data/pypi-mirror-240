from setuptools import setup, find_packages

setup(
    name='Libreria_generador_codigos',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'qrcode',
        'Pillow',
        'python-barcode',
    ],
    entry_points={
        'console_scripts': [
            'trabajo_grupal.py=Libreria_generador_codigos.trabajo_grupal.py:main',
        ],
    },
    author='Sara & Nahia',
    author_email='sara.crego@alumni.mondragon.com',
    description='Descripción de tu proyecto',
    url='https://github.com/nahiaunceta/GuardarCodigo_Progra_bda4_Sara_Nahia.git',
)
