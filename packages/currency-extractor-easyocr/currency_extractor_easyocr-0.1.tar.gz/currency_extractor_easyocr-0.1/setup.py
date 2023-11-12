from setuptools import setup, find_packages

setup(
    name='currency_extractor_easyocr',
    version='0.1',
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
)
