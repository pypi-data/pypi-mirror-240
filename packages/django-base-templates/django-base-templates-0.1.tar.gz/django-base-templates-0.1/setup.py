import setuptools
import pathlib

setuptools.setup(
    name="django-base-templates",
    version="0.1",
    packages=setuptools.find_packages(),
    description="Adding base templates for django apps",
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
)