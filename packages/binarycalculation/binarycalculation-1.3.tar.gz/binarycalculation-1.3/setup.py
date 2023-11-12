from setuptools import setup
from pathlib import Path

parent_path = Path(__file__).parent
long_description = (parent_path/"binarycalculation/README.md").read_text()

setup(
    name="binarycalculation",
    version="1.3",
    description="Binary Number Operations",
    packages=['binarycalculation'],
    author="josikie",
    author_email="kiejosi12@gmail.com",
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown"
)