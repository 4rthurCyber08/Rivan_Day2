
## Given Values
company_name = None
total_users = None
user_list = None
ip_space = None
reserved_ip = None
vlan = None

## Answers
host_bits = None
new_net_bits = None
new_cidr = None

rivan_format = None
increment = None
octet = None

company_net_ip = None
company_net_mask = None

first_valid = None
last_valid = None
broadcast = None

not_net_ip = None
not_net_mask = None

question_temp = f'''
Design a network for {company_name} with {total_users} {user_list}. 
- Use the available IP address space {ip_space}
- Reserve the first {reserved_ip} IP addresses of the network.
- Set the network for VLAN {vlan}
'''

answer_temp = f'''
C: {total_users} = {host_bits} bits

S: /32 - {host_bits} = {new_cidr} {rivan_format}

I: Ipasok {increment} sa {octet} octet = {company_net_ip} {company_net_mask}

--

NETWORK: ({company_name}) = {company_net_ip} {company_net_mask}
VALID RANGE:
- FIRST VALID IP = {first_valid}
- LAST VALID IP = {last_valid}
BROADCAST/LAST IP = {broadcast}

NOT NETWORK: (NOT {company_name}) = {not_net_ip} {not_net_mask}
'''


