from setuptools import setup

with open('README.md') as readme:
    readme = readme.read()

version = '1.1'

setup(
    name="freeimagehost",
    version=version,
    description="An unofficial wrapper for the freeimagehost website api.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="samuelmarc",
    license="MIT",
    keywords=["image", "upload", "uploader", "imageuploader"],
    packages=['imagehost'],
    install_requires=['httpx'],
    python_requires=">=3.8"
)
