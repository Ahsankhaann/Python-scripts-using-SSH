#'iosv_l2_cisco_design' is a cisco configuration guide for acccess switches and it has all the appropriate config in it, so this script is basically open that
#file and copying config from it and then transforming those line by line config file into a list(array) format and then saving it in 'lines' to be sent at
#bottom function when we type net_connect.send_config_set(lines) to apply the appropriate changes after establish SSH connection.
from netmiko import ConnectHandler

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.84',
    'username': 'ahsan',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.85',
    'username': 'ahsan',
    'password': 'cisco',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.86',
    'username': 'ahsan',
    'password': 'cisco',
}

with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
    
    
