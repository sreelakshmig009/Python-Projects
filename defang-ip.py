def ip_address(address):
    
    split_address = address.split(".")
    
    
    return "[.]".join(split_address)
ipaddress = input()
print(ip_address(ipaddress))
