
<!-- Your monitor number = #$34T# -->


## ⛅ Warm Up for Day 2.
*"Repetition is the mother of all skills"*

<br>

### 🔧 Configure the following:
  - Switch (__CoreTAAS__ & __CoreBABA__)
  - Voice Gateway/Call Manager (__CUCM - Cisco Unified Call Manager__)
  - Router (__EDGE__)

<br>

Verify:

~~~cmd
@cmd
ping 10.#$34T#.1.10             PC Network Adapter
ping 10.#$34T#.1.2		    CoreTAAS
ping 10.#$34T#.1.4		    CoreBABA
ping 10.#$34T#.100.8		CUCM
ping 10.#$34T#.#$34T#.1		EDGE - INSIDE
ping 200.0.0.#$34T#		    EDGE - OUTSIDE

ping 200.0.0.k		        Klassmate's EDGE	       k = klassmate's Monitor Number
ping 10.k.100.8		        Klassmate's CUCM
ping 10.k.1.4		        Klassmate's CoreBABA
ping 10.k.1.2		        Klassmate's CoreTAAS
ping 10.k.1.10		        Klassmate's PC
~~~

Your Branch must be able to call other klassmates  

<br>

View your cameras:
  - http://10.#$34T#.50.6
  - http://10.#$34T#.50.8

&nbsp;
---
&nbsp;

### 🌐 Configure DNS
  - Create __DNS zones & records__ for daytwo#$34T#.com  
  - Create a __website__ for daytwo#$34T#.com  
  - Create an __email__ for

| Email                       | Name           |
| ---                         | ---            |
| support@daytwo#$34T#.com    | Rivan Support  |
| user1@daytwo#$34T#.com      | User1          |

<br>

Send an email from support@daytwo#$34T#.com to user1@daytwo#$34T#.com

<br>
<br>

---
&nbsp;

## 🎯 Review

### 1. A Cisco IP phone receives untagged data traffic from an attached PC. Which action is taken by the phone?
  - [ ] __A.__ It drops the traffic.
  - [ ] __B.__ It allows the traffic to pass through unchanged.
  - [ ] __C.__ It tags the traffic with the native VLAN.
  - [ ] __D.__ It tags the traffic with the default VLAN

&nbsp;
---
&nbsp;

### 2. Which command can you enter to determine the addresses that have been assigned on a DHCP Server?
  - [ ] __A.__ Show ip DHCP database.
  - [ ] __B.__ Show ip DHCP pool.
  - [ ] __C.__ Show ip DHCP binding.
  - [ ] __D.__ Show ip DHCP server statistic.

&nbsp;
---
&nbsp;

### 3. Which two VLAN IDs indicate a default VLAN? (Choose two.)
  - [ ] __A.__ 0
  - [ ] __B.__ 1
  - [ ] __C.__ 1005
  - [ ] __D.__ 1006
  - [ ] __E.__ 4096

&nbsp;
---
&nbsp;

### 4. Which command prevents passwords from being stored in the configuration as plain text on a router or switch?
  - [ ] __A.__ enable secret
  - [ ] __B.__ enable password
  - [ ] __C.__ service password-encryption
  - [ ] __D.__ username cisco password encrypt

&nbsp;
---
&nbsp;

### 5. What is the primary function of a Layer 3 device?
  - [ ] __A.__ to transmit wireless traffic between hosts.
  - [ ] __B.__ to analyze traffic and drop unauthorized traffic from the Internet.
  - [ ] __C.__ to forward traffic within the same broadcast domain.
  - [ ] __D.__ to pass traffic between different networks.

&nbsp;
---
&nbsp;

### 6. Which option about JSON is true
  - [ ] __A.__ uses predefined tags or angle brackets () to delimit markup text
  - [ ] __B.__ used to describe structured data that includes arrays
  - [ ] __C.__ used for storing information
  - [ ] __D.__ similar to HTML, it is more verbose than XML

&nbsp;
---
&nbsp;

