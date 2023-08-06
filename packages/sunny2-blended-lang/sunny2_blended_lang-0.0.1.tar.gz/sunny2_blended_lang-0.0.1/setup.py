from setuptools import setup, find_packages
VERSION = '0.0.1'
DESCRIPTION = 'Test package'
LONG_DESCRIPTION = 'Test package'

# Setting up
setup(
    name="sunny2_blended_lang",
    version=VERSION,
    author="sunny",
    author_email="<sprakash@cognam.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['markupsafe']
)