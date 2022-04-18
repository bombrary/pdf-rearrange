import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdf-rearrange",
    version="0.1.0",
    author="bombrary",
    author_email="bombrary@gmail.com",
    description="Rearrange PDF pages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bombrary/pdf-rearrange",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['pdf-rearrange = pdf_rearrange:main']
    },
    python_requires='>=3.7',
)
