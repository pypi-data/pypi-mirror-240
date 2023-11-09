import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name='pybd_gui',    # This is the name of your PyPI-package.
    version='1.3.7',
    url='https://github.com/ryanGT/pybd_gui',
    author='Ryan Krauss',
    author_email='ryanwkrauss@gmail.com',
    description="gui front end for the modeling controls block diagrams in python",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    install_requires=[
          'py_block_diagram',  \
          'krauss_misc', \
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
