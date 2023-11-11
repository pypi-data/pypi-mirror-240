from setuptools import setup, find_packages

# Read the content of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='base_conversion_kit',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'markdown'
    ],
    python_requires='>=3.6',
    project_urls={
        'Funding': 'https://ko-fi.com/porfanid',
        'GitHub': 'https://github.com/porfanid/base-conversion-kit'
    },
    description='A simple package to convert numbers to different bases and work with them',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
