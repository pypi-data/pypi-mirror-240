from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="Aishapackage",
    version="2.0.0",
    author="Al-Areef",
    description="A Python package designed to simplify and streamline Paystack API integration, enabling secure \
        online payment processing in your Python applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NUCCASJNR/PaystackPy",  # Replace with your GitHub repository URL
    packages=find_packages(),
    install_requires=["requests"],  # Add any dependencies your package needs
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
