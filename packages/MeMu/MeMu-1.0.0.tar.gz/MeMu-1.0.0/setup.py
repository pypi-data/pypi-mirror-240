from setuptools import setup, find_packages

setup(
    name='MeMu',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['fonts/*.ttf', 'images/*.png', 'icons/*.ico'],
    },
    install_requires=[
        'customtkinter>=5.1.3',
        'PIL>=9.4.0',
        'pyboy>=1.6.6'
    ],
)