### 7. Which output displays a JSON data representation?
Which of the following is the JSON encoding of a dictionary or hash?
  - [ ] __A.__ {“key”: “value”}
  - [ ] __B.__ [“key”, “value”]
  - [ ] __C.__ {“key”, “value”}
  - [ ] __D.__ (“key”: “value”)

&nbsp;
---
&nbsp;

### 8. What are two functions of a Layer 2 switch? (Choose two.)
  - [ ] __A.__ acts as a central point for association and authentication servers.
  - [ ] __B.__ selects the best route between networks on a WAN.
  - [ ] __C.__ moves packets within a VLAN.
  - [ ] __D.__ moves packets between different VLANs.
  - [ ] __E.__ makes forwarding decisions based on the MAC address of a packet.

&nbsp;
---
&nbsp;

### 9. Using direct sequence spread spectrum, which three 2.4-GHz channels are used to limit collisions?
  - [ ] __A.__ 5, 6, 7
  - [ ] __B.__ 1, 2, 3
  - [ ] __C.__ 1, 6, 11
  - [ ] __D.__ 1, 5, 10

&nbsp;
---
&nbsp;

### 10. When should an engineer implement a collapsed-core architecture?
  - [ ] __A.__ Only when using VSS technology
  - [ ] __B.__ For small networks with minimal need for growth
  - [ ] __C.__ For large networks that are connected to multiple remote sites
  - [ ] __D.__ The access and distribution layers must be on the same device

<br>
<br>

---
&nbsp;

# 💻 Network Fundamentals

<br>

### 🔢 Counting as a network engineer.

|     | Decimal | IPv4          | IPv6   |
| --- | ---     | ---           | ---    |
| -1  | 1999    | 1.255.255.255 | :1fff: |
|     | 2000    | 2.0.0.0       | :2000: |
| +1  | 2001    | 2.0.0.1       | :2001: |
|     |         |               |        |
| -1  |         |               |        |
|     | 2999    | 2.255.255.255 | :2fff: |
| +1  |         |               |        |
|     |         |               |        |
| -1  |         |               |        |
|     | 4099    | 4.0.255.255   | :40ff: |
| +1  |         |               |        |
|     |         |               |        |
| -1  |         |               |        |
|     | 6790    | 6.7.255.0     | :67f0: |
| +1  |         |               |        |
|     |         |               |        |
| -1  |         |               |        |
|     | 5389    | 5.3.8.255     | :538f: |
| +1  |         |               |        |
|     |         |               |        |

&nbsp;
---
&nbsp;

### Internet Protocol Version 4 (IPv4)
*What is the IP address of your phone?*
  - ipchicken.com
  - ipconfig

<br>

### Public IP address
| Class | IP Range                    |
| ---   | ---                         |
| A     | 1.0.0.0 - 126.255.255.255   |
| B     | 128.0.0.0 - 191.255.0.0     |
| C     | 192.0.0.0 - 223.255.255.0   |
| D     | 224.0.0.0 - 239.255.255.255 |
| E     | 240.0.0.0 - 255.255.255.255 |

<br>

~~~cmd
@cmd
ping 8.8.8.8
ping 1.1.1.1
ping 4.4.1.1

tracert 8.8.8.8
~~~

<br>
<br>

<details>
<summary>Traceroute Output</summary>
	
~~~cmd
Tracing route to dns.google [8.8.8.8]
over a maximum of 30 hops:

  1    20 ms     1 ms     1 ms  10.28.0.1
  2     2 ms     1 ms     1 ms  192.168.100.1
  3    10 ms    10 ms     8 ms  10.56.0.1
  4     *        9 ms     *     161.49.4.128.convergeict.com [161.49.4.128]
  5     6 ms     4 ms     4 ms  161.49.4.240.convergeict.com [161.49.4.240]
  6     *        *        *     Request timed out.
  7     4 ms     5 ms     5 ms  161.49.6.147.convergeict.com [161.49.6.147]
  8     5 ms     5 ms     4 ms  142.250.174.148
  9     9 ms     5 ms     5 ms  142.251.251.137
 10     5 ms     5 ms     6 ms  142.251.246.167
 11     5 ms     9 ms     4 ms  dns.google [8.8.8.8]
