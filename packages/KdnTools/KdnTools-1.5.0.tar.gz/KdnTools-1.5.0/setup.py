from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='KdnTools',
    version='1.5.0',
    description="Useful tools for every project.",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/KdntNinja/Code/tree/main/Python/KdnTools",
    author="KdntNinja",
    project_urls={
        "Source": "https://github.com/KdntNinja/Code/tree/main/Python/KdnTools"
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10,<3.12",
    install_requires=["prettytable", "colorama", "requests"],
    packages=find_packages(),
    include_package_data=True,
)


"""





"""