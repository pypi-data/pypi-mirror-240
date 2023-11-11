from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="odoo_resource_assessor",
    version="0.2.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "resource-assessor=odoo_resource_assessor.resource_assessor:main",
        ],
    },
    install_requires=[
        "psutil",
    ],
    author="Lai",
    author_email="sysadmin@coopdevs.org",
    description="A tool to calculate Odoo configuration based on system resources.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.coopdevs.org/coopdevs/sandbox/odoo_resource_assessor",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Framework :: Odoo",
    ],
)
