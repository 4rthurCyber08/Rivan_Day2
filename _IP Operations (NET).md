
<!-- Your monitor number = #$34T# -->


## ⛅ Warm Up for Day 2.

Access the ff via SecureCRT:
- 10.#$34T#.1.2       CoreTAAS
- 10.#$34T#.1.4       CoreBABA
- 10.#$34T#.100.8     CUCM
- 10.#$34T#.#$34T#.1  EDGE

<br>

Verify Connectivity:

~~~cmd
@cmd
ping 10.#$34T#.1.10         PC Network Adapter
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


<br>
<br>

---
&nbsp;


### REVIEW

~~~
!@CoreBABA
conf t
 monitor session 1 source interface fa0/3,fa0/5,fa0/7
 monitor session 1 destination interface fa0/1,fa0/9
 end
~~~


<br>
<br>

---
&nbsp;


## CIA

### Confidentiality, Integrity, Availability
*How to access port 445 because you don't have a Firewall!*
~~~
!@cmd
net use \\10.3.3.x\ipc$ /user:administrator C1sc0123
net use x: /delete
net use x: \\10.3.3.x\c$
~~~

<br>

__Unsecure vs Secured__
| User  | Pass    |
| ---   | ---     |
| admin | secr3t  |
| user1 | pass123 |
| admin | pass    |

<br>

~~~
!@CoreTAAS
conf t
 username admin privilege 15 secret pass
 username _____ privilege 15 secret pass
 !
 ip domain name sec.com
 crypto key generate rsa
 2048
 ip ssh version 2
 !
 line vty 0 14
  transport input all
  login local
  exec-timeout 0 0
  end
~~~

<br>


__Parser View__
~~~
!@CoreTAAS
conf t
 aaa new-model
 aaa authentication login default local
 aaa authorization exec default local
 line vty 0 14
  transport input all
  login authentication default
 !
 parser view T1
  secret pass
  commands exec include configure terminal
  commands exec include show ip interface brief
  commands exec include show interface *
  commands configure include interface
  commands configure include interface GigabitEthernet0/1 
  commands interface include shutdown
  commands interface include no shutdown
  exit
 username tier1 view T1 secret pass
 username tier2 privilege 15 secret pass
 end
~~~


<br>
<br>

---
&nbsp;


### ✉️ Integrity

1. Code Signing  

2. Cryptographic Checksum
   
3. Merkle Trees / Content-Addressed Storage


<br>
<br>

---
&nbsp;


### 🔀 Availability
*Avoid a single point of failure*

<br>

Expensive Switches have __Loop Avoidance__  

Execute a persistent ping
~~~
!@cmd
ping 10.#$34T#.1.2 -t
~~~


__Trunking__
~~~
!@CoreBABA, CoreTAAS
conf t
 int range fa0/10-12
  switchport trunk encapsulation dot1q
  switchport mode trunk
  switchport trunk allowed vlan all
  switchport trunk native vlan
  end
show int trunk
~~~


__Etherchannel__
~~~
!@CoreBABA, CoreTAAS
conf t
 int range fa0/10-12
  channel-group 1 mode active
  channel-protocol lacp
  end
show int po1 | inc BW
~~~


<br>
<br>

---
&nbsp;


### NIC TEAMING

Windows Server 2022:
  Name: WIN-NETPLUS-M
  
  | NetAdapter        | Connection          | IP Address        |
  | ---               | ---                 | ---               |
  | Network Adapter 1 | NAT                 | 208.8.8.8     /24 |
  | Network Adapter 2 | VMNet 2             | 192.168.102.8 /24 |
  | Network Adapter 3 | VMNet 3             | 192.168.103.8 /24 |
  | Network Adapter 4 | VMNet 3             |                   |
  | Network Adapter 5 | VMNet 3             |                   |
  | Network Adapter 6 | Bridged (Replicate) | 10.#$34T#.1.8 /24 |


<br>
<br>

---
&nbsp;


## Domain Name System

| Name | Domain Name   | IP                 |
| ---  | ---           | ---                |
| ns1  | net#$34T#.com | 10.#$34T#.1.8      |
| www  |               | 10.#$34T#.1.8      |
|      |               | 10.#$34T#.1.8      |
| ct   |               | 10.#$34T#.1.2      |
| cb   |               | 10.#$34T#.1.4      |
| cm   |               | 10.#$34T#.100.8    |
| ed   |               | 10.#$34T#.#$34T#.1 |
| cam6 |               | 10.#$34T#.50.6     |
| cam8 |               | 10.#$34T#.50.8     |


