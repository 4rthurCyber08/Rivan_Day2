import json
import random
import ipadd
import pprint
import rivan

class Computation:
    def __init__(self, companies, users, is_question=True):
        self.companies = companies
        self.users = users
        self.is_question = is_question
    
    def rand_company(self):
        total_values = len(self.companies)
        chosen_num = random.randint(1, total_values)
        chosen_name = self.companies[chosen_num - 1]

        return chosen_name

    def rand_user_groups(self):
        total_values = len(self.users)

        max_group = 3
        chosen_name = []

        while max_group > 0:
            chosen_num = random.randint(1, total_values)
            chosen_user = self.users[chosen_num - 1]

            if chosen_user in chosen_name:
                pass
            else:
                if max_group == 1:
                    chosen_name.append('and ' + chosen_user)
                else:
                    chosen_name.append(chosen_user)
                max_group -= 1

        return chosen_name
    
    def rand_net(self, if_subnets=False):
        # Pick a random private network address
        private_ranges = [
            ipadd.IPv4Network("10.0.0.0/8"),
            ipadd.IPv4Network("172.16.0.0/12"),
            ipadd.IPv4Network("192.168.0.0/16"),
        ]
        while True:
            try:
                while True:
                    try:
                        base = random.choice(private_ranges)
                        
                        # Pick a random _prefix length between /4 and /27
                        _prefix = random.randint(4, 27)

                        if base == ipadd.IPv4Network("10.0.0.0/8"):
                            # Pick a random _prefix length between /4 and /27
                            _prefix = random.randint(9, 27)

                        elif base == ipadd.IPv4Network("172.16.0.0/12"):
                            # Pick a random _prefix length between /12 and /27
                            _prefix = random.randint(17, 27)
                        
                        elif base == ipadd.IPv4Network("192.168.0.0/16"):
                            # Pick a random _prefix length between /16 and /27
                            _prefix = random.randint(25, 27)

                        subnets = list(base.subnets(new_prefix=_prefix))

                    except:
                        continue
                    else:
                        break

                ## NETWORK: Select a random subnet
                total_subnets = len(subnets)
                chosen_subnet = random.randint(1, total_subnets - 2)
                _network = subnets[chosen_subnet]
            
            except:
                continue
            else:
                break
        
        if if_subnets:
            return _prefix,_network

        ## NOT NETWORK: Determine the next network
        _next_network = subnets[chosen_subnet + 1]

        ## Get the increment
        _i = rivan.FromCIDR.get_inc(_prefix)

        ## Get valid range
        ## FIRST VALID IP
        _first_valid = _network[1]

        ## LAST VALID IP
        _last_valid = _network[-2]

        ## LAST IP/BROADCAST
        _broadcast = _network[-1]

        ## Get total HOSTS
        _hosts = len(list(_network)) - 2

        network_values = {
            'prefix': _prefix,
            'increment': _i,
            'hosts': _hosts,
            'network': _network,
            'first_valid': _first_valid,
            'last_valid': _last_valid,
            'broadcast': _broadcast,
            'next_network': _next_network
        }
        
        if self.is_question == True:
            if _hosts > 6000:
                _hosts = 6000
            elif _hosts <= 6:
                _hosts = 6

            _given_req_hosts = random.randint(3, _hosts)
            _given_reserved_ips = self.set_reserved_ips(_given_req_hosts)

            _given_values = {
                'network': _network,
                'req_hosts': _given_req_hosts,
                'reserved_ips': _given_reserved_ips
            }

            return _given_values

        return network_values
    
    def get_rand_devices(self):
        dhcp_server = [
            'D1', 'D2'
        ]
        
        dhcp_client = [
            'P1', 'P2'
        ]
        
        req_server = dhcp_server[random.randint(0, len(dhcp_server) - 1)]
        req_client = dhcp_client[random.randint(0, len(dhcp_client) - 1)]
        
        if req_client == 'P1': 
            switchport = 'e0/0'
        elif req_client == 'P2':
            switchport = 'e1/0'
        
        
        return req_server, req_client, switchport
        

    def set_reserved_ips(self, req_hosts):
        ip_res = int(0.2*req_hosts)
        
        if ip_res > 1_000:
            ip_res = 200

        elif ip_res > 200:
            ip_res = 100

        elif ip_res > 100:
            ip_res = 50

        elif ip_res > 50:
            ip_res = 10

        elif ip_res > 10:
            ip_res = 4

        else:
            ip_res = 2
        
        return (ip_res)
    
    def rand_vlan(self):
        set_vlan = random.randint(1, 200)
        
        return (set_vlan)
    
    # def rand_ip(self):
    #     random_int = random.randint(0, 2**32 - 1)
    #     random_ip = ipadd.IPv4Address(random_int)
        
    #     # Generate a random _prefix length.
    #     random__prefix = random.randint(1, 32)
        
    #     # Combine into a network object.
    #     random_network = ipadd.IPv4Network(f"{random_ip}/{random__prefix}", strict=False)
        
    #     return (random_network, random_ip)
    
    def get_network_values(self, original, prefix):
        orig_network = original.split('/')[0]
        orig_network_obj = ipadd.ip_network(f'{orig_network}{prefix}')
        
        network_obj = ipadd.ip_network(orig_network_obj.broadcast_address + 1)
        new_network = str(network_obj).split('/')[0]
        new_network_obj = ipadd.ip_network(f'{new_network}{prefix}')
        
        net_values = {
            'network': new_network_obj,
            'net_mask': new_network_obj.netmask,
            'first_valid': new_network_obj.network_address + 1,
            'last_valid': new_network_obj.broadcast_address - 1,
            'broadcast': new_network_obj.broadcast_address,
            'next_network': new_network_obj.broadcast_address + 1
        }
        
        return net_values
        

