import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ServiceRX",
    version="0.0.1",
    author="Mark Cartagena",
    author_email="mark@mknxgn.com",
    description="MkNxGn ServiceRX, Connects your code to your remote code with seamless interaction.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mknxgn.com/",
    install_requires=['netifaces>=0.10.9'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
