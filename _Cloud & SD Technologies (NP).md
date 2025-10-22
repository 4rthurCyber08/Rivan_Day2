
SDWAN

vManage was introduced as the management plane, where all Day 0, Day 1, and Day N functions will be performed, including WAN Edge 
configuration, routing and control policies, troubleshooting, and monitoring. 

vSmart is the brain of the Cisco SD WAN fabric and is responsible for calculating and deploying all control and data policies as well as handling 
the distribution of encryption keys for data plane connectivity.

vBond makes up the orchestration plane and is responsible for authenticating components on the fabric in addition to distributing control and 
management plane information to the WAN Edges. The vBond is the component that aids in discovery of the fabric for all other components (such 
as when devices are behind NAT). The vBond then distributes the connectivity information for the vSmart and vManage to the WAN Edge.

vEdge handles the data plane is where user traffic will be routed and forwarded across the WAN. The data plane is similar to routers that would 
be deployed in a traditional WAN, though in Cisco SD WAN, these are referred to as WAN Edges. 

Each component authenticates each other and if successful, a Datagram Transport Layer Security (DTLS) tunnel is established. Separating the 
control plane from the data and management plane, the protocol that vSmart uses to communicate all the WAN Edge routing is called Overlay 
Management Protocol (OMP).



SDWAN

vManage was introduced as the management plane, where all Day 0, Day 1, and Day N functions will be performed, including WAN Edge 
configuration, routing and control policies, troubleshooting, and monitoring. 

vSmart is the brain of the Cisco SD WAN fabric and is responsible for calculating and deploying all control and data policies as well as handling 
the distribution of encryption keys for data plane connectivity.

vBond makes up the orchestration plane and is responsible for authenticating components on the fabric in addition to distributing control and 
management plane information to the WAN Edges. The vBond is the component that aids in discovery of the fabric for all other components (such 
as when devices are behind NAT). The vBond then distributes the connectivity information for the vSmart and vManage to the WAN Edge.

vEdge handles the data plane is where user traffic will be routed and forwarded across the WAN. The data plane is similar to routers that would 
be deployed in a traditional WAN, though in Cisco SD WAN, these are referred to as WAN Edges. 

Each component authenticates each other and if successful, a Datagram Transport Layer Security (DTLS) tunnel is established. Separating the 
control plane from the data and management plane, the protocol that vSmart uses to communicate all the WAN Edge routing is called Overlay 
Management Protocol (OMP).



<br>
<br>
<br>

1. Set a static route 
~~~
!@cmd
route add 10.69.255.13 mask 255.255.255.255 10.69.255.5
~~~

<br>

2. Access the vManage GUI, then push the vEdge list to the controllers
https://10.69.255.13:8443

<br>

`Configuration` > `Certificates` > `Send to Controllers`

<br>

---

<br>
<br>
<br>

## Configuration Feature Templates
Create an MOTD Banner Template 
Add Template > vEdge-Cloud

SYSTEM TEMPLATE
VE-System
> Baud Rate 9600

BANNER TEMPLATE
Login: WELCOME TO RIVAN SD-WAN
MOTD: NEXTGEN NETWORKING. DON'T BE LEFT BEHIND!!!!

VPN TEMPLATES
  VPN 0 - Named: Transport-VPN (INBAND)
  - IPv4 Route: Add a Default Route that is Device Specific
  
  VPN512 - Named: MGMT-VPN (OUT-OF-BAND)

  VPN-INTERFACE-ETHERNET
  - NO SHUT
  - G0/1
  - IPv4 Address: Device Specific
  - Tunnel: Global
    - Color: Biz-internet
	- Allow Services
	  - All
	  - NETCONF
	  - SSH
	- NAT: Global On

  VPN-INTERFACE-ETHERNET
  - NO SHUT
  - Eth0

BGP TEMPLATE
  BGP
  - NO SHUT
  - AS Number: 100
  - NEIGHBOR
    - Address: Device Specific
    - Remote AS: 1
	- Address Family: On
	- Address Family: IPv4 unicast
	- NO SHUT



DEVICE TEMPLATES
  Basic Info
    - VE-SYSTEM

  Transport & Management VPN
    - VPN 0
	- BGP 0
	- VPN Interface
	- VPN 512
	- VPN Interface
  Others
    - BANNER
	

Attach to devices
Per Device Configuration
- LUZON
Address(vpn_next_hop_ip_address_0)  : 192.168.50.1
IPv4 Address(vpn_if_ipv4_address)   : 192.168.20.1/30
Address(bgp_neighbor_address)       : 192.167.20.2
Hostname(system_host_name)          : EDGE-LUZON
System IP(system_system_ip)         : 10.1.21.1
Site ID(system_site_id)             : 21


- VISAYAS
Address(vpn_next_hop_ip_address_0)  : 192.168.50.1
IPv4 Address(vpn_if_ipv4_address)   : 192.168.20.5/30
Address(bgp_neighbor_address)       : 192.167.20.6
Hostname(system_host_name)          : EDGE-VISAYAS
System IP(system_system_ip)         : 10.1.25.1
Site ID(system_site_id)             : 25

- MINDANAO
Address(vpn_next_hop_ip_address_0)  : 192.168.50.1
IPv4 Address(vpn_if_ipv4_address)   : 192.168.20.9/30
Address(bgp_neighbor_address)       : 192.167.20.10
Hostname(system_host_name)          : EDGE-MINDANAO
System IP(system_system_ip)         : 10.1.29.1
Site ID(system_site_id)             : 29


Outline
- SD-Networking
- SDWAN
  - vManage
  - vBond
  - vSmart

- C8000 Edge
- NetConf
- Cisco DNA Center



- Nexus9K

- Meraki
- DNS Center




















Outline
- SD-Networking
- SDWAN
  - vManage
  - vBond
  - vSmart

- C8000 Edge
- NetConf
- Cisco DNA Center



- Nexus9K

- Meraki
- DNS Center
