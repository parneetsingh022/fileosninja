from setuptools import setup, find_packages
import pathlib

VERSION = '0.0.2'
DESCRIPTION = 'A versatile Python module for streamlined file I/O operations and essential OS-related tasks. Simplify your code with the power of fileosninja, providing a cohesive and efficient solution for reading and writing files, along with seamless integration of operating system functionalities. Empower your projects with the core capabilities of fileosninja, designed for simplicity and performance.'

# Setting up
setup(
    name="fileosninja",
    version=VERSION,
    author="Parneet Sidhu",
    author_email="parneetsingh022@gmail.com",
    description=DESCRIPTION,
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['docs', 'requirements.txt']),
    install_requires=[],
    license="The Unlicense",
    project_urls={
        "Documentation": "https://parneetsingh022.github.io/fileosninja/",
        "Source":"https://github.com/parneetsingh022/fileosninja"
    },
    keywords=['file IO', 'OS operations', 'Python module', 'file handling', 'operating system utilities'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True
)