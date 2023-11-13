from setuptools import setup, find_packages

setup(
    name='minio_operations',
    version='0.2',
    packages=find_packages(),
    description='Python package for MinIO operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Abouzar Kamaee',
    author_email='abouzarkamaee@gmail.com',
    url='https://github.com/A-Kamaee/minio_operations',
    install_requires=[
        'pandas',
        'minio'
    ],
    python_requires='>=3.6',
)