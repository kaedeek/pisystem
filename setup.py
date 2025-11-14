from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pynexusx",
    version="1.1.0",
    description="A simple CLI tool to update all Python packages using VersaLog.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="kaede",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "VersaLog",
        "plyer",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "Pyn = pynexusx.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: System :: Software Distribution",
        "Intended Audience :: Developers",
    ],
)
