"""
    Koverse Data Platform (KDP) API

    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces. Please note that the Python client library follows Python's naming convention of snake casing for fields, even though they may appear in camel case in the API specification. <p><b>By default this api documentation targets the koverse production server at 'api.app.koverse.com' You can provide the hostname of your koverse instance to this documentation page via the 'host' query param.</p> <p><b>For example providing host - https://documentation.koverse.com/api?host=api.myHost.com, will update requests to target the provided host.</b></p> <p><b>Authentication request example with provided host - https://api.myHost.com/authentication</b></p>  # noqa: E501

    The version of the OpenAPI document: 4.96.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "kdp-api-python-client"
VERSION = "4.96.0"
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
    description="Koverse Data Platform (KDP) API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Koverse Data Platform (KDP) API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    The KDP API is a REST API that can be used to create, access, and update data in KDP Workspaces. Please note that the Python client library follows Python&#39;s naming convention of snake casing for fields, even though they may appear in camel case in the API specification. &lt;p&gt;&lt;b&gt;By default this api documentation targets the koverse production server at &#39;api.app.koverse.com&#39; You can provide the hostname of your koverse instance to this documentation page via the &#39;host&#39; query param.&lt;/p&gt; &lt;p&gt;&lt;b&gt;For example providing host - https://documentation.koverse.com/api?host&#x3D;api.myHost.com, will update requests to target the provided host.&lt;/b&gt;&lt;/p&gt; &lt;p&gt;&lt;b&gt;Authentication request example with provided host - https://api.myHost.com/authentication&lt;/b&gt;&lt;/p&gt;  # noqa: E501
    """
)
