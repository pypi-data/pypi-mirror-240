from setuptools import setup, find_packages

setup(
    name='LibreriaViajes_UxueAinara',
    version='0.5.6',
    author='Ainara Hoyos y Uxue Garcia',
    description='Una librería para obtener información de interés sobre su destino.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0',
        'termcolor>=1.1.0',
    ],
    package_data={
        'Viajes': ['docs/build/html/index.html'],
    },
)