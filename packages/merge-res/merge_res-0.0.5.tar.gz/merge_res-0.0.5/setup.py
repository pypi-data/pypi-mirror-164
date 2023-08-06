from setuptools import find_packages, setup

setup(
  name="merge_res",
  version="0.0.5",
  author="malinkang",
  author_email="linkang.ma@gmail.com",
  description="",
  long_description="",
  url="https://malinkang.com",
  packages=find_packages(),
    entry_points={
        "console_scripts": ["merge_res = merge_res.cli:main"],
    },
)