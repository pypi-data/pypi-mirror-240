import ipaddress

def calculate_valid_hosts_count(prefix_length):
    prefix_length = int(prefix_length)
    return 2 ** (32 - prefix_length) - 2

def is_network_ip(ip_str):
    try:
        ip = ipaddress.IPv4Address(ip_str)
        network = ipaddress.IPv4Network(f"{ip_str}/{prefix_length}", strict=False)
        return ip == network.network_address
    except (ipaddress.AddressValueError, ValueError):
        return False

def get_valid_host_range(ip_str, prefix_length):
    network = ipaddress.IPv4Network(f"{ip_str}/{prefix_length}", strict=False)
    start_ip = network.network_address + 1
    end_ip = network.broadcast_address - 1
    return start_ip, end_ip
# while True:
    # ip_prefix=input('enter the subnet: ')
    # if ip_prefix == 'q': break
    # if ip_prefix.find('/') != -1 :
        # ip =ip_prefix.split('/')[0]
        # prefix_length = ip_prefix.split('/')[1]  # Corresponds to a subnet mask of 255.255.255.0
        # valid_hosts_count = calculate_valid_hosts_count(prefix_length)
        # start, end = get_valid_host_range(ip, prefix_length)

        # if is_network_ip(ip, prefix_length):
            # print(f"{ip} is a network IP. Number of valid hosts in the subnet: {valid_hosts_count} starts at {start} end at {end}")
        # else:
            # print(f"{ip} is a host IP. Number of valid hosts in the subnet: {valid_hosts_count} starts at {start} end at {end}")
    # else:
        # for prefix_length in range(8, 31):
            # ip = ip_prefix
            # if is_network_ip(ip, prefix_length):
                # valid_hosts_count = calculate_valid_hosts_count(prefix_length)
                # start, end = get_valid_host_range(ip, prefix_length)
                # print(f"{ip} is a network IP.Prefix is:{prefix_length} Number of valid hosts in the subnet: {valid_hosts_count} starts at {start} end at {end}")
            # else:
                # valid_hosts_count = calculate_valid_hosts_count(prefix_length)
                # start, end = get_valid_host_range(ip, prefix_length)
                # print(f"{ip} is a host IP.Prefix is:{prefix_length} Number of valid hosts in the subnet: {valid_hosts_count} starts at {start} end at {end}")