~~~

</details>

&nbsp;
---
&nbsp;

### Private IP address  
*Why do big companies uses the IP addresses that starts with 10.x.x.x ? *

<br>

| Class | IP Range                        | No. of Host |
| ---   | ---                             | ---         |
| A     | 10.0.0.0 - 10.255.255.255       | 16,777,214  |
| B     | 172.16.0.0 - 172.31.255.255     | 64,534      |
| C     | 192.168.0.0 - 192.168.255.255   | 254         |

<br>
<br>
<br>
<br>

---
&nbsp;

## 🙌 CIDR (Rivan Finger Method)
*How do devices see IP addresses? *
	
### `0 0 0 0   0 0 0 0   .   0 0 0 0   0 0 0 0   .   0 0 0 0   0 0 0 0   .   0 0 0 0   0 0 0 0`

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>




<br>
<br>

__Example 01:__
<details>
<summary>192.168.20.1 /24</summary>
	
### `1 1 0 0   0 0 0 0   .   1 0 1 0   1 0 0 0   .   0 0 0 1   0 1 0 0   .   0 0 0 0   0 0 0 1`

### `1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   0 0 0 0   0 0 0 0`

<br>
<br>
<br>

### `1 1 0 0   0 0 0 0   .   1 0 1 0   1 0 0 0   .   0 0 0 1   0 1 0 0   .   1 1 1 1   1 1 1 1`

</details>

<br>

__Example 02:__
<details>
<summary>172.16.40.1 /21</summary>
	
### `1 0 1 0   1 1 0 0   .   0 0 0 1   0 0 0 0   .   0 0 1 0   1 0 0 0   .   0 0 0 0   0 0 0 1`

### `1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 1 1   1 0 0 0   .   0 0 0 0   0 0 0 0`

<br>
<br>
<br>

### `1 0 1 0   1 1 0 0   .   0 0 0 1   0 0 0 0   .   0 0 1 0   1 1 1 1   .   1 1 1 1   1 1 1 1`

</details>

<br>

__Example 03:__
<details>
<summary>10.100.22.205 /30</summary>
	
### `0 0 0 0   1 0 1 0   .   0 1 1 0   0 1 0 0   .   0 0 0 1   0 1 1 0   .   1 1 0 0   1 1 0 1`

### `1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 1 1   .   1 1 1 1   1 1 0 0`

<br>
<br>
<br>

### `0 0 0 0   1 0 1 0   .   0 1 1 0   0 1 0 0   .   0 0 0 1   0 1 1 0   .   1 1 0 0   1 1 1 1`

</details>

&nbsp;
---
&nbsp;

| Binary             | Decimal|
| ---                | ---    |
| `0 0 0 0  0 0 0 0` | = 0    |
| `0 0 0 0  0 0 0 1` | = 1    |
| `0 0 0 0  0 0 1 0` | = 2    |
| `0 0 0 0  0 0 1 1` | = 3    |
| `0 0 0 0  0 1 0 0` | = 4    |
| `0 0 0 0  0 1 0 1` | = 5    |
| `0 0 0 0  0 1 1 0` | = 6    |
| `0 0 0 0  0 1 1 1` | = 7    |
| `0 0 0 0  1 0 0 0` | = 8    |
| `0 0 0 0  1 0 0 1` | = 9    |
| `0 0 0 0  1 0 1 0` | = 10   |
| `0 0 0 0  1 0 1 1` | = 11   |
| `0 0 0 0  1 1 0 0` | = 12   |
| `0 0 0 0  1 1 0 1` | = 13   |
| `0 0 0 0  1 1 1 0` | = 14   |
| `0 0 0 0  1 1 1 1` | = 15   |
|                    |        |
| `0 0 0 1  0 0 0 0` | = 16   |

<br>
<br>

---
&nbsp;

### 🎯 Exercise 01: Convert CIDR to various formats

<br>

