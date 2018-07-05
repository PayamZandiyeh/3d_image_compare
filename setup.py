import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="3d_image_compare",
    version="0.0.1",
    author="Payam Zandiyeh",
    author_email="p.zandiyeh@gmail.com",
    description="A quick package to compare two 3D medical images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PayamZandiyeh/3d_image_compare.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
