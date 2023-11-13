from setuptools import setup, find_packages

setup(
    name='pictriage',
    version='1.0.6',
    author='Author Name',
    author_email='author@example.com',
    description='Description of my package',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'starlette',
        'uvicorn',
        'ibis==3.2.0',
        'natsort==8.4.0',
        'python-multipart',
    ],
    entry_points={
        'console_scripts': ['pictriage=pictriage:main'],
    },
)
