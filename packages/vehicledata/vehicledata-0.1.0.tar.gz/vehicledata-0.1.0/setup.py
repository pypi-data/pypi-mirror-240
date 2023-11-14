from setuptools import setup, find_packages

setup(
    name="vehicledata",
    version="0.1.0",
    author="Deepak Gautam",
    author_email="rohit45deepak@gmail.com",
    url="https://www.sddoc.in",
    description="A Python package for retrieving vehicle information, including challans and additional details.",
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
