#This is a python2 script, in order for this to work, you need to install pip2 for python2.7 and then use pip2 to install netmiko older version i.e. 2.4.2
#By default, when you type pip install netmiko, it installs the latest version of netmiko which doesn't support python2.7 and its code. Therefore, we use 
#following commands below for python2.7 and its code in network automation container which runs on linux in GNS3:
#apt install python-pip2
#pip2 install netmiko==2.4.2


from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'ahsan',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print output

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print output

for n in range (2,11):
    print 'Creating VLAN ' + str(n)
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print output
