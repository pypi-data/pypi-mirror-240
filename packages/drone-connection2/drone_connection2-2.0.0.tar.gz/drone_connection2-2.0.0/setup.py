import setuptools
import pathlib

setuptools.setup(
    name="drone_connection2",
    version="2.0.0",
    description="Drone connection",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="RAKOTONIAINA Harry Yves",
    author_email="iharrysh.rakotoniaina@gmail.com",
    classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Utilities",
    ],
    python_requires=">=3.10, <3.11",
    packages=setuptools.find_packages(),
    include_package_data=True, 
    license="@H._T Free",
)

