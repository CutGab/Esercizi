import re

def is_valid_ipv4(address: str) -> bool:
    
    is_valid = re.match(
        r'^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.'
        r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.'
        r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.'
        r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$',
        address
    )
    return bool(is_valid)

print(is_valid_ipv4("192.168.0.1")) # True
print(is_valid_ipv4("255.255.255.255")) # True
print(is_valid_ipv4("256.100.10.1")) # False (256 è fuori range)
print(is_valid_ipv4("192.168.1")) # False (solo 3 parti)
print(is_valid_ipv4("192.168.1.a")) # False (parte non numerica)