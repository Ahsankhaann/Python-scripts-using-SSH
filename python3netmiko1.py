#To use Python3 netmiko SSH script, you need to update the linux references using "apt-get update" command. 
#Then you have to install pip by using "apt-get install python3-pip" and type 'y' to install the software
#Finally, you need to have latest version of netmiko that works with python3, you can do it by using command "pip3 install -U netmiko"
 

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',                                      
    'username': 'ahsan',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print (output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

for n in range (2,11):
    print ('Creating VLAN ' + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print (output)
