import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "open-next-cdk",
    "version": "0.0.10",
    "description": "Deploy a NextJS app using OpenNext packaging to serverless AWS using CDK",
    "license": "Apache-2.0",
    "url": "https://github.com/datasprayio/open-next-cdk.git",
    "long_description_content_type": "text/markdown",
    "author": "Dataspray<matus@matus.io>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/datasprayio/open-next-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "open_next_cdk",
        "open_next_cdk._jsii"
    ],
    "package_data": {
        "open_next_cdk._jsii": [
            "open-next-cdk@0.0.10.jsii.tgz"
        ],
        "open_next_cdk": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.105.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.91.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
