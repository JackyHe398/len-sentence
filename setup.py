from setuptools import setup, find_packages

setup(
    name="len_sentence",
    version="0.1.0",
    author="JackyHe398",
    author_email="hekinghung@gmail.com",
    description="Length of sentence utilities for counting the number of words/characters in a sentence",
    install_requires=[
        "re"
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)

# python setup.py sdist bdist_wheel
# twine upload dist/*