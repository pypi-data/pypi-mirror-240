from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rich_graph",
    version="0.0.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["rich_graph"],
    install_requires=[],  # no additional deps needed for install
    extras_require={
        "dev": ["pytest>=3.7", "twine>=4.0"],
    },
    package_dir={"": "src"},
    url="https://github.com/amsifontes/rich_graph",
    author="Anthony Sifontes",
    author_email="anthony.sifontes@gmail.com",
    maintainer="Anthony Sifontes",
    maintainer_email="anthony.sifontes@gmail.com",
)
