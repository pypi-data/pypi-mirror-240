from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

DESCRIPTION = 'Upload Files to DMS'
LONG_DESCRIPTION = 'A package that allows users to upload files to DMS'

# Setting up
setup(
    name="dmsuploader",
    version='0.0.3',
    author="MTLM",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['tqdm>=4.66.1', 'requests>=2.31.0'],
    keywords=['python', 'dms', 'uploader'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ]
)