| CIDR | NETMASK     | RIVAN Format | WILDCARD    |
| ---  | ---         | ---          | ---         |
| /20  |             | (Octet, i)   |             |
| /27  |             | (Octet, i)   |             |
| /14  |             | (Octet, i)   |             |

<br>
<br>

---
&nbsp;

## 0️⃣ Bit Length





&nbsp;
---
&nbsp;

  
### 🎯 Exercise 02: Find the Bit Length

<br>

| Value     | Bits |
| ---       | ---  |
| 195       |      |
| 13        |      |
| 1,750     |      |
| 1,855     |      |
| 2,700     |      |
| 2         |      |
| 376       |      |
| 888       |      |
| 8         |      |
| 212       |      |
| 4,500     |      |
| 81        |      |
| 20,000    |      |
| 55        |      |
| your age  |      |

<br>
<br>

---
&nbsp;


##  Subnetting (Host)

### 🎯 Exercise 03: Design a network for `accenture.com` with 1750 agents, team leads, project managers, and quality assurance teams. Use the 10.0.0.0/8 IP address space.
- [ ] 10.16.0.0/24
- [ ] 10.0.4.0/22
- [ ] 10.0.8.0/21
- [ ] 10.0.32.0/20

<br>
<br>

### CSI Method  
__CONVERT__  
  1750 = 11 bits

<br>

__SUBTRACT__  
  /32 - 11 bits = /21

<br>

<details>
<summary>Why /32? </summary>

### `0 0 0 0  0 0 0 0  .  0 0 0 0  0 0 0 0  .  0 0 0 0  0 0 0 0  .  0 0 0 0  0 0 0 0`
### `                                                     0 0 0     0 0 0 0  0 0 0 0`
### `_______________________________________________________________________________`
### `0 0 0 0  0 0 0 0  .  0 0 0 0  0 0 0 0  .  0 0 0 0  0                           `

</details>

<br>
	
__INSERT (*IPASOK*)__  
/21 (Octet, i)

<br>

Insert 8 inside the 3rd octet of the given IP address space, 10.0.0.0  

<br>

> __10.0.8.0 /21__

<br>

<details>
<summary>IP Values</summary>
	
|                               |                        |
| ---                           | ---                    |
| Network IP                    | 10.0.8.0 255.255.248.0 |
| First Valid (Network +1)      | 10.0.8.1               |
| Last Valid (Broadcast -1)     | 10.0.15.254            |
| Broadcast (Next Network -1)   | 10.0.15.255            |
|                               |                        |
| Next Network (Insert i again) | 10.0.16.0              |

</details>

<br>
<br>

---
&nbsp;

### 🎯 Exercise 04: Design a network for `concentrix.com` with 160 admin, 250 managers, 112 executive, 100 security agents. Use the 172.16.0.0/16 IP address space.
- [ ] 172.16.8.0 /22
- [ ] 172.16.16.0 /23
- [ ] 172.16.4.0 /22
- [ ] 172.16.2.0 /23

<br>

CIA Method
- CONVERT:	
- SUBTRACT:
- INSERT(Ipasok):

<br>

|                               |                        |
| ---                           | ---                    |
| Network IP                    |                        |
| First Valid (Network +1)      |                        |
| Last Valid (Broadcast -1)     |                        |
| Broadcast (Next Network -1)   |                        |
|                               |                        |
| Next Network (Insert i again) |                        |

<br>
<br>

---
&nbsp;

### 🎯 Exercise 05: Design and implement a network for `foundever.com` with 45 users. Use the 192.168.0.0/24 IP address space
CIA Method
- CONVERT:	
- SUBTRACT:
- INSERT(Ipasok):

<br>

|                               |                        |
| ---                           | ---                    |
| Network IP                    |                        |
| First Valid (Network +1)      |                        |
| Last Valid (Broadcast -1)     |                        |
| Broadcast (Next Network -1)   |                        |
|                               |                        |
| Next Network (Insert i again) |                        |

<br>
<br>

__IMPLEMENTATION__

