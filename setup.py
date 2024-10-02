from setuptools import setup, find_packages

setup(
    name='data-pipeline-project',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pyspark',
        'minio',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'data-pipeline = src.main:main'
        ]
    },
    author='Luan Fonseca',
    author_email='contatos_luan@hotmail.com',
    description='Data Pipeline Project using Spark and MinIO',
    url='https://github.com/tiluan/data-pipeline-project',
)