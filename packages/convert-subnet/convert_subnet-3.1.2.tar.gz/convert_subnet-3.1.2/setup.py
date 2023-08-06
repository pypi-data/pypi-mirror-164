import os
import sys
import setuptools
#from setuptools import setup, find_packages

with open('/opt/script/convert_subnet/requirements.txt') as f:
    requirements = f.readlines()

with open("/opt/script/convert_subnet/README.md", "r") as fh:
    long_description = fh.read()
    
#long_description = 'Convert Prefix Length To Subnet Mask & Vice-Versa'

setuptools.setup(
        name ='convert_subnet',
        version ='3.1.2',
        author ='LongDT15',
        author_email ='longdt15@fpt.com.vn',
        url ='https://github.com/VietDuc19',
        description ='convert_subnet: Convert Prefix Length To Subnet Mask & Vice-Versa',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages=setuptools.find_packages(),
        entry_points ={
            'console_scripts': [
                'convert_subnet = convert_subnet.convert_subnet:main'
            ]
        },
        classifiers =[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        keywords ='network subnet_mask Prefix_Length CIDR Suffix',
        install_requires = requirements,
        zip_safe = False
)
