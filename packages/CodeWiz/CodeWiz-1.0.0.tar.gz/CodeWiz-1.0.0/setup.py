import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CodeWiz", # Replace with your own username
    version="1.0.0",
    author="CODABLE",
    author_email="izumi@codable.co.kr",
    description="Communicate with CodeWiz through Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://codable.co.kr/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)