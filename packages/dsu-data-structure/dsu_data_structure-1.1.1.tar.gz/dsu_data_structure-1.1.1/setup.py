import dsu_data_structure
import setuptools


setuptools.setup(
    name="dsu_data_structure",
    version=dsu_data_structure.__version__,

    author="Dmitry Volkov",
    author_email="d1mav0lk0v@yandex.ru",

    description="Disjoint set union structure implementation for Python 3.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    url="https://github.com/d1mav0lk0v/dsu_data_structure/",
    download_url="https://github.com/d1mav0lk0v/dsu_data_structure/zipball/master/",

    license="MIT License, see LICENSE file",

    packages=["dsu_data_structure",],
    # package=setuptools.find_packages(),
    # install_requires=[],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)