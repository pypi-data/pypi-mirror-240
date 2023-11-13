from setuptools import setup, find_packages


description = "Zenlabs Machine Learning Framework"

setup(
    name="zenlabs-ml-framework",
    version='1.1',
    description=description,
    long_description=description,
    long_description_content_type="text/x-rst",
    url="https://www.zenlabs.com",
    author='Shirish',
    author_email="shirishranjit@gmail.com",
    license='MIT',
    packages=find_packages(),
    package_data={"com/resources": ["*.txt", "*.rst", "config"]},
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
