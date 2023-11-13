# import setuptools


# setuptools.setup(
# 	# Here is the module name.
# 	name="test_cry",

# 	# version of the module
# 	version="0.0.1",

# 	# Name of Author
# 	author="username_123",

# 	# your Email address
# 	author_email="machanii@outlook.com",

# 	long_description='long_description',
# 	long_description_content_type="text/markdown",

# 	packages=setuptools.find_packages(),


# 	license="MIT",

# 	# classifiers like program is suitable for python3, just leave as it is.
# 	classifiers=[
# 		"Programming Language :: Python :: 3",
# 		"License :: OSI Approved :: MIT License",
# 		"Operating System :: OS Independent",
# 	],
# )


from setuptools import setup, find_packages

long_description = "\n Some logn"

VERSION = '0.0.2'
DESCRIPTION = 'Generating'
LONG_DESCRIPTION = 'A package'

# Setting up
setup(
    name="test_cry",
    version=VERSION,
    author="Name",
    author_email="<info@noname.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)