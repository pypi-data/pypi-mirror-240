from setuptools import setup, find_packages


VERSION = '0.0.25'
DESCRIPTION = 'some'
LONG_DESCRIPTION = 'some'

# Setting up
setup(
    name="diffydes",
    version=VERSION,
    author="Your Name",
    author_email="yourname@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)