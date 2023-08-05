"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    The version of the OpenAPI document: 2.11.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "channelengine-merchant-api-client"
VERSION = "2.12.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="ChannelEngine Merchant API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/channelengine/merchant-api-client-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "ChannelEngine Merchant API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    ChannelEngine API for merchants  # noqa: E501
    """
)
