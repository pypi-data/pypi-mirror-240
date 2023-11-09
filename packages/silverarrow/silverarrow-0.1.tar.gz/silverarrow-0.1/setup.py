from setuptools import setup, find_packages

setup(
    name='silverarrow',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'embeddings-cli=embeddings.cli:main',
        ],
    },
)
