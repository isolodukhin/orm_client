from setuptools import setup

REQUIRES = [
    'records',
    'sqlalchemy',
    'structlog'
]

setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/isolodukhin/orm_client.git',
    license='MIT',
    author='ilaso',
    author_email='Ilya',
    install_requirements=REQUIRES,
    description='orm_client with allure and logger'
)