~~~
!@cmd
ping www.net#$34T#.com

ping smtp.net#$34T#.com
~~~


&nbsp;
---
&nbsp;


### DNS Hierarchy
1. ROOT
2. TLD
3. SLD
4. RECORDS


<br>
<br>

---
&nbsp;


## Web Server
__Configure Web Server (net#$34T#.com)__  

<br>

__Access__
http://www.net#$34T#.com/


<br>
<br>

---
&nbsp;


### 🔴 Phishing Websites
Configure DNS for  `bclo.com`

| Record | Mapping   |
| ---    | ---       |
|        | 208.8.8.8 |
| ns     | 208.8.8.8 |
| www    | 208.8.8.8 |


<br>
<br>


1. Internet Information Services Manager
2. Create an `http` mapping for the bdo web files to the domain `www.bclo.com`

<br>

__Access__
http://www.bclo.com/


<br>
<br>

---
&nbsp;


### 🎯 Exercise: Create another phishing website for bpi.com.ph

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
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


## Secure Web (HTTPS)

### CA Hierarchy
1. ROOT CA   (Self-signed)
2. SUB CA
3. LEAF CA


<br>
<br>

~~~
!@cmd
ping -4 www.rivanit.com
~~~


<br>
<br>

---
&nbsp; 


### SSL Certificate

Subject : Distinguished Names  
  - Defined ITU-T (International Telecommunication Union Telecommunication   Standardization Sector) X.500 Series  
  - X.501 - Defines the directory model and Distinguished Names.  
  - X.520 - Defines the standard attribute types used in DNs  


<br>
<br>

---
&nbsp; 


### Wildcard Certificate  
Configure DNS for  `net#$34T#.com`

| Record | Mapping           |
| ---    | ---               |
| www    | 208.8.8.8         |
| web    | www.net#$34T#.com |
| site   | www.net#$34T#.com |


&nbsp;
---
&nbsp;


### 🎯 Exercise: Create a ROOT, INTERMEDIATE, LEAF Certificate for https://www.bclo.com

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
<br>

---
&nbsp;


## Enterprise Email Server
- HMail Server
- Thunderbird

<br>

__Create Accounts For `net#$34T#.com`__
1. Support
2. Admin
3. User

<br>

Setup __DNS Secondary Zones__ & __Conditional Forwarders__
~~~
!@cmd
route add 10.0.0.0 mask 255.0.0.0 10.#$34T#.1.4 -p
route add 200.0.0.0 mask 255.255.255.0 10.#$34T#.1.4 -p
~~~


<br>
<br>

---
&nbsp;


## Security Awareness
Phishing Simulation Emails 

__Admin__ > __Users__  

<br>

~~~
Example:
Subject: Action Required: Password Expires Today
Text: Click here to update your password.
~~~


&nbsp;
---
&nbsp;


### NOC / Network Operations Center
~~~
Subject: URGENT: Core Router Configuration Validation Required

Content:
Hello,

The Network Operations team has identified a configuration mismatch 
affecting several production network devices.

A validation task has been assigned to your account.

Please review the updated configuration checklist:

[Review Network Configuration]

Failure to complete validation before the maintenance window may impact
network availability.

Regards,

Network Operations Center
~~~

&nbsp;
---
&nbsp;


### SOC / Security Operations Center
~~~
Subject: HIGH PRIORITY: SIEM Alert Requires Analyst Review

Content:
A critical security event has been generated.

Alert ID:
SOC-2026-0815-7742

Event Type:
Suspicious Authentication Activity

Severity:
High

Please access the incident dashboard and confirm whether this activity
requires escalation.

[Open Incident Dashboard]

Security Operations Team
~~~


&nbsp;
---
&nbsp;


### Finance Department
~~~
Subject: Payment Approval Required: Outstanding Vendor Invoice

Content:
Dear Finance Team,

A vendor invoice requires review and approval before the payment deadline.

Vendor:
ABC Technology Solutions

Invoice Number:
INV-2026-88391

Amount:
$18,750.00

Please review the invoice documentation:

[View Invoice]

If this request appears unusual, please verify through the approved
vendor communication channel.

Accounts Payable
~~~


&nbsp;
---
&nbsp;


### Human Resources (HR)
~~~
Subject: Updated Employee Benefits Policy Requires Review

Content:
Hello,

The annual employee benefits policy has been updated.

All employees must review the updated document before the enrollment
period closes.

Please access the updated policy here:

[Review Benefits Document]

HR Department
~~~


&nbsp;
---
&nbsp;


### System Administrators
~~~
Subject: Administrator Account Password Expiration Notice

Content:
Your privileged administrator account password will expire soon.

To avoid interruption of administrative access, please validate your
account information.

[Validate Administrator Account]

IT Infrastructure Team
~~~


&nbsp;
---
&nbsp;


### General Employees
~~~
Subject: Action Required: Microsoft 365 Account Verification

Content:
Your Microsoft 365 account requires verification due to a recent security
update.

Please complete verification:

[Verify Account]

Failure to complete verification may result in temporary account
restrictions.

IT Service Desk
~~~


<br>
<br>

---
&nbsp;


## Identity Access Management
Install `Active Directory Domain Services`

<br>

| OU  | Local Domain | Global Group | Users |
| --- | ---          | ---          | ---   |
| NOC | LGNOC        | GGNOC        | ac    |
| SOC | LGSOC        | GGSOC        | kc    |
| FIN | LGFIN        | GGFIN        | zc    |

~~~
!@cmd
gpupdate /force
~~~

<br>

NAS - Network Attatched Storage (File Access) 
SAN - Storage Area Network (Storage Access)


<br>
<br>

---
&nbsp;


## AAA - RADIUS (Wired & Wireless)
> [!IMPORTANT]
> Configure WinServer 2022 for a RADIUS Server

<br>

Requirements:
- ACTIVE DIRECTORY
- NETWORK POLICY SERVER (RADIUS)

<br>

~~~
!@Cisco
conf t
 username admin privilege 15 secret pass
 aaa new-model
 radius server WINRAD
  address ipv4 10.#$34T#.1.8 auth-port 1812 acct-port 1813
  key C1sc0123
  exit
 aaa group server radius RADGROUP
  server name WINRAD
  exit
 aaa authentication login default group RADGROUP local
 aaa authorization exec default group RADGROUP local
 line vty 0 14
  login authentication default
  end
~~~


<br>
<br>

---
&nbsp;


## Enterprise Certificate Authority

~~~
!@UTM-PH
conf t
 hostname UTM-PH
 enable secret pass
 service password-encryption
 no logging cons
 ip domain lookup
 ip domain lookup source-interface G2
 ip name-server 192.168.102.8
 line vty 0 14
  transport input all
  password pass
  login local
  exec-timeout 0 0
 int g1
  ip add 208.8.8.11 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.11 255.255.255.0
  no shut
 int g3
  ip add 10.11.11.113 255.255.255.224
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 ip route 0.0.0.0 0.0.0.0 208.8.8.2
 end
wr
!
~~~


<br>


Create a Service Account:
- Active Directory and Users and Computers

| New User    |              |
| ---         | ---          |
| User Name   | ca           |
| Full Name   | CERTAUTH     |
| Password    | C1sc0123     |
| Pass Policy | Never Expire |
| Member of   | IIS_IUSRS    |


&nbsp;
---
&nbsp;


### Install Active Directory Certificate Services

Afterwards, install ADCS Add-Ons:
- Certificate Enrollment Policy Web Service  
- Certificate Enrollment Web Service         
- Certificate Authority Web Enrollment
- Network Device Enrollment Service


&nbsp;
---
&nbsp;


### Create DNS Mapping for both Device
- Reverse Lookup Zone : 208.8.8.0
- A Record : utmph.net#$34T#.com : 208.8.8.11


~~~
!@UTM-PH
conf t
 crypto key generate rsa modulus 2048 label CERTKEY
 !
 crypto pki trustpoint NETPLUS
  enrollment terminal
  serial-number
  revocation-check none
  end
~~~


&nbsp;
---
&nbsp;


### Access CA Web Enrollment

Set Routes for trustpoints:
~~~
!@cmd
route add 208.8.8.11 mask 255.255.255.255 192.168.102.11
~~~

<br>
<br>


http://192.168.102.8/certsrv/mscep/mscep.dll  


<br>
<br>

Grab the Hash & Challenge Password    
- Hash: ___________    
- Pass: ___________ 


&nbsp;
---
&nbsp;


### Enroll Network Devices

~~~
!@UTM-PH
conf t
 crypto pki enroll NETPLUS
~~~