if __name__ == '__main__':
    ## Get Object Names
    with open('names.json') as file:
        name_store = json.load(file)

    company_list = name_store['Company_Names']
    user_list = name_store['User_Groups']

    ## Given Company
    company = Computation(company_list, user_list).rand_company()
    company_name = company + '.com'

    ## Given User Groups
    user_group = Computation(company_list, user_list).rand_user_groups()
    user_group = str(user_group).replace('\'', '')
    user_group = str(user_group).replace('[', '')
    user_group = str(user_group).replace(']', '')

    ## Given VLAN
    vlan = Computation(company_list, user_list).rand_vlan()

    ## Given IP Address Space
    req_values = Computation(company_list, user_list).rand_net()
    ip_space = str(req_values['network'])

    ## Given Required Hosts
    req_hosts = req_values['req_hosts']

    ## Given Required Reserved IPs
    req_reserved_ips = req_values['reserved_ips']

    req_devices = Computation(company_list, user_list).get_rand_devices()
    
    req_dhcp_server = req_devices[0]

    req_dhcp_client = req_devices[1]

    req_int = req_devices[2]

    ## Question
    question_basic = f'''
----------- QUESTION ------------

Design and implement a network for {company_name} with {req_hosts} {user_group}. 
- Use the available IP address space {ip_space}
- Reserve the first {req_reserved_ips} IP addresses of the network.
- Set the network for VLAN {vlan}.
- {req_dhcp_server} must be the DHCP server.
- {req_dhcp_client} must be the DHCP client.
'''

    ## Solution Template
    answer_temp = '''
----------- COMPUTE ------------

Convert: __ = __ bits
Subtract: /32 - __ = /__ = ( __Octet, __i )
Ipasok: Ipasok __i sa __ octet = __.__.__.__ /__

--

Network IP: (Company) = __.__.__.__  __.__.__.__
Valid Range:
- First Valid IP = __.__.__.__
- Last Valid IP = __.__.__.__
Broadcast/Last IP = __.__.__.__

NOT Network: (NOT Company) = __.__.__.__  __.__.__.__
'''

    question_portion = f'''
{question_basic} 
{answer_temp}
'''

    with open('_subnet_viaHosts.txt', 'w') as file:
        file.write(question_portion)


    ## Computation
    host_bits = rivan.GetCSI(req_hosts).convert_host_bits()
    constant = 32
    new_slash = f'/{str(constant - host_bits)}' 
    rivan_format = rivan.FromCIDR.to_rivan(constant - host_bits)
    octet = rivan_format[0].replace('\'', '')
    _i = rivan_format[1]
    _new_network = Computation(company_list, user_list).get_network_values(ip_space, new_slash)

    correct_answers = f'''
----------- ANSWER COMPUTATION------------

Convert: {req_hosts} = {host_bits} bits
Subtract: {constant} - {host_bits} = {new_slash} = ({octet}, {_i}i)
Ipasok: Ipasok {_i}i sa {octet} octet = {_new_network['network']}

--

Network IP: ({company_name}) = {str(_new_network['network']).split('/')[0]} {_new_network['net_mask']}
Valid Range:
- First Valid IP = {_new_network['first_valid']}
- Last Valid IP = {_new_network['last_valid']}
Broadcast/Last IP = {_new_network['broadcast']}

NOT Network: (NOT {company_name}) = {_new_network['next_network']} {_new_network['net_mask']}
'''

    if 'P1' in req_dhcp_client:
        accessw = 'A1'
    elif 'P2' in req_dhcp_client:
        accessw = 'A2'
        req_int = 'e1/0'

    ## Configuration
    configure_dhcp_server = f'''
!@{req_dhcp_server}
conf t
 vlan {vlan}
  name {company_name}
  exit
 interface vlan {vlan}
  ip address {_new_network['first_valid']} {_new_network['net_mask']}
  no shutdown
  exit
 ip dhcp pool {company_name}
  network {str(_new_network['network']).split('/')[0]} {_new_network['net_mask']}
  default-router {_new_network['first_valid']}
  domain-name {company_name}
  end
'''

    configure_dhcp_access = f'''
!@{accessw}
conf t
 int {req_int}
  switchport mode access
  switchport access vlan {vlan}
  end
'''

    configure_dhcp_client = f'''
!@{req_dhcp_client}
conf t
 int {req_int}
  no shutdown
  ip add dhcp
  end
'''
        
    answer_portion = f'''
{correct_answers}

----------- ANSWER CONFIGURATIONS ------------
{configure_dhcp_server}
{configure_dhcp_access}
{configure_dhcp_client}
'''

    with open('_subnet_viaHosts(answers).txt', 'w') as file:
        file.write(answer_portion)
    
    
    ################### SUBNET
    
    given_values =  Computation(company_list, user_list).rand_net(if_subnets=True)
    avail_network = given_values[1]
    net_cidr = str(avail_network)[-2::]
    total_subnets = 2**(32 - int(net_cidr))
    
    if total_subnets <= 4:
        total_subnets = 4
    elif total_subnets >= 8192:
        total_subnets = 8000
    
    req_range = int(int(total_subnets)*0.2)
    if req_range <= 2:
        req_range = 4
        
    req_subnets = random.randint(2, req_range)
    
    ## Question
    question_basic = f'''
----------- QUESTION ------------

1. Design {req_subnets} offices for {company_name} using the available network address {avail_network}. 
Maximize the number of IP addresses.
- For the 2nd office, 
    assign the first valid IP on R4's e0/1 interface.
    assign the last valid IP on P1's e0/1 interface.

- For the 3rd office,
    assign the first valid IP on R3's e0/1 interface.
    assign the last valid IP on P2's e0/1 interface. 

- For the 4th office,
    assign the first valid IP on R2's e0/1 interface.
    assign the last valid IP on S1's e0/1 interface. 

- For the 5th office,
    assign the first valid IP on R1's e0/1 interface.
    assign the last valid IP on S2's e0/1 interface. 
'''

    with open('_subnet_viaSubnet.txt', 'w') as file:
        file.write(question_basic)

    # Computation
    subnet_bits = rivan.GetCAI(req_subnets).convert_subnet_bits()
    new_slash = f'/{str(int(net_cidr) + subnet_bits)}' 
    rivan_format = rivan.FromCIDR.to_rivan(int(net_cidr) + subnet_bits)
    octet = rivan_format[0].replace('\'', '')
    _i = rivan_format[1]
    
    _new_network = Computation(company_list, user_list).get_network_values(str(avail_network), new_slash)
    
    _1st_network = ipadd.IPv4Network(str(avail_network)[0:-3] + new_slash) 
    _2nd_network = _new_network['network']
    _3rd_network = ipadd.IPv4Network(str(_2nd_network[-1] + 1) + new_slash)
    _4th_network = ipadd.IPv4Network(str(_3rd_network[-1] + 1) + new_slash)
    _5th_network = ipadd.IPv4Network(str(_4th_network[-1] + 1) + new_slash)
    
    correct_answers_subnet = f'''
----------- ANSWER COMPUTATION------------

Convert: {req_subnets} = {subnet_bits} bits
Add: {net_cidr} + {subnet_bits} = {new_slash} = ({octet}, {_i}i)
Ipasok: Ipasok {_i}i sa {octet} octet:

1st Office = {_1st_network}
2nd Office = {_2nd_network}
3rd Office = {_3rd_network}
4th Office = {_4th_network}
5th Office = {_5th_network}

---

2nd Office:
  NETWORK = {_2nd_network[0]} {_new_network['net_mask']}
  VALID RANGE:
  - FIRST VALID IP = {_2nd_network[1]}
  - LAST VALID IP = {_2nd_network[-2]}
  BROADCAST/LAST IP = {_2nd_network[-1]}

  NOT NETWORK: (NOT 2nd Office) = {_2nd_network[-1] + 1} {_new_network['net_mask']}

3rd Office:
  NETWORK = {_3rd_network[0]} {_new_network['net_mask']}
  VALID RANGE:
  - FIRST VALID IP = {_3rd_network[1]}
  - LAST VALID IP = {_3rd_network[-2]}
  BROADCAST/LAST IP = {_3rd_network[-1]}

  NOT NETWORK: (NOT 3rd Office) = {_3rd_network[-1] + 1} {_new_network['net_mask']}

4th Office:
  NETWORK = {_4th_network[0]} {_new_network['net_mask']}
  VALID RANGE:
  - FIRST VALID IP = {_4th_network[1]}
  - LAST VALID IP = {_4th_network[-2]}
  BROADCAST/LAST IP = {_4th_network[-1]}

  NOT NETWORK: (NOT 4th Office) = {_4th_network[-1] + 1} {_new_network['net_mask']}

5th Office:
  NETWORK = {_5th_network[0]} {_new_network['net_mask']}
  VALID RANGE:
  - FIRST VALID IP = {_5th_network[1]}
  - LAST VALID IP = {_5th_network[-2]}
  BROADCAST/LAST IP = {_5th_network[-1]}

  NOT NETWORK: (NOT 5th Office) = {_5th_network[-1] + 1} {_new_network['net_mask']}
'''
    
    ## Configuration
    configure_offices = f'''
2nd Office:

!@R4
conf t
 int e0/1
  ip add {_2nd_network[1]} {_new_network['net_mask']}
  no shut
  end

!@P1
conf t
 int e0/1
  ip add {_2nd_network[-2]} {_new_network['net_mask']}
  no shut
  end

--

3rd Office:

!@R3
conf t
 int e0/1
  ip add {_3rd_network[1]} {_new_network['net_mask']}
  no shut
  end

!@P2
conf t
 int e0/1
  ip add {_3rd_network[-2]} {_new_network['net_mask']}
  no shut
  end

--

4th Office:

!@R2
conf t
 int e0/1
  ip add {_4th_network[1]} {_new_network['net_mask']}
  no shut
  end

!@S1
conf t
 int e0/1
  ip add {_4th_network[-2]} {_new_network['net_mask']}
  no shut
  end

--

5th Office:

!@R1
conf t
 int e0/1
  ip add {_5th_network[1]} {_new_network['net_mask']}
  no shut
  end

!@S2
conf t
 int e0/1
  ip add {_5th_network[-2]} {_new_network['net_mask']}
  no shut
  end
    
'''

    answer_portion = f'''
{correct_answers_subnet}

----------- ANSWER CONFIGURATIONS ------------
{configure_offices}
'''

    with open('_subnet_viaSubnet(answers).txt', 'w') as file:
        file.write(answer_portion)