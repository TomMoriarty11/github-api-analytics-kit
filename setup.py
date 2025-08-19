from setuptools import setup, find_packages

setup(
    name="github_api_analytics_kit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "python-dotenv"
    ],
    author="Thomas Hawkins",
    description="Modular toolkit for GitHub API analytics and profiling",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
