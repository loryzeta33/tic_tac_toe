from setuptools import setup, find_packages

setup(
    name="tic_tac_toe",
    version="0.1.0",
    author="Lorenzo Zorri",
    author_email="loryzeta33@gmail.com",
    description="A minimal and flexible Tic Tac Toe game implementation in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/loryzeta33/tic_tac_toe",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)
