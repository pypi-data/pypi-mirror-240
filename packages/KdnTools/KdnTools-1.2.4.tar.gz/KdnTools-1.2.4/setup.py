from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='KdnTools',
    version='1.2.4',
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
    install_requires=["prettytable", "colorama"],
    extras_require={
        "dev": ["pytest", "twine", "wheel"],
        "test": ["pytest"],
        "docs": ["sphinx", "sphinx_rtd_theme"],
        "lint": ["flake8", "black", "isort"],
        "format": ["black", "isort"],
    },
    packages=find_packages(),
    include_package_data=True,
)


"""
Remove-Item -Recurse -Force dist ; python setup.py sdist bdist_wheel ; twine upload dist/* 
pip install --upgrade KdnTools
"""