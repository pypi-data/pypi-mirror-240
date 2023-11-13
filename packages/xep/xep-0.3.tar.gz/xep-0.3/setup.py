from setuptools import setup, find_packages

setup(
    name="xep",
    version="0.3",
    packages=find_packages(exclude=("test*",)),
    license="",
    description="",
    url="https://github.com/Onanim90/xep",
    author="Pavel Ilyin",
    author_email="azunya.90@gmail.com",
    python_requires=">=3.9",
    install_requires=[
        "openpyxl",
        "pyyaml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
