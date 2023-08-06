**This Project Is Used To Convert Network Subnet Mask (For Example: 255.255.255.0) To Prefix Length/CIDR Suffix (For Example: 24) and Vice-Versa.**

Installation
```
# pip install subnetinfo setuptools
# pip install convert_subnet
```

How To Use
```
# convert_subnet -s Subnet_Mask_Value
# convert_subnet -c Prefix_Length_Value
```

Example
| Command	    | Output 		|
| :-------------: |:-------------:|
| # convert_subnet -s 255.255.255.0		| 24
| # convert_subnet -c 28				| 255.255.255.240