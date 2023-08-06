# import setuptools
# from setuptools import find_packages  # or find_namespace_packages
from setuptools import setup, find_packages
# setup(use_scm_version=True)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="src",
    version="0.0.1",
    author="Joel Yancey,",
    author_email="joelgyancey@ucla.edu",
    description="AlignEM-SWIFT is a graphical tool for aligning serial section electron micrographs using SWiFT-IR.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms=["any"],
    url="https://github.com/mcellteam/swift-ir/tree/development_ng",
    packages=find_packages(),

)


# $ python setup.py --help-commands
#
# And you will get:
#
# Standard commands:
#   build             build everything needed to install
#   build_py          "build" pure Python modules (copy to build directory)
#   build_ext         build C/C++ extensions (compile/link to build directory)
#   build_clib        build C/C++ libraries used by Python extensions
#   build_scripts     "build" scripts (copy and fixup #! line)
#   clean             clean up temporary files from 'build' command
#   install           install everything from build directory
#   install_lib       install all Python modules (extensions and pure Python)
#   install_headers   install C/C++ header files
#   install_scripts   install scripts (Python or otherwise)
#   install_data      install data files
#   sdist             create a source distribution (tarball, zip file, etc.)
#   register          register the distribution with the Python package index
#   bdist             create a built (binary) distribution
#   bdist_dumb        create a "dumb" built distribution
#   bdist_rpm         create an RPM distribution
#   bdist_wininst     create an executable installer for MS Windows
#   upload            upload binary package to PyPI
#
# Extra commands:
#   rotate            delete older distributions, keeping N newest files
#   develop           install package in 'development mode'
#   setopt            set an option in setup.cfg or another config file
#   saveopts          save supplied options to setup.cfg or other config file
#   egg_info          create a distribution's .egg-info directory
#   upload_sphinx     Upload Sphinx documentation to PyPI
#   install_egg_info  Install an .egg-info directory for the package
#   alias             define a shortcut to invoke one or more commands
#   easy_install      Find/get/install Python packages
#   bdist_egg         create an "egg" distribution
#   test              run unit tests after in-place build
#   build_sphinx      Build Sphinx documentation
#
# usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
#    or: setup.py --help [cmd1 cmd2 ...]
#    or: setup.py --help-commands
#    or: setup.py cmd --help