~~~
config t
 vlan 25
  name _____.com
  exit
 int vlan 25
  ip add __.__.__.__  __.__.__.__
  ip ospf 1 area 0
  no shut
  exit
 ip dhcp excluded-add __.__.__.__  __.__.__.__
 ip dhcp pool _____.com
  network __.__.__.__  __.__.__.__
  default-router __.__.__.__
  domain-name _____.com
  dns-server 10.#$34T#.1.10
  option 150 ip 10.#$34T#.100.8
 int fa 0/5
  switchport voice vlan 25
  shut
  no shut
  end
show ip dhcp binding
~~~

<br>
<br>

---
&nbsp;


### 🎯 Exercise 06: Design and implement networks.
![DHCP](img/DHCP.png)

<br>

P1
- IP address: 10.35.0.0/16
- Domain Name: BSP.COM
- Number of Users: 812
- Reserved IPs: First 70 IPs
- Assign to VLAN: 35

<br>

P1
- IP address: 172.16.64.0/18
- Domain Name: ACCENTURE.COM
- Number of Users: 87
- Reserved IPs: First 10 IPs
- Assign to VLAN: 40

<br>

S1
- IP address: 192.168.52.0/24
- Domain Name: TELETECH.NET
- Number of Users: 345
- Reserved IPs: First 100 IPs
- Assign to VLAN: 52
	
<br>

S2
- IP address: 10.67.48.0/20
- Domain Name: FOUNDEVER.COM
- Number of Users: 1456
- Reserved IPs: First 100 IPs
- Assign to VLAN: 67

<br>
<br>

---
&nbsp;

## Subnetting (Subnet)

![BitLength](img/BitLength.png)

&nbsp;
---
&nbsp;

![RANGE](img/Range.png)

<br>
<br>

---
&nbsp;

### 🎯 Exercise 07: Subnet for 8 offices using the Network address 192.168.128.0/27  Maximize the number of IP addresses.

<br>

### CAI Method  
__CONVERT *(Bit Value. NOT Length)*__  
  8 = 3 bits  

<br>

__ADD__  
  /27 + 3 bits = /30 (4th, 4i)  

<br>

__INSERT(*IPASOK*)__  
  1st Office: 192.168.128.0 /30  
  2nd Office: 192.168.128.4 /30  
  3rd Office: 192.168.128.8 /30  
  4th Office: 192.168.128.12 /30  
  5th Office: 192.168.128.16 /30  
  6th Office: 192.168.128.20 /30  
  7th Office: 192.168.128.24 /30  
  8th Office: 192.168.128.28 /30  

<br>

From the NETWORK: 192.168.128.0 /27 (4th, 32i)  
Valid Range:  
- FIRST VALID: 192.168.128.1 /27  
- LAST VALID: 192.168.128.30   
- LAST IP/BROADCAST: 192.168.128.31  

<br>
NEXT NETWORK: 192.168.128.32 /27  

<br>
<br>

---
&nbsp;

### 🎯 Exercise 08: Subnet for 16 offices using the Network address 172.16.224.0/19. Maximize the number of IP addresses.

CAI Method
- CONVERT:	
- ADD:
- INSERT(Ipasok):

<br>

Offices:
1. &nbsp;
2. &nbsp;
3. &nbsp;
4. &nbsp;
5. &nbsp;
6. &nbsp;
7. &nbsp;
8. &nbsp;
9. &nbsp;
10. &nbsp;
11. &nbsp;
12. &nbsp;
13. &nbsp;
14. &nbsp;
15. &nbsp;
16. &nbsp;
17. &nbsp;
18. &nbsp;
19. &nbsp;
20. &nbsp;

<br>
<br>

---
&nbsp;

### 🎯 Exercise 09: Design and Implement 4 offices using the Network address 172.16.224.0/19. Maximize the number of IP addresses.

CAI Method
- CONVERT:	
- ADD:
- INSERT(Ipasok):

<br>

Offices:
1. &nbsp;
2. &nbsp;
3. &nbsp;
4. &nbsp;

&nbsp;
---
&nbsp;

![ValidRangeRST](img/ValidRange.png)
























