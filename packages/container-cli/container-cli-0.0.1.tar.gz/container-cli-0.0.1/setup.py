from setuptools import setup
from setuptools import find_packages

VERSION = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="container-cli",
    version=VERSION,
    description='✨A powerful tool for docker containers✨',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='y',
    # url='https://github.com/yixinNB/checkopt',
    packages=find_packages(exclude=['test']),
    # project_urls={
    #     "Documentation": "https://github.com/yixinNB/checkopt",
    #     "Code": "https://github.com/yixinNB/checkopt",
    #     "Issue tracker": "https://github.com/yixinNB/checkopt/issues",
    # },
    entry_points={
        'console_scripts': [
            'cc = container_cli:main',
        ]
    },
    install_requires=[
        'loguru>=0.7',
        'checkopt>=1',
        'questionary>=2'
    ],
)

