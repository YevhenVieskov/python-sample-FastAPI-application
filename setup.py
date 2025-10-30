from setuptools import setup

setup(
    name='rest_sample',
    version='0.1',
    description='A sample Python package',
    author='John Doe',
    author_email='jdoe@example.com',
    packages=['rest_sample'],
    install_requires=[
        fastapi,
        uvicorn,
        sqlalchemy,
        httpx,
        requests
    ],
)