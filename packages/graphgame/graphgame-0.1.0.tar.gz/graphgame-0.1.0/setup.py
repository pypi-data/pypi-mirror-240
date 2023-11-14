from setuptools import setup, find_packages

setup(
    name='graphgame',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'networkx',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'graphgame=your_package.main:main'  # Replace 'your_package.main:main' with your module path and function
        ]
    },
    description='A simple graph-building game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
