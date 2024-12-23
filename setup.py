from setuptools import setup, find_packages

VERSION = '0.0.2' #to be changed during every deployment

setup(
    name='deploy-django',
    version= VERSION,
    package_dir={'': 'main'},
    packages= find_packages(where='main'),
    long_description = 'A simple script for deploying django, visit https://github.com/LSAB23/deploy-django for more infomatoin',
    long_description_content_type= 'text/markdown',
    url = 'https://github.com/LSAB23/deploy-django',
    author= 'Lsab',
    author_email= 'lsabkwaku@gmail.com',
    license= 'MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX',
    ],
    extras_require={
        'dev': ['gunicorn>=23.0.0', 'pythondotenv>=1.0.1']
    },
    python_requires = '>=3.10',
    py_modules=['deploy', 'requirement', 'scripts', 'utils']
)