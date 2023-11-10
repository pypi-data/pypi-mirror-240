from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='gpt_pdf_reader',
    version='0.1',
    packages=find_packages(),
    description='A Python package that utilizes GPT-4V and other tools to extract and process information from PDF files',
    install_requires=required_packages,
)