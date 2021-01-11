from setuptools import setup, find_packages

setup(
    name="eastern-ceylon",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "eastern>=2.0",
    ],
    entry_points={"eastern.plugin": ["ceylon = eastern_ceylon.plugin:CeylonPlugin"]},
)
