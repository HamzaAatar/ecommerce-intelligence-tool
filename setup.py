from setuptools import setup, find_packages

setup(
    name="ecommerce-intelligence-tool",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "requests",
        "pandas",
        "selenium",
        "webdriver-manager",
        "rich",
        "click",
        "tqdm",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "ecommerce-tool=ecommerce_tool.cli:main",
        ],
    },
    author="Hamza ATTAR",
    description="E-commerce website intelligence aggregation tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HamzaAatar/ecommerce-intelligence-tool",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)
