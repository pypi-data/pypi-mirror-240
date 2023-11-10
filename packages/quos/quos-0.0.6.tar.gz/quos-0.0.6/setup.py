import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quos",
    version="0.0.6",
    author="Lalit Patel",
    author_email="LLSR@att.net",
    description="Quos package for plotting and simulating quantum computing circuits employing oscillatory qudits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lapyl/quos",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['matplotlib'],
    package_data = {"quos": ["icons/**/*", "iconx/**/*"],},
)