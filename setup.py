import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="defe",
    version="1.0.0",
    author="Bhupesh Varshney",
    author_email="varshneybhupesh@gmail.com",
    description="A Tech feed Aggregator for Developers.",
    keywords="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["defe", "core"],
    url="https://github.com/Bhupesh-V/defe",
    project_urls={
        "Documentation": "https://defe.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/Bhupesh-V/defe",
        "Funding": "https://www.patreon.com/bePatron?u=18082750",
        "Say Thanks!": "https://github.com/Bhupesh-V/defe/issues/new?assignees=&labels=&template=---say-thank-you.md&title=",
        "Tracker": "https://github.com/Bhupesh-V/defe/issues",
    },
    package_data={
        # include any *.json files found in the "core" module
        "core": ["feeders/*.json"],
    },
    install_requires=["feedparser", "colorama", "tqdm", "diskcache"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Topic :: Education",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Terminals",
        "Topic :: Internet",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["defe=defe.__main__:main"]},
    python_requires=">=3.6",
)
