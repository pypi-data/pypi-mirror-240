from os.path import join, dirname
from setuptools import setup, find_packages
import meinkonfig


def read(name):
    with open(join(dirname(__file__), name), encoding='utf-8') as file:
        return file.read()


setup(
    name='meinkonfig',
    packages=find_packages(),
    version=meinkonfig.__version__,
    author='vodyanoy',
    author_email='vodyanoy420@gmail.com',
    maintainer='vodyanoy',
    maintainer_email='vodyanoy420@gmail.com',
    url='https://github.com/vodyanoy420/meinkonfig',
    license='MIT',
    keywords=['config', 'yaml', 'yamlconfig', 'meinkonfig'],
    platforms=['Linux', 'Unix', 'Mac OS', 'Windows'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
    ],
    description='YAML config reader',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=read('requirements.txt').split('\n'),
)
