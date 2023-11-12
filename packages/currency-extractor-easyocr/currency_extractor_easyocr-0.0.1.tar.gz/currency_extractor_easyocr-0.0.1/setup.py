from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='currency_extractor_easyocr',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'easyocr',
    ],
    entry_points={
        'console_scripts': [
            'currency_symbol_extract=currency_extractor_easyocr.currency_extract:main',
        ],
    },
    description='Extract Currency Symbols on image using EasyOCR',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
