from setuptools import setup, find_packages


setup(
    name="trackalot",
    version="0.1-dev0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "click",
        "requests",
        "flask",
        "flask-sqlalchemy"
    ],
    entry_points={
        "console_scripts": [
            "trackalot = trackalot.cli:main"
        ]
    }
)
