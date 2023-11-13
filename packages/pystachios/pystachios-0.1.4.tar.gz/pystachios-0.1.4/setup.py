from setuptools import setup, find_packages

VERSION = '0.1.4'
DESCRIPTION = "Let's keep testing this thing called pypi"
LONG_DESCRIPTION = ('This is supposed to be a description')

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="pystachios",
    version=VERSION,
    author="Felipe Kautzmann",
    author_email="<recuerdaesto@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)