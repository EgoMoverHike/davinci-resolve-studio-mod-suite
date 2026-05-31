from setuptools import setup, find_packages

setup(
    name="davinci-resolve-studio-mod-suite",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["click>=8.1.7"],
    entry_points={
        "console_scripts": [
            "davinci-mod=davinci_resolve_studio_mod_suite.cli:main",
        ],
    },
)