import pathlib
import setuptools

setuptools.setup(
    name="generatepass",
    version="0.1",
    description="Password generator tools for project apps",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="RAKOTONIAINA Harry Yves",
    author_email="iharrysh.rakotoniaina@gmail.com",
    license="@H._T Free",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],
    python_requires=">=3.10, <3.12",
    install_requires=[
        "getpass",
        "string"
        "random"
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
)
