import setuptools

from hina.sdk import SDK_VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="HinaCloudSDK",
    version=SDK_VERSION,
    author="hina",
    author_email="hina@hinadt.com",
    description="This is the official Python SDK for Hina Analytics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://git.hinadt.com/hina-cloud-sdk/hina-cloud-python-sdk.git",
    packages=setuptools.find_packages(),
)
