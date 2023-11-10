from setuptools import setup

setup(
    name='sevenbridges',
    version='0.0.8',
    description='',
    long_description='',
    author='',
    author_email='',
    url='https://pypi.org/project/sevenbridges',
    license='',
    packages=['src'],
    python_requires='>=3.8',
    install_requires=[
        'pandas',
        'matplotlib',
        'networkx',
        'numpy',
        'scikit-learn',
        'scipy',
        'dtaidistance',
        'libpysal',
    ],
)
