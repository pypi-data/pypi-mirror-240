from setuptools import setup, find_packages


setup(
    name="mati1daTools",
    version="0.0.1",
    author="mati1da",
    author_email="mati1da.ppx@gmail.com",
    description="常用工具类",
    long_description="常用工具类",
    license="BSD License",
    packages=find_packages(),
    install_requires=[
        "openpyxl==3.1.2",
    ],
)
