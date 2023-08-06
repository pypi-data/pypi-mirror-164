from setuptools import find_packages, setup

setup(
  name="smalii",
  version="0.0.3",
  author="malinkang",
  author_email="linkang.ma@gmail.com",
  description="",
  long_description="",
  url="https://github.com/malinkang/smalii",
  packages=find_packages(),
    entry_points={
        "console_scripts": ["smalii = .cli:main"],
    },
)