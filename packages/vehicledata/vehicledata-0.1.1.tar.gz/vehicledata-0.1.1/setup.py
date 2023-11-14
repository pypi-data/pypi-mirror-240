from setuptools import setup, find_packages

setup(
    name="vehicledata",
    version="0.1.1",
    author="Deepak Gautam",
    author_email="rohit45deepak@gmail.com",
    url="https://www.sddoc.in",
    
    description="A Python package for retrieving vehicle information, including challans and additional details.",
    long_description="This package provides a Python interface for retrieving information about vehicles, including details about challans and additional information. check docs in https://github.com/deepakstark01/getvehicledata ",
    long_description_content_type="text/plain",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    entry_points={
        'console_scripts': [
            'getvehicle=vehciledata:src.details.getvehicle',
        ],
    },
)
