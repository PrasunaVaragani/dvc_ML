from setuptools import setup

with open('README.md', 'r', encoding = 'utf-8') as f:
    long_description = f.read()

setup(
    name='src',
    version='0.0.3',
    author='varagani',
    description='A small package for dvc ml pipeline',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/PrasunaVaragani/dvc_ML.git',
    author_email='prasuna153@gmail.com',
    packages=['src'],
    license='GNU',
    python_requires='>=3.7',
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]


)