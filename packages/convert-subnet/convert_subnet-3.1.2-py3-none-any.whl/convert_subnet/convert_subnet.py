# Requiment: https://pypi.org/project/subnetinfo/
# pip install subnetinfo setuptools
import socket
import struct
from argparse import ArgumentParser
from subnet_info import SubnetInfo

# Convert Subnet Mask To CIDR: 255.255.255.0 -> 24
def netmask_to_cidr(subnetmask_input):
    _subnet = SubnetInfo()
    value = _subnet.calculate_cidr(subnet_mask=str(subnetmask_input))
    print(value)

# Convert CIDR To Subnet Mask: 24 -> 255.255.255.0
def cidr_to_subnetmask(cidr_input):
    host_bits = 32 - int(cidr_input)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    print(netmask)

def main():
    argparser = ArgumentParser('convert_subnet')
    argparser.add_argument('-s', '--subnetmask', default=None, help='Subnet Mask Value (Example: 255.255.255.0)')
    argparser.add_argument('-c', '--cidr', default=None, help='Prefix Length (Example: 24)')
    args = argparser.parse_args()
    
    subnetmask = args.subnetmask
    cidr = args.cidr
    
    if subnetmask != None and cidr != None:
        print("Only One Option At The Same Time")
    elif subnetmask != None:
        netmask_to_cidr(subnetmask)
    elif cidr != None:
        cidr_to_subnetmask(cidr)
    else:
        print("Please Specify Option")

# Neu Muon Chay Script Va Output Ra Man Hinh Terminal Thi Uncomment Doan Sau. Khi Chay python /PATH2/SCRIPT.py, No Se Execute Function main De Chay. Lam Nhu The Nay, Function main Se Chi Duoc Execute Neu Chay Script, Khong Phai Khi Import File (Avoiding Having The Interpreter Assign __name__ To __main__, Which Could Cause Code To Be Imported Twice (If Another Module Imports Script)).
# Neu Muon Compile & Upload Len Pypi Thi Nen Comment Doan Sau
#if __name__ == '__main__':
#    main()

# Call A Specific Python Function In A File From The Command Line, Nho Uncomment Doan if __name__ == '__main__': main()
# python -c "from file_name.py import function;function()"