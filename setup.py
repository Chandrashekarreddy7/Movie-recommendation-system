from setuptools import setup

with open("Readme.md",'r',encoding="utf-8") as fh:
    long_description=fh.read()

author_name="Chandrashekar reddy"
src_repo="src"
List_of_requirements=['streamlit']
setup(
    name=src_repo,
    version='0.0.1',
    author=author_name,
    description="A small example package for movie recommedation",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package=[src_repo],
    python_requires='>=3.7',
    install_requires=List_of_requirements
)