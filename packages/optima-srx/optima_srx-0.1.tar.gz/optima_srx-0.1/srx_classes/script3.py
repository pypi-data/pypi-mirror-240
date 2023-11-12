from jnpr.junos.utils.config import Config
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import UnlockError
from jnpr.junos.exception import ConfigLoadError
from jnpr.junos.exception import CommitError
from lxml import etree
import ipaddress
sets = '''
set security address-book global description RHV_server address pacudssnrhvm 10.64.29.10
set security address-book global description RHV_server address pacudssnrhvh01 10.64.29.11
set security address-book global description RHV_server address pacudssnrhvh02 10.64.29.12
set security address-book global description RHV_server address pacudssnrhvh03 10.64.29.13
set security address-book global description RHV_server address pacudssnrhvh04 10.64.29.14
set security address-book global description RHV_server address pacudssnrhvh05 10.64.29.15
set security address-book global description RHV_server address pacudssnrhvh06 10.64.29.16
set security address-book global description RHV_server address pacudssnrhvh07 10.64.29.17
set security address-book global description Satellite_Server address vacudssnsat 10.64.24.18
set security address-book global description Ansible_Server address vacudssnansible01 10.64.24.19
set security address-book global description Ansible_Server address vacudssnansible02 10.64.24.20
set security address-book global description Ansible_Server address vacudssnansible03 10.64.24.21
set security address-book global description Ansible_Server address vacudssndb01 10.64.24.22
set security address-book global description IDM_server address vacudssnidm01 10.64.24.23
set security address-book global description IDM_server address vacudssnidm02 10.64.24.24
set security address-book global description Cloudforms_Server address vacudssnmaster01 10.64.24.30
set security address-book global description Cloudforms_Server address vacudssnmaster02 10.64.24.26
set security address-book global description Cloudforms_Server address vacudssnmaster03 10.64.24.27
set security address-book global description Cloudforms_Server address vacudssnmaster04 10.64.24.28
set security address-book global description Cloudforms_Server address vacudssnmaster05 10.64.24.29
set security address-book global description Cloudforms_Server address vacudssncf07 10.64.24.31
set security address-book global description Cloudforms_Server address vacudssncf08 10.64.24.32
set security address-book global description Cloudforms_Server address vacudssncf09 10.64.24.33
set security address-book global description Cloudforms_Server address vacudssncf10 10.64.24.34
set security address-book global description Cloudforms_Server address vacudssncf11 10.64.24.35
set security address-book global description Cloudforms_Server address vacudssncf12 10.64.24.36
set security address-book global description OpenStack_Server address vacudssnospdir01 10.64.24.50
set security address-book global description OpenStack_Server address pacudssnospctrl01 10.64.24.51
set security address-book global description OpenStack_Server address pacudssnospctrl02 10.64.24.52
set security address-book global description OpenStack_Server address pacudssnospctrl03 10.64.24.53
set security address-book global description OpenStack_Server address pacudssnstor01 10.64.24.55
set security address-book global description OpenStack_Server address pacudssnstor02 10.64.24.56
set security address-book global description OpenStack_Server address pacudssnstor03 10.64.24.57
set security address-book global description OpenStack_Server address pacudssnstor04 10.64.24.58
set security address-book global description OpenStack_Server address pacudssnospcom01 10.64.24.70
set security address-book global description OpenStack_Server address pacudssnospcom02 10.64.24.71
set security address-book global description OpenStack_Server address pacudssnospcom03 10.64.24.72
set security address-book global description OpenStack_Server address pacudssnospcom04 10.64.24.73
set security address-book global description OpenStack_Server address pacudssnospcom05 10.64.24.74
set security address-book global description OpenStack_Server address pacudssnospcom06 10.64.24.75
set security address-book global description OpenStack_Server address pacudssnospcom07 10.64.24.76
set security address-book global description OpenStack_Server address pacudssnospcom08 10.64.24.77
set security address-book global description OpenStack_Server address pacudssnospcom09 10.64.24.78
set security address-book global description OpenStack_Server address pacudssnospcom10 10.64.24.79
set security address-book global description OpenStack_Server address pacudssnospcom11 10.64.24.80
set security address-book global description OpenStack_Server address pacudssnospcom12 10.64.24.81
set security address-book global description OpenStack_Server address pacudssnospcom13 10.64.24.82
set security address-book global description OpenStack_Server address pacudssnospcom14 10.64.24.83
set security address-book global description OpenStack_Server address pacudssnospcom15 10.64.24.84
set security address-book global description OpenStack_Server address pacudssnospcom16 10.64.24.85
set security address-book global description OpenStack_Server address pacudssnospcom17 10.64.24.86
set security address-book global description OpenStack_Server address pacudssnospcom18 10.64.24.87
set security address-book global description OpenStack_Server address pacudssnospcom19 10.64.24.88
set security address-book global description OpenStack_Server address pacudssnospcom20 10.64.24.89
set security address-book global description OpenStack_Server address pacudssnospcom21 10.64.24.90
set security address-book global description OpenStack_Server address pacudssnospcom22 10.64.24.91
set security address-book global description OpenStack_Server address pacudssnospcom23 10.64.24.92
set security address-book global description OpenStack_Server address pacudssnospcom24 10.64.24.93
set security address-book global description OpenStack_Server address pacudssnospcom25 10.64.24.94
set security address-book global description OpenStack_Server address pacudssnospcom26 10.64.24.95
set security address-book global description OpenStack_Server address pacudssnospcom27 10.64.24.96
set security address-book global description OpenStack_Server address pacudssnospcom28 10.64.24.97
set security address-book global description OpenStack_Server address pacudssnospcom29 10.64.24.98
set security address-book global description OpenStack_Server address pacudssnospcom30 10.64.24.99
set security address-book global description OpenStack_Server address pacudssnospcom31 10.64.24.100
set security address-book global description OpenStack_Server address pacudssnospcom32 10.64.24.101
set security address-book global description OpenStack_Server address pacudssnospcom33 10.64.24.102
set security address-book global description OpenStack_Server address pacudssnospcom34 10.64.24.103
set security address-book global description OpenStack_Server address pacudssnospcom35 10.64.24.104
set security address-book global description OpenStack_Server address pacudssnospcom36 10.64.24.105
set security address-book global description OpenStack_Server address pacudssnospcom37 10.64.24.106
set security address-book global description OpenStack_Server address pacudssnospcom38 10.64.24.107
set security address-book global description OpenStack_Server address pacudssnospcom39 10.64.24.108
set security address-book global description OpenStack_Server address pacudssnospcom40 10.64.24.109
set security address-book global description OpenStack_Server address pacudssnospcom41 10.64.24.110
set security address-book global description OpenStack_Server address pacudssnospcom42 10.64.24.111
set security address-book global description OpenStack_Server address pacudssnospcom43 10.64.24.112
set security address-book global description OpenStack_Server address pacudssnospcomdb01 10.64.24.150
set security address-book global description OpenStack_Server address pacudssnospcomdb02 10.64.24.151
set security address-book global description DNS_(_Temp_unitil_DDI_is_implemented) address CSADDSVD01 10.65.200.11
set security address-book global description DNS_(_Temp_unitil_DDI_is_implemented) address CSADDSVD02 10.65.200.12
set security address-book global description DNS_(_Temp_unitil_DDI_is_implemented) address CSADDSVD03 10.65.200.13
set security address-book global description DNS_(_Temp_unitil_DDI_is_implemented) address CSADDSLBVD 10.65.200.10
set security address-book global description Exchange address CSEXNLBVP01 10.65.200.64
set security address-book global description Exchange address CSExchVD01 10.65.200.52
set security address-book global description Exchange address CSExchVD02 10.65.200.53
set security address-book global description DHCP address CSDHCPVD01 10.65.200.21
set security address-book global description DHCP address CSDHCPVD02 10.65.200.22
set security address-book global description PKI address CSROOTVD01 10.65.200.31
set security address-book global description PKI address CSCAVD01 10.65.200.32
set security address-book global description PKI address CSCAVD02 10.65.200.33
set security address-book global description RDS address CSRDSVD01 10.65.200.41
set security address-book global description RDS address CSRDSVD02 10.65.200.42
set security address-book global description KMS address CSKMSVD01 10.65.200.46
set security address-book global description KMS address CSKMSVD02 10.65.200.47
set security address-book global description SQL_Always_ON address CSSQLVD01 10.65.200.81
set security address-book global description SQL_Always_ON address CSSQLVD02 10.65.200.82
set security address-book global description SQL_Always_ON address CSSQLCLUSTERVD01 10.65.200.83
set security address-book global description SQL_Always_ON address CSAGlistenerVD01 10.65.200.84
set security address-book global description WSUS address CSWSUSVD01 10.65.208.11
set security address-book global description WSUS address CSWSUSVD02 10.65.208.12
set security address-book global description ADFS address CSADFSVP01 10.65.200.110
set security address-book global description ADFS address CSADFSVP02 10.65.200.111
set security address-book global description ADFS address CSANLBVD 10.65.200.112
set security address-book global description ADFS address CSPADFSVP01 10.65.210.11
set security address-book global description ADFS address CSPADFSVP02 10.65.210.12
set security address-book global description ADFS address CSPNLBVD 10.65.210.13
set security address-book global description NTP address ACUD02-SSN-C10-NTP001 10.65.200.101
set security address-book global description NTP address ACUD02-SSN-C11-NTP002 10.65.200.102
set security address-book global description NTP address CSNTPLBVD 10.65.200.100
set security address-book global address RH_Ovirtmgmt_Subnet 10.64.29.0/27
set security address-book global address CSIAMJOBVD01 10.64.10.210
set security address-book global address CSIAMJOBVD02 10.64.10.211
set security address-book global address CSIAMWEBVD01 10.64.10.212
set security address-book global address CSIAMWEBVD02 10.64.10.213
set security address-book global address CQIAMJOBVD01 10.33.10.210
set security address-book global address CQIAMJOBVD02 10.33.10.211
set security address-book global address CQIAMWEBVD01 10.33.10.212
set security address-book global address CQIAMWEBVD02 10.33.10.213
set security address-book global address CSIAMDBVD01 10.64.10.186
set security address-book global address CSIAMDBVD02 10.64.10.187
set security address-book global address CQIAMDBVD01 10.33.10.186
set security address-book global address CQIAMDBVD02 10.33.10.187
set security address-book global address CQADDSVD01 10.34.200.11
set security address-book global address CQADDSVD02 10.34.200.12
set security address-book global address CQADDSVD03 10.34.200.13
set security address-book global address CQEXNLBVP01 10.34.200.64
set security address-book global address CQExchVD01 10.34.200.52
set security address-book global address CQExchVD02 10.34.200.53
set security address-book global address CQExchVD03 10.34.200.54
set security address-book global address CQExchVD04 10.34.200.55
set security address-book global address CQExchVD05 10.34.200.56
set security address-book global address 10.64.0.0_16 10.64.0.0/16
set security address-book global address 10.65.0.0_16 10.65.0.0/16
set security address-book global address 10.32.0.0_16 10.32.0.0/16
set security address-book global address 10.33.0.0_16 10.33.0.0/16
set security address-book global address 10.34.0.0_16 10.34.0.0/16
set security address-book global address ACUD01-SSN-DEE-PPAMSPP01PD 10.33.10.194
set security address-book global address ACUD01-QPN-DEE-PPAMSPP02PD 10.33.10.195
set security address-book global address ACUD01-QPN-DEE-PPAMSPP03PD 10.33.10.196
set security address-book global address CQPAMSPSVD01_1 10.33.10.197
set security address-book global address CQPAMSPSVD01_2 10.33.10.198
set security address-book global address CQPAMSPSVD02_1 10.33.10.199
set security address-book global address CQPAMSPSVD02_2 10.33.10.200
set security address-book global address ACUD01-SSN-DEE-PPAMSPP01PD 10.64.10.194
set security address-book global address ACUD01-SSN-DEE-PPAMSPP02PD 10.64.10.195
set security address-book global address ACUD01-SSN-DEE-PPAMSPP03PD 10.64.10.196
set security address-book global address CSPAMSPSVD01_1 10.64.10.197
set security address-book global address CSPAMSPSVD01_2 10.64.10.198
set security address-book global address CSPAMSPSVD02_1 10.64.10.199
set security address-book global address CSPAMSPSVD02_2 10.64.10.200
set security address-book global address RH_COC_IPMI_Subnet 10.64.20.0/22
set security address-book global address 10.64.24.0_22 10.64.24.0/22
set security address-book global address RH_management_Subnet 10.64.24.0/22
set security address-book global address OSP-CiscoAPI_Subnet 10.64.32.0/24
set security address-book global address ACI-components_Subnet 10.64.8.0/28
set security address-book global address ACI-components_Subnet_64-9 10.64.9.0/24
set security address-book global address Internal_API__Subnet 10.64.31.0/24
set security address-book global address ACUD-SSN-UNI480F-0154 10.64.70.20
set security address-book global address ACUD-SSN-UNI480F-0150 10.64.70.21
set security address-book global address ACUD-SSN-UNI880F-0152 10.64.70.22
set security address-book global address CP0-S031 10.64.70.5
set security address-book global address CP1-S031 10.64.70.6
set security address-book global address ACUD-SSN-X6-4-S031-DA1 10.64.70.7
set security address-book global address CP0-S022 10.64.70.8
set security address-book global address CP1-S022 10.64.70.9
set security address-book global address ACUD-SSN-X6-4-S022-DA2 10.64.70.10
set security address-book global address Z9100-SW1 10.64.70.30
set security address-book global address Z9100-SW2 10.64.70.31
set security address-book global address Isilon_Node_1 10.64.70.32
set security address-book global address Isilon_Node_2 10.64.70.33
set security address-book global address Isilon_Node_3 10.64.70.34
set security address-book global address Isilon_Node_4 10.64.70.35
set security address-book global address ssn0dbadm01 10.64.43.5
set security address-book global address ssn0dbadm02 10.64.43.6
set security address-book global address ssn0celadm01 10.64.43.7
set security address-book global address ssn0celadm02 10.64.43.8
set security address-book global address ssn0celadm03 10.64.43.9
set security address-book global address ssn0sw-adm0 10.64.43.10
set security address-book global address ssn0sw-rocea0 10.64.43.11
set security address-book global address ssn0sw-roceb0 10.64.43.12
set security address-book global address pacudssnexsw-adm0 10.64.43.15
set security address-book global address pacudssnexsw-rocea0 10.64.43.16
set security address-book global address pacudssnexsw-roceb0 10.64.43.17
set security address-book global address pacudssnexsw-pdua0 10.64.43.18
set security address-book global address pacudssnexsw-pdub0 10.64.43.19
set security address-book global address ssn0dbadm01-ilom 10.64.47.5
set security address-book global address ssn0dbadm02-ilom 10.64.47.6
set security address-book global address ssn0celadm01-ilom 10.64.47.7
set security address-book global address ssn0celadm02-ilom 10.64.47.8
set security address-book global address ssn0celadm03-ilom 10.64.47.9
set security address-book global address ssn0-connexo-vm01 10.65.40.5
set security address-book global address ssn0-connexo-vm02 10.65.40.6
set security address-book global address ssn0-eerp-vm01 10.65.40.21
set security address-book global address ssn0-eerp-vm02 10.65.40.22
set security address-book global address pacudssnexdb01c03 10.65.40.37
set security address-book global address pacudssnexdb02c03 10.65.40.38
set security address-book global address pacudssnexdb01c04 10.65.40.53
set security address-book global address pacudssnexdb02c04 10.65.40.54
set security address-book global address pacudssnexdb01c05 10.65.40.69
set security address-book global address pacudssnexdb02c05 10.65.40.70
set security address-book global address pacudssnexdb01c06 10.65.40.85
set security address-book global address pacudssnexdb02c06 10.65.40.86
set security address-book global address pacudssnexdb01c07 10.65.40.101
set security address-book global address pacudssnexdb02c07 10.65.40.102
set security address-book global address pacudssnexdb01c08 10.65.40.117
set security address-book global address pacudssnexdb02c08 10.65.40.118
set security address-book global address ssn0-connexo-vm01-vip 10.65.40.7
set security address-book global address ssn0-connexo-vm02-vip 10.65.40.8
set security address-book global address ssn0-eerp-vm01-vip 10.65.40.23
set security address-book global address ssn0-eerp-vm02-vip 10.65.40.24
set security address-book global address pacudssnexdb01c03-vip 10.65.40.39
set security address-book global address pacudssnexdb02c03-vip 10.65.40.40
set security address-book global address pacudssnexdb01c04-vip 10.65.40.55
set security address-book global address pacudssnexdb02c04-vip 10.65.40.56
set security address-book global address pacudssnexdb01c05-vip 10.65.40.71
set security address-book global address pacudssnexdb02c05-vip 10.65.40.72
set security address-book global address pacudssnexdb01c06-vip 10.65.40.87
set security address-book global address pacudssnexdb02c06-vip 10.65.40.88
set security address-book global address pacudssnexdb01c07-vip 10.65.40.103
set security address-book global address pacudssnexdb02c07-vip 10.65.40.104
set security address-book global address pacudssnexdb01c08-vip 10.65.40.119
set security address-book global address pacudssnexdb02c08-vip 10.65.40.120
set security address-book global address ssn0-connexo-scan 10.65.40.11
set security address-book global address ssn0-eerp-scan 10.65.40.27
set security address-book global address pacudssnexdb01c03-sc 10.65.40.43
set security address-book global address pacudssnexdb01c04-sc 10.65.40.59
set security address-book global address pacudssnexdb01c05-sc 10.65.40.75
set security address-book global address pacudssnexdb01c06-sc 10.65.40.91
set security address-book global address pacudssnexdb01c07-sc 10.65.40.107
set security address-book global address pacudssnexdb01c08-sc 10.65.40.123
set security address-book global address ssn0-connexo-vm01-bk 10.65.41.5
set security address-book global address ssn0-connexo-vm02-bk 10.65.41.6
set security address-book global address ssn0-eerp-vm01-bk 10.65.41.21
set security address-book global address ssn0-eerp-vm02-bk 10.65.41.22
set security address-book global address pacudssnexdb01c03-bk 10.65.41.37
set security address-book global address pacudssnexdb02c03-bk 10.65.41.38
set security address-book global address pacudssnexdb01c04-bk 10.65.41.53
set security address-book global address pacudssnexdb02c04-bk 10.65.41.54
set security address-book global address pacudssnexdb01c05-bk 10.65.41.69
set security address-book global address pacudssnexdb02c05-bk 10.65.41.70
set security address-book global address pacudssnexdb01c06-bk 10.65.41.85
set security address-book global address pacudssnexdb02c06-bk 10.65.41.86
set security address-book global address pacudssnexdb01c07-bk 10.65.41.101
set security address-book global address pacudssnexdb02c07-bk 10.65.41.102
set security address-book global address pacudssnexdb01c08-bk 10.65.41.117
set security address-book global address pacudssnexdb02c08-bk 10.65.41.118
set security address-book global address pacudssnexdb01c01-sb 10.65.41.11
set security address-book global address pacudssnexdb01c02-sb 10.65.41.27
set security address-book global address pacudssnexdb01c03-sb 10.65.41.43
set security address-book global address pacudssnexdb01c04-sb 10.65.41.59
set security address-book global address pacudssnexdb01c05-sb 10.65.41.75
set security address-book global address pacudssnexdb01c06-sb 10.65.41.91
set security address-book global address pacudssnexdb01c07-sb 10.65.41.107
set security address-book global address pacudssnexdb01c08-sb 10.65.41.123
set security address-book global address ssn0db01-priv1 192.168.10.1
set security address-book global address ssn0db01-priv2 192.168.10.2
set security address-book global address ssn0db02-priv1 192.168.10.3
set security address-book global address ssn0db02-priv2 192.168.10.4
set security address-book global address ssn0cel01-priv1 192.168.10.5
set security address-book global address ssn0cel01-priv2 192.168.10.6
set security address-book global address ssn0cel02-priv1 192.168.10.7
set security address-book global address ssn0cel02-priv2 192.168.10.8
set security address-book global address ssn0cel03-priv1 192.168.10.9
set security address-book global address ssn0cel03-priv2 192.168.10.10
set security address-book global address ssn0-connexo-vm01-priv1 192.168.10.11
set security address-book global address ssn0-connexo-vm01-priv2 192.168.10.12
set security address-book global address ssn0-connexo-vm02-priv1 192.168.10.13
set security address-book global address ssn0-connexo-vm02-priv2 192.168.10.14
set security address-book global address ssn0-eerp-vm01-priv1 192.168.10.15
set security address-book global address ssn0-eerp-vm01-priv2 192.168.10.16
set security address-book global address ssn0-eerp-vm02-priv1 192.168.10.17
set security address-book global address ssn0-eerp-vm02-priv2 192.168.10.18
set security address-book global address VACUDSSNOEMOMS1 10.64.44.5
set security address-book global address VACUDSSNOEMOMS2 10.64.44.6
set security address-book global address VACUDSSNOEMRAC1 10.64.44.7
set security address-book global address VACUDSSNOEMRAC1-vip 10.64.44.8
set security address-book global address VACUDSSNOEMRAC2 10.64.44.9
set security address-book global address VACUDSSNOEMRAC2-vip 10.64.44.10
set security address-book global address VACUDSSNOEMSCAN 10.64.44.13
set security address-book global address PACUDOEMRAC1-priv 10.65.39.5
set security address-book global address PACUDOEMRAC2-priv 10.65.39.6
set security address-book global address pacudsradbadm01 10.64.45.5
set security address-book global address pacudsradbadm02 10.64.45.6
set security address-book global address pacudsraceladm01 10.64.45.7
set security address-book global address pacudsraceladm02 10.64.45.8
set security address-book global address pacudsraceladm03 10.64.45.9
set security address-book global address pacudsrasw-adm0 10.64.45.10
set security address-book global address pacudsrasw-rocea0 10.64.45.11
set security address-book global address pacudsrasw-roceb0 10.64.45.12
set security address-book global address pacudsrasw-pdua0 10.64.45.13
set security address-book global address pacudsrasw-pdub0 10.64.45.14
set security address-book global address pacudsradbadm01-ilom 10.64.50.5
set security address-book global address pacudsradbadm02-ilom 10.64.50.6
set security address-book global address pacudsraceladm01-ilom 10.64.50.7
set security address-book global address pacudsraceladm02-ilom 10.64.50.8
set security address-book global address pacudsraceladm03-ilom 10.64.50.9
set security address-book global address 10.65.41.96_28 10.65.41.96/28
set security address-book global address 10.65.41.112_28 10.65.41.112/28
set security address-book global address 10.65.40.0_28 10.65.40.0/28
set security address-book global address 10.65.40.16_28 10.65.40.16/28
set security address-book global address 10.65.40.32_28 10.65.40.32/28
set security address-book global address 10.65.40.48_28 10.65.40.48/28
set security address-book global address 10.65.40.64_28 10.65.40.64/28
set security address-book global address 10.65.40.80_28 10.65.40.80/28
set security address-book global address 10.65.40.96_28 10.65.40.96/28
set security address-book global address 10.65.40.112_28 10.65.40.112/28
set security address-book global address 10.65.42.0_28 10.65.42.0/28
set security address-book global address 10.65.41.0_28 10.65.41.0/28
set security address-book global address SSN_Syslog_Server 10.64.10.229
set security address-book global address 10.65.41.16_28 10.65.41.16/28
set security address-book global address 10.65.41.32_28 10.65.41.32/28
set security address-book global address 10.65.41.48_28 10.65.41.48/28
set security address-book global address 10.65.41.64_28 10.65.41.64/28
set security address-book global address 10.65.41.80_28 10.65.41.80/28
set security address-book global address 10.65.29.0_24 10.65.29.0/24
set security address-book global address QPN_GigaMon_subnet 10.33.10.104/29
set security address-book global address SSN_GigaMon_subnet 10.64.10.56/29
set security address-book global address 10.64.29.0_27 10.64.29.0/27
set security address-book global address 10.33.10.99 10.33.10.99
set security address-book global address 10.33.10.100 10.33.10.100
set security address-book global address 10.33.10.101 10.33.10.101
set security address-book global address 10.33.10.90 10.33.10.90
set security address-book global address 10.33.10.91 10.33.10.91
set security address-book global address 10.33.10.98 10.33.10.98
set security address-book global address 10.64.10.42 10.64.10.42
set security address-book global address 10.64.10.43 10.64.10.43
set security address-book global address 10.32.11.56 10.32.11.56
set security address-book global address 10.32.11.57 10.32.11.57
set security address-book global address 10.32.11.58 10.32.11.58
set security address-book global address 10.32.10.74 10.32.10.74
set security address-book global address 10.32.10.75 10.32.10.75
set security address-book global address 10.32.10.76 10.32.10.76
set security address-book global address 10.32.10.77 10.32.10.77
set security address-book global address 10.32.10.90 10.32.10.90
set security address-book global address 10.32.10.91 10.32.10.91
set security address-book global address 10.32.11.50 10.32.11.50
set security address-book global address 10.32.11.51 10.32.11.51
set security address-book global address 10.32.11.52 10.32.11.52
set security address-book global address 10.32.11.53 10.32.11.53
set security address-book global address 10.32.12.17 10.32.12.17
set security address-book global address 10.32.12.18 10.32.12.18
set security address-book global address 10.32.12.19 10.32.12.19
set security address-book global address 10.32.12.20 10.32.12.20
set security address-book global address 10.32.12.21 10.32.12.21
set security address-book global address 10.32.12.22 10.32.12.22
set security address-book global address 10.33.12.17 10.33.12.17
set security address-book global address 10.33.12.18 10.33.12.18
set security address-book global address 10.33.12.19 10.33.12.19
set security address-book global address 10.33.12.20 10.33.12.20
set security address-book global address 10.33.12.21 10.33.12.21
set security address-book global address 10.33.12.22 10.33.12.22
set security address-book global address 10.33.12.23 10.33.12.23
set security address-book global address 10.65.12.17 10.65.12.17
set security address-book global address 10.65.12.18 10.65.12.18
set security address-book global address CQDWPLVD01 10.32.20.4
set security address-book global address CQDWPLVD02 10.32.20.5
set security address-book global address CQDWCGVD01 10.34.251.4
set security address-book global address CQSMITVD01 10.32.20.6
set security address-book global address CQSMITVD02 10.32.20.7
set security address-book global address CQRESRVD01 10.34.251.5
set security address-book global address CQREARVD01 10.34.251.6
set security address-book global address CQREARVD02 10.34.251.7
set security address-book global address CQREARVD03 10.34.251.8
set security address-book global address CQREARVD04 10.34.251.9
set security address-book global address CQREARVD05 10.34.251.10
set security address-book global address CQMIDTVD01 10.34.251.11
set security address-book global address CQMIDTVD02 10.34.251.12
set security address-book global address CQREDBVD01 10.34.250.4
set security address-book global address CQREDBVD02 10.34.250.5
set security address-book global address CQRSDBVD01 10.34.250.6
set security address-book global address CQDISCVD01 10.34.252.4
set security address-book global address CQWINPVD01 10.34.252.5
set security address-book global address CQENCOVD01 10.34.253.4
set security address-book global address CQENPOVD01 10.34.253.5
set security address-book global address CQTSPRVD01 10.34.254.4
set security address-book global address CQRSSOVD01 10.34.254.5
set security address-book global address CQRSSOVD02 10.34.254.6
set security address-book global address CQTSSRVD01 10.34.254.7
set security address-book global address CQTSINVD01 10.34.254.8
set security address-book global address CQTSINVD02 10.34.254.9
set security address-book global address CQTSREVD01 10.34.254.10
set security address-book global address CQTSREVD02 10.34.254.11
set security address-book global address CQTSISVD01 10.34.254.12
set security address-book global address CQTSISVD02 10.34.254.13
set security address-book global address CQTSISVD03 10.34.254.14
set security address-book global address CQTSSIVD01 10.34.254.15
set security address-book global address CQTSRCVD01 10.34.254.16
set security address-book global address CQTSRCVD02 10.34.254.17
set security address-book global address CQTSRCVD03 10.34.254.18
set security address-book global address CQTSPGVD01 10.34.254.19
set security address-book global address CQTRDBVD01 10.34.250.7
set security address-book global address CQAPVMVD01 10.34.251.67
set security address-book global address CQAPACVD01 10.34.251.68
set security address-book global address CQAPSPVD01 10.34.251.69
set security address-book global address CQTSCOVD01 10.34.252.67
set security address-book global address CQTETLVD01 10.34.252.68
set security address-book global address CQTCDBVD01 10.34.250.7
set security address-book global address CQTSSAVD01 10.34.250.8
set security address-book global address CQTSAFVD01 10.34.253.67
set security address-book global address CQTSARVD01 10.34.253.67
set security address-book global address CQTSARVD02 10.34.253.68
set security address-book global address CQTSARVD03 10.34.253.69
set security address-book global address CQTSARVD04 10.34.253.70
set security address-book global address CQTSARVD05 10.34.253.71
set security address-book global address CQTSARVD06 10.34.253.72
set security address-book global address CQTSDBVD01 10.34.250.9
set security address-book global address CQTSVMVD01 10.34.254.67
set security address-book global address CQTVDBVD01 10.34.250.10
set security address-book global address CQTSORVD01 10.34.251.131
set security address-book global address CQTSORVD02 10.34.251.132
set security address-book global address CQTSORVD03 10.34.251.133
set security address-book global address CQTSORVD04 10.34.251.134
set security address-book global address CQTODBVD01 10.34.250.11
set security address-book global address CQTODBVD02 10.34.250.12
set security address-book global address CQTSNAVD01 10.34.252.31
set security address-book global address CSREARVD01 10.65.251.6
set security address-book global address CSREARVD02 10.65.251.7
set security address-book global address CSREARVD03 10.65.251.8
set security address-book global address CSREARVD04 10.65.251.9
set security address-book global address CSREARVD05 10.65.251.10
set security address-book global address CSMIDTVD01 10.65.251.11
set security address-book global address CSMIDTVD02 10.65.251.12
set security address-book global address CSREDBVD01 10.65.250.4
set security address-book global address CSREDBVD02 10.65.250.5
set security address-book global address CSDISCVD01 10.65.252.4
set security address-book global address CSWINPVD01 10.65.252.5
set security address-book global address CSENCOVD01 10.65.253.4
set security address-book global address CSENPOVD01 10.65.253.5
set security address-book global address CSTSPRVD01 10.65.254.4
set security address-book global address CSRSSOVD01 10.65.254.5
set security address-book global address CSTSSRVD01 10.65.254.6
set security address-book global address CSTSINVD01 10.65.254.7
set security address-book global address CSTSREVD01 10.65.254.8
set security address-book global address CSTSISVD01 10.65.254.9
set security address-book global address CSTSISVD02 10.65.254.10
set security address-book global address CSTSRCVD01 10.65.254.11
set security address-book global address CSTSPGVD01 10.65.254.12
set security address-book global address CSTRDBVD01 10.65.250.6
set security address-book global address CSTSCOVD01 10.65.251.67
set security address-book global address CSTETLVD01 10.65.251.68
set security address-book global address CSTCDBVD01 10.65.250.7
set security address-book global address CSTSSAVD01 10.65.252.67
set security address-book global address CSTSAFVD01 10.65.252.68
set security address-book global address CSTSARVD01 10.65.252.69
set security address-book global address CSTSARVD02 10.65.252.70
set security address-book global address CSTSARVD03 10.65.252.71
set security address-book global address CSTSARVD04 10.65.252.72
set security address-book global address CSTSARVD05 10.65.252.73
set security address-book global address CSTSARVD06 10.65.252.74
set security address-book global address CSTSDBVD01 10.65.250.8
set security address-book global address CSTSVMVD01 10.65.253.67
set security address-book global address CSTVDBVD01 10.65.250.9
set security address-book global address CCP_IoTHub_01 10.65.124.4
set security address-book global address CCP_IoTHub_02 10.65.124.5
set security address-book global address CCP_IoTHub_03 10.65.124.6
set security address-book global address CCP_CEP_Engine_01 10.65.124.7
set security address-book global address CCP_CEP_Engine_02 10.65.124.8
set security address-book global address CCP_CEP_Engine_03 10.65.124.9
set security address-book global address CCP_CEP_Engine_04 10.65.124.10
set security address-book global address CCP_CEP_Engine_05 10.65.124.11
set security address-book global address CCP_API_manger_01 10.65.124.12
set security address-book global address CCP_API_manger_02 10.65.124.13
set security address-book global address CCP_ESB_01 10.65.124.14
set security address-book global address CCP_ESB_02 10.65.124.15
set security address-book global address CCP_key_management_01 10.65.124.16
set security address-book global address CCP_key_management_02 10.65.124.17
set security address-book global address CCP_Bigdata_Master_01 10.68.40.4
set security address-book global address CCP_Bigdata_Master_02 10.68.40.5
set security address-book global address CCP_Bigdata_Slave_01 10.68.40.4
set security address-book global address CCP_Bigdata_Slave_02 10.68.40.5
set security address-book global address CCP_Bigdata_Slave_03 10.68.40.6
set security address-book global address CCP_Bigdata_Slave_04 10.68.40.7
set security address-book global address CCP_Bigdata_Slave_05 10.68.40.8
set security address-book global address CCP_Bigdata_Slave_06 10.68.40.9
set security address-book global address CCP_Bigdata_Slave_07 10.68.40.10
set security address-book global address CCP_PowerBI_Report_01 10.65.125.13
set security address-book global address CCP_PowerBI_Report_02 10.65.125.14
set security address-book global address CCP_Analytics_Engine_01 10.68.40.15
set security address-book global address CCP_Analytics_Engine_02 10.68.40.16
set security address-book global address CCP_ML_analytics_01 10.65.125.17
set security address-book global address CCP_ML_analytics_02 10.65.125.18
set security address-book global address CCP_GIS_App_01 10.65.124.18
set security address-book global address CCP_GIS_App_02 10.65.124.19
set security address-book global address CCP_GIS_App_03 10.65.124.20
set security address-book global address CCP_GIS_DB_01 10.68.40.21
set security address-book global address CCP_GIS_DB_02 10.68.40.22
set security address-book global address CCP_IoTOPs_01 10.65.124.23
set security address-book global address CCP_IoTOPs_02 10.65.124.24
set security address-book global address CCP_Platform_Database_01 10.68.40.19
set security address-book global address CCP_Platform_Database_02 10.68.40.20
set security address-book global address CCP_Logging_Monitoring_01 10.65.125.21
set security address-book global address CCP_Logging_Monitoring_02 10.65.125.22
set security address-book global address CCP_Logging_Monitoring_03 10.65.125.23
set security address-book global address CCP_DB_01 10.65.126.4
set security address-book global address CCP_DB_02 10.65.126.5
set security address-book global address CCP_APP_administration_01 10.65.126.6
set security address-book global address CCP_APP_administration_02 10.65.126.7
set security address-book global address CCP_Dashboard_Report_01 10.65.126.8
set security address-book global address CCP_Dashboard_Report_02 10.65.126.9
set security address-book global address CCP_APP_Server_01 10.65.127.4
set security address-book global address CCP_APP_Server_02 10.65.127.5
set security address-book global address CCP_DB_Server_01 10.68.40.6
set security address-book global address CCP_DB_Server_02 10.68.40.7
set security address-book global address CCP_Deployment 10.65.128.4
set security address-book global address CCP_Domain_01 10.65.129.4
set security address-book global address CCP_Domain_02 10.65.129.5
set security address-book global address CCPP_Load_balancer_01 10.65.130.4
set security address-book global address CCPP_Load_balancer_02 10.65.130.5
set security address-book global address CEP_APP_Server_01 10.34.120.4
set security address-book global address CEP_APP_Server_02 10.34.120.5
set security address-book global address CEP_supporting_01 10.34.120.6
set security address-book global address CEP_supporting_02 10.34.120.7
set security address-book global address CEP_DB_01 10.34.120.8
set security address-book global address CEP_DB_02 10.34.120.9
set security address-book global address CEP_Chat_Engine_01 10.34.120.10
set security address-book global address CEP_Chat_Engine_02 10.34.120.11
set security address-book global address CEP_Portal_web_01 10.34.120.12
set security address-book global address CEP_Portal_web_02 10.34.120.13
set security address-book global address CEP_Portal_DB_01 10.34.120.15
set security address-book global address CEP_Portal_DB_02 10.34.120.16
set security address-book global address CEP_API_manger_01 10.34.120.17
set security address-book global address CEP_API_manger_02 10.34.120.18
set security address-book global address CEP_ESB_01 10.34.120.19
set security address-book global address CEP_ESB_02 10.34.120.20
set security address-book global address CEP_SM_analytics_01 10.34.120.23
set security address-book global address CEP_SM_analytics_02 10.34.120.24
set security address-book global address CEP_key_managment_01 10.34.120.21
set security address-book global address CEP_key_managment_02 10.34.120.22
set security address-book global address CEP_MEAP_Application_01 10.34.121.4
set security address-book global address CEP_MEAP_Application_02 10.34.121.5
set security address-book global address CEP_Open_Data__App_01 10.34.122.4
set security address-book global address CEP_Open_Data__App_02 10.34.122.5
set security address-book global address CEP_Open_Data_API_01 10.34.122.6
set security address-book global address CEP_Open_Data_API_02 10.34.122.7
set security address-book global address CEP_Open_Data__DB_01 10.34.122.8
set security address-book global address CEP_Open_Data__DB_02 10.34.122.9
set security address-book global address CEP_Notification_01 10.34.122.10
set security address-book global address CEP_Notification_02 10.34.122.11
set security address-book global address Load_Balancer_External_01 10.32.16.4
set security address-book global address Load_Balancer_External_02 10.32.16.5
set security address-book global address SCADA_Exp_St_Flex_01 10.65.120.4
set security address-book global address SCADA_Exp_St_Flex_02 10.65.120.5
set security address-book global address SCADA_Exp_St_Flex_03 10.65.120.6
set security address-book global address SCADA_Exp_St_Flex_04 10.65.120.7
set security address-book global address SCADA_Exp_St_Flex_05 10.65.120.8
set security address-book global address SCADA_Exp_St_Flex_06 10.65.120.9
set security address-book global address SCADA_Exp_St_Flex_07 10.65.120.10
set security address-book global address SCADA_Exp_St_Flex_Eng_01 10.65.120.11
set security address-book global address SCADA_Exp_St_Flex_Eng_02 10.65.120.12
set security address-book global address SCADA_Exp_St_Flex_Eng_03 10.65.120.14
set security address-book global address SCADA_Experion_01 10.65.120.15
set security address-book global address SCADA_Experion_02 10.65.120.16
set security address-book global address SCADA_Experion_03 10.65.120.17
set security address-book global address SCADA_Experion_04 10.65.120.18
set security address-book global address SCADA_Experion_05 10.65.120.19
set security address-book global address SCADA_Domain_Controller_mng 10.65.120.20
set security address-book global address SCADA_Domain_Controller_prod 10.65.120.21
set security address-book global address ADMS_Data_collection_01 10.65.121.4
set security address-book global address ADMS_Data_collection_02 10.65.121.5
set security address-book global address ADMS_Data_OMS_01 10.65.121.6
set security address-book global address ADMS_Data_OMS_02 10.65.121.7
set security address-book global address ADMS_Data_DMS_01 10.65.121.8
set security address-book global address ADMS_Data_DMS_02 10.65.121.9
set security address-book global address ADMS_Electrical_OTS_dataCollection_ 10.65.121.10
set security address-book global address ADMS_Electrical_OTS_Application_ 10.65.121.11
set security address-book global address ADMS_Historian_01 10.65.121.12
set security address-book global address ADMS_Historian_02 10.65.121.13
set security address-book global address ADMS_OWS_1 10.65.121.14
set security address-book global address ADMS_OWS_2 10.65.121.15
set security address-book global address AMI_Connexo_DB_01 10.65.123.4
set security address-book global address AMI_Connexo_DB_02 10.65.123.5
set security address-book global address AMI_Connexo_App_WS_01 10.65.123.6
set security address-book global address AMI_Connexo_App_WS_02 10.65.123.7
set security address-book global address AMI_Connexo_App_WS_03 10.65.123.8
set security address-book global address AMI_Connexo_App_WS_04 10.65.123.9
set security address-book global address AMI_Connexo_App_WS_05 10.65.123.10
set security address-book global address AMI_Connexo__Communication_01 10.65.123.11
set security address-book global address AMI_Connexo__Communication_02 10.65.123.12
set security address-book global address AMI_Connexo__Communication_03 10.65.123.13
set security address-book global address AMI_Connexo__Communication_04 10.65.123.14
set security address-book global address AMI_Connexo__Communication_05 10.65.123.15
set security address-book global address AMI_Connexo_GUI 10.65.123.17
set security address-book global address 10.65.29.250 10.65.29.250
set security address-book global address 10.68.40.5-29 range-address 10.68.40.5 to 10.68.40.29
set security address-book global address 10.65.122.4-24 range-address 10.65.122.4 to 10.65.122.24
set security address-book global address 10.215.193.11-58 range-address 10.215.193.11 to 10.215.193.58
set security address-book global address 10.215.194.11-58 range-address 10.215.194.11 to 10.215.194.58
set security address-book global address 10.215.195.11-58 range-address 10.215.195.11 to 10.215.195.58
set security address-book global address 10.64.24.10-36 range-address 10.64.24.10 to 10.64.24.36
set security address-book global address 10.64.24.50-58 range-address 10.64.24.50 to 10.64.24.58
set security address-book global address 10.64.24.70-112 range-address 10.64.24.70 to 10.64.24.112
set security address-book global address 10.64.24.150-151 range-address 10.64.24.150 to 10.64.24.151
set security address-book global address CSNCSVD01-DEP 10.65.90.4
set security address-book global address CSNCSVD01-CNT1 10.65.90.5
set security address-book global address CSNCSVD01-CNT2 10.65.90.6
set security address-book global address CSNCSVD01-CNT3 10.65.90.7
set security address-book global address CSNCSVD01-EDG1 10.65.100.22
set security address-book global address CSNCSVD01-EDG2 10.65.100.23
set security address-book global address SSN_NCS_VIP_Edg 10.65.100.24
set security address-book global address CSFODEPVD01 10.65.110.5
set security address-book global address CSFOLBVD01 10.65.110.6
set security address-book global address CSFOLBVD02 10.65.110.7
set security address-book global address CSFOOMVD01 10.65.110.8
set security address-book global address CSFOOMVD02 10.65.110.9
set security address-book global address CSFOOMVD03 10.65.110.10
set security address-book global address CSFOCATVD01 10.65.110.11
set security address-book global address CSFOCATVD02 10.65.110.12
set security address-book global address CSFOOAMVD01 10.65.110.13
set security address-book global address CSFOOAMVD02 10.65.110.14
set security address-book global address CSFOILCVD01 10.65.110.15
set security address-book global address CSFOILCVD02 10.65.110.16
set security address-book global address CSFOARCVD01 10.65.110.17
set security address-book global address CSFOARCVD02 10.65.110.18
set security address-book global address CSCBOVMDSD01 10.65.65.5
set security address-book global address CSCBOGSST01 10.65.65.6
set security address-book global address CSCBOINTD01 10.65.65.7
set security address-book global address CSCBOJOBD01 10.65.65.8
set security address-book global address CSCBOTSD01 10.65.65.9
set security address-book global address CSNCSVD01-DEP-CDCSSN-DC 10.65.90.6
set security address-book global address CSNCSVD01-CNT1-CDCSSN-DC 10.65.90.7
set security address-book global address CSNCSVD01-CNT2-CDCSSN-DC 10.65.90.8
set security address-book global address CSNCSVD01-CNT3-CDCSSN-DC 10.65.90.9
set security address-book global address CSNCSVD01-EDG1OAM-CDCSSN-DC 10.65.90.10
set security address-book global address CSNCSVD01-EDG2OAM-CDCSSN-DC 10.65.90.11
set security address-book global address CSFODEPVD01OAM-CDCSSN-DC 10.65.110.5
set security address-book global address CSFOLBVD01OAM-CDCSSN-DC 10.65.110.6
set security address-book global address CSFOLBVD02OAM-CDCSSN-DC 10.65.110.7
set security address-book global address CSFOOMVD01OAM-CDCSSN-DC 10.65.110.8
set security address-book global address CSFOOMVD02OAM-CDCSSN-DC 10.65.110.9
set security address-book global address CSFOOMVD03OAM-CDCSSN-DC 10.65.110.10
set security address-book global address CSFOCATVD01OAM-CDCSSN-DC 10.65.110.11
set security address-book global address CSFOCATVD02OAM-CDCSSN-DC 10.65.110.12
set security address-book global address CSFOOAMVD01OAM-CDCSSN-DC 10.65.110.13
set security address-book global address CSFOOAMVD02OAM-CDCSSN-DC 10.65.110.14
set security address-book global address CSFOILCVD01OAM-CDCSSN-DC 10.65.110.15
set security address-book global address CSFOILCVD02OAM-CDCSSN-DC 10.65.110.16
set security address-book global address CSFOARCVD01OAM-CDCSSN-DC 10.65.110.17
set security address-book global address CSFOARCVD02OAM-CDCSSN-DC 10.65.110.18
set security address-book global address CSCBAVMDSD01OAM-CDCSSN-DC 10.65.65.5
set security address-book global address CSCBAGSSD01OAM-CDCSSN-DC 10.65.65.6
set security address-book global address CSBAINTD01OAM-CDCSSN-DC 10.65.65.7
set security address-book global address 10.215.195.11-17_ range-address 10.215.195.11 to 10.215.195.17
set security address-book global address 10.215.195.44-50 range-address 10.215.195.44 to 10.215.195.50
set security address-book global address CSCBAJOBD01OAM-CDCSSN-DC 10.65.65.8
set security address-book global address CSCBATSD01OAM-CDCSSN-DC 10.65.65.9
set security address-book global description Etisalat_Operators address Etisalat-Operator-2 10.215.193.12
set security address-book global description Etisalat_Operators address Etisalat-Operator-3 10.215.193.13
set security address-book global description Etisalat_Operators address Etisalat-Operator-4 10.215.193.14
set security address-book global description Etisalat_Operators address Etisalat-Operator-5 10.215.193.15
set security address-book global description Etisalat_Operators address Etisalat-Operator-6 10.215.193.16
set security address-book global description Etisalat_Operators address Etisalat-Operator-7 10.215.193.17
set security address-book global description Etisalat_Operators address Etisalat-Operator-8 10.215.193.18
set security address-book global description Etisalat_Operators address Etisalat-Operator-9 10.215.193.19
set security address-book global description Etisalat_Operators address Etisalat-Operator-10 10.215.193.20
set security address-book global description Etisalat_Operators address Etisalat-Operator-11 10.215.193.21
set security address-book global description Etisalat_Operators address Etisalat-Operator-12 10.215.193.22
set security address-book global description Etisalat_Operators address Etisalat-Operator-13 10.215.193.23
set security address-book global description Etisalat_Operators address Etisalat-Operator-14 10.215.193.24
set security address-book global description Etisalat_Operators address Etisalat-Operator-15 10.215.193.25
set security address-book global description Etisalat_Operators address Etisalat-Operator-16 10.215.193.26
set security address-book global description Etisalat_Operators address Etisalat-Operator-17 10.215.193.27
set security address-book global description Etisalat_Operators address Etisalat-Operator-18 10.215.193.28
set security address-book global description Etisalat_Operators address Etisalat-Operator-19 10.215.193.29
set security address-book global description Etisalat_Operators address Etisalat-Operator-20 10.215.193.30
set security address-book global description Etisalat_Operators address Etisalat-Operator-21 10.215.193.31
set security address-book global description Etisalat_Operators address Etisalat-Operator-22 10.215.193.32
set security address-book global description Etisalat_Operators address Etisalat-Operator-23 10.215.193.33
set security address-book global description Etisalat_Operators address Etisalat-Operator-24 10.215.193.34
set security address-book global description Etisalat_Operators address Etisalat-Operator-25 10.215.193.35
set security address-book global description Etisalat_Operators address Etisalat-Operator-26 10.215.193.36
set security address-book global description Etisalat_Operators address Etisalat-Operator-27 10.215.193.37
set security address-book global description Etisalat_Operators address Etisalat-Operator-28 10.215.193.38
set security address-book global description Etisalat_Operators address Etisalat-Operator-29 10.215.193.39
set security address-book global description Etisalat_Operators address Etisalat-Operator-30 10.215.193.40
set security address-book global description Etisalat_Operators address Etisalat-Operator-31 10.215.193.41
set security address-book global description Etisalat_Operators address Etisalat-Operator-32 10.215.193.42
set security address-book global description Etisalat_Operators address Etisalat-Operator-33 10.215.193.43
set security address-book global description Etisalat_Operators address Etisalat-Operator-34 10.215.193.44
set security address-book global description Etisalat_Operators address Etisalat-Operator-35 10.215.193.45
set security address-book global description Etisalat_Operators address Etisalat-Operator-36 10.215.193.46
set security address-book global description Etisalat_Operators address Etisalat-Operator-37 10.215.193.47
set security address-book global description Etisalat_Operators address Etisalat-Operator-38 10.215.193.48
set security address-book global description Etisalat_Operators address Etisalat-Operator-39 10.215.193.49
set security address-book global description Etisalat_Operators address Etisalat-Operator-40 10.215.193.50
set security address-book global description Etisalat_Operators address Etisalat-Operator-41 10.215.193.51
set security address-book global description Etisalat_Operators address Etisalat-Operator-42 10.215.193.52
set security address-book global description Etisalat_Operators address Etisalat-Operator-43 10.215.193.53
set security address-book global description Etisalat_Operators address Etisalat-Operator-44 10.215.193.54
set security address-book global description Etisalat_Operators address Etisalat-Operator-45 10.215.193.55
set security address-book global description Etisalat_Operators address Etisalat-Operator-46 10.215.193.56
set security address-book global description Etisalat_Operators address Etisalat-Operator-47 10.215.193.57
set security address-book global description Etisalat_Operators address Etisalat-Operator-48 10.215.193.58
set security address-book global description Load_Balancer-_External address LoadBalancer_External_01 10.32.16.4
set security address-book global description Load_Balancer-_External address LoadBalancer_External_02 10.32.16.5
set security address-book global description MEAP_Application_server address CEP_MEAPApplication_01 10.34.121.4
set security address-book global description MEAP_Application_server address CEP_MEAPApplication_02 10.34.121.5
set security address-book global description Application_Server address SCADA_Exp_St_Flex_Eng_04 10.65.120.14
set security address-book global description App_Server address AMI_Connexo_Communication_01 10.65.123.11
set security address-book global description App_Server address AMI_Connexo_Communication_02 10.65.123.12
set security address-book global description App_Server address AMI_Connexo_Communication_03 10.65.123.13
set security address-book global description App_Server address AMI_Connexo_Communication_04 10.65.123.14
set security address-book global description App_Server address AMI_Connexo_Communication_05 10.65.123.15
set security address-book global description GUI_Server address AMI_Connexo_GUI_01 10.65.123.16
set security address-book global description GUI_Server address AMI_Connexo_GUI_02 10.65.123.17
set security address-book global description Load_balancer-_internal address CCPP_Loadbalancer_01 10.65.130.4
set security address-book global description Load_balancer-_internal address CCPP_Loadbalancer_02 10.65.130.5
set security address-book global description Digital_Signage_-_Navori address Navori-QL-1 10.65.132.11
set security address-book global description Digital_Signage_-_Navori address Navori-QL-2 10.65.132.12
set security address-book global description Digital_Signage_-_Navori address Navori-QL-3 10.65.132.13
set security address-book global description Digital_Signage_-_Navori address Navori-QL-4 10.65.132.14
set security address-book global description Digital_Signage_-_Navori address Navori-QL-5 10.65.132.15
set security address-book global description Digital_Signage_-_Navori address Navori-QL-6 10.65.132.16
set security address-book global description Kasberesky_Admin_management_server address Kasp_Admin_Mng 10.65.134.11
set security address-book global description Citrix_Delivery_Control_server address Citrix_Delivery_Control_01 10.65.135.11
set security address-book global description Citrix_Delivery_Control_server address Citrix_Delivery_Control_02 10.65.135.12
set security address-book global description Citrix_Store_Front_Server address Citrix_StoreFront_01 10.65.135.13
set security address-book global description Citrix_Store_Front_Server address Citrix_StoreFront_02 10.65.135.14
set security address-book global description Citrix_Database_SQL_Server_ address Citrix_SQL_Srv_01 10.65.135.15
set security address-book global description Citrix_Database_SQL_Server_ address Citrix_SQL_Srv_02 10.65.135.16
set security address-book global description Citrix_License_Server address Citrix_License_Srv 10.65.135.17
set security address-book global description Citrix_Dirctor_Server address Citrix_Director_Srv 10.65.135.18
set security address-book global description Citrix_File_Server address Citrix_File_Srv_01 10.65.135.19
set security address-book global description Citrix_File_Server address Citrix_File_Srv_02 10.65.135.20
set security address-book global description Citrix_Unified_Print address Citrix_Uni_Print 10.65.135.21
set security address-book global description Citrix_Normal_User_machine address Citrix_Normal_User_01 10.65.135.22
set security address-book global description Citrix_Normal_User_machine address Citrix_Normal_User_02 10.65.135.23
set security address-book global description Citrix_Normal_User_machine address Citrix_Normal_User_03 10.65.135.24
set security address-book global description Citrix_Normal_User_machine address Citrix_Normal_User_04 10.65.135.25
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_01 10.65.135.26
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_02 10.65.135.27
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_03 10.65.135.28
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_04 10.65.135.29
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_05 10.65.135.30
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_06 10.65.135.31
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_07 10.65.135.32
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_08 10.65.135.33
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_09 10.65.135.34
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_10 10.65.135.35
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_11 10.65.135.36
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_12 10.65.135.37
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_13 10.65.135.38
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_14 10.65.135.39
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_15 10.65.135.40
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_16 10.65.135.41
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_17 10.65.135.42
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_18 10.65.135.43
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_19 10.65.135.44
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_20 10.65.135.45
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_21 10.65.135.46
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_22 10.65.135.47
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_23 10.65.135.48
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_24 10.65.135.49
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_25 10.65.135.50
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_26 10.65.135.51
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_27 10.65.135.52
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_28 10.65.135.53
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_29 10.65.135.54
set security address-book global description Citrix_Heavy_User_machine address Citrix_Heavy_User_30 10.65.135.55
set security address-book global description E-Business_ERP_Application_Server address EBus_Oracle_App_01 10.65.136.11
set security address-book global description E-Business_ERP_Application_Server address EBus_Oracle_App_02 10.65.136.12
set security address-book global description E-Business_ERP_Database_Server address Ebus_Oracle_DB_01 10.65.136.13
set security address-book global description E-Business_ERP_Database_Server address Ebus_Oracle_DB_02 10.65.136.14
set security address-book global description Parking_Database_Server address CCP_Parking_DB 10.65.127.6
set security address-book global description Lighting_Database_Server address CCP_Lighting_DB 10.65.127.7
set security address-book global description DMS_CSViewer_App_FE_Database_Server address DMS_CSViewer_App_FE_01 10.34.122.19
set security address-book global description DMS_CSViewer_App_FE_Database_Server address DMS_CSViewer_App_FE_02 10.34.122.20
set security address-book global description DMS_CSViewer_App_FE_Database_Server address DMS_CSViewer_App_FE_03 10.34.122.21
set security address-book global description DMS_CSAdmin_search address DMS_CSAdmin_Search_Srv_01 10.34.122.22
set security address-book global description DMS_CSAdmin_search address DMS_CSAdmin_Search_Srv_02 10.34.122.23
set security address-book global description DMS_CSAdmin_search address DMS_CSAdmin_Search_Srv_03 10.34.122.24
set security address-book global description DMS_Brava_Server address DMS_Brava_Srv_01 10.34.122.25
set security address-book global description DMS_Brava_Server address DMS_Brava_Srv_02 10.34.122.26
set security address-book global description DMS_Archive_Database_Server address DMS_Archive_01 10.34.122.27
set security address-book global description DMS_Archive_Database_Server address DMS_Archive_02 10.34.122.28
set security address-book global description DMS_Archive_Database_Server address DMS_Archive_03 10.34.122.29
set security address-book global description DMS_Archive_Database_Server address DMS_Archive_04 10.34.122.30
set security address-book global description DMS_OTDS_Database_Server address DMS_OTDS_01 10.34.122.31
set security address-book global description DMS_OTDS_Database_Server address DMS_OTDS_02 10.34.122.32
set security address-book global description DMS_OTDS_Database_Server address DMS_OTDS_03 10.34.122.33
set security address-book global description DMS_DB_Database_Server address DMS_DB_01 10.34.122.34
set security address-book global description DMS_DB_Database_Server address DMS_DB_02 10.34.122.35
set security address-book global description DMS_DB_Database_Server address DMS_DB_03 10.34.122.36
set security address-book global description DMS_OCR_Database_Server address DMS_OCR_01 10.34.122.37
set security address-book global description DMS_OCR_Database_Server address DMS_OCR_02 10.34.122.38
set security address-book global description DMS_OCR_Database_Server address DMS_OCR_03 10.34.122.39
set security address-book global description LDS_Mng_Latabase_Server address LDS_Mng_01 10.65.122.4
set security address-book global description LDS_Mng_Latabase_Server address LDS_Mng_02 10.65.122.5
set security address-book global description LDS_App_Latabase_Server address LDS_App_01 10.65.122.6
set security address-book global description LDS_App_Latabase_Server address LDS_App_02 10.65.122.7
set security address-book global description MDM_DevProf_Server address MDM_DevProf_Mng_01 10.34.120.50
set security address-book global description MDM_DevProf_Server address MDM_DevProf_Mng_02 10.34.120.51
set security address-book global description Load_balancer_ address LoadBalancer_Internal_01 10.34.121.6
set security address-book global description Load_balancer address LoadBalancer_Internal_02 10.34.121.7
set security address-book global description CCP_Automation_Server address CCP_Automation_BPM_01 10.34.121.8
set security address-book global description CCP_Automation_Server address CCP_Automation_BPM_02 10.34.121.9
set security address-book global description CEP_Portal_Server address CEP_Portal_web_03 10.34.120.14
set security address-book global description CCP_SSN_GIS_DB_Catabase_Server address CCP_SSN_GIS_DB_01 10.65.124.21
set security address-book global description CCP_SSN_GIS_DB_Catabase_Server address CCP_SSN_GIS_DB_02 10.65.124.22
set security address-book global description CCP_GIS_Server address CCP_GIS_DMZ_01 10.34.122.12
set security address-book global description CCP_GIS_Server address CCP_GIS_DMZ_02 10.34.122.13
set security address-book global description CCP_GIS_Server address CCP_GIS_DMZ_03 10.34.122.14
set security address-book global description CCP_GIS_Server address CCP_GIS_DMZ_04 10.34.122.15
set security address-book global description CCP_GIS_Server address CCP_GIS_DMZ_05 10.34.122.16
set security address-book global description CCP_GIS_Server address CCP_GIS_DMZ_06 10.34.122.17
set security address-book global description CCP_GIS_Server address CCP_GIS_DMZ_07 10.34.122.18
set security address-book global description Internal_Media_Server address CCP_InternalMedia_01 10.34.121.10
set security address-book global description Internal_Media_Server address CCP_InternalMedia_02 10.34.121.11
set security address-book global description GIS_SSN_Op_Postgres_XL address CCP_GIS_SSN_Op_Postgres_XL_01 10.65.131.4
set security address-book global description GIS_SSN_Op_Postgres_XL address CCP_GIS_SSN_Op_Postgres_XL_02 10.65.131.5
set security address-book global description GIS_SSN_Op_Postgres_XL address CCP_GIS_SSN_Op_Postgres_XL_03 10.65.131.6
set security address-book global description GIS_SSN_Op_Postgres_XL address CCP_GIS_SSN_Op_Postgres_XL_04 10.65.131.7
set security address-book global description GIS_SSN_Op_Postgres_XL address CCP_GIS_SSN_Op_Postgres_XL_05 10.65.131.8
set security address-book global description GIS_SSN_Op_Postgres_XL address CCP_GIS_SSN_Op_Postgres_XL_06 10.65.131.9
set security address-book global description GIS_SSN_Op_Postgres_XL address CCP_GIS_SSN_Op_Postgres_XL_07 10.65.131.10
set security address-book global description GIS_SSN_Op_Geo_Server address CCP_GIS_SSN_Op_Geo_Server_01 10.65.131.11
set security address-book global description GIS_SSN_Op_Geo_Server address CCP_GIS_SSN_Op_Geo_Server_02 10.65.131.12
set security address-book global description GIS_SSN_Op_Geo_Server address CCP_GIS_SSN_Op_Geo_Server_03 10.65.131.13
set security address-book global description GIS_SSN_Op_Geo_Server address CCP_GIS_SSN_Op_Geo_Server_04 10.65.131.14
set security address-book global description GIS_SSN_Op_Core_Services address CCP_GIS_SSN_Op_Core_Services_01 10.65.131.15
set security address-book global description GIS_SSN_Op_Core_Services address CCP_GIS_SSN_Op_Core_Services_02 10.65.131.16
set security address-book global description GIS_SSN_Op_Core_Services address CCP_GIS_SSN_Op_Core_Services_03 10.65.131.17
set security address-book global description GIS_SSN_Op_Core_Services address CCP_GIS_SSN_Op_Core_Services_04 10.65.131.18
set security address-book global description GIS_SSN_Op_Core_Services address CCP_GIS_SSN_Op_Core_Services_05 10.65.131.19
set security address-book global description GIS_SSN_Op_Core_Services address CCP_GIS_SSN_Op_Core_Services_06 10.65.131.20
set security address-book global description GIS_SSN_Op_Core_Services address CCP_GIS_SSN_Op_Core_Services_07 10.65.131.21
set security address-book global address 10.215.193.49-52 10.215.193.52
set security address-book global address 10.215.193.45-48 range-address 10.215.193.45 to 10.215.193.48
set security address-book global address 10.215.193.43-44 range-address 10.215.193.43 to 10.215.193.44
set security address-book global address 10.65.121.6-9 range-address 10.65.121.6 to 10.65.121.9
set security address-book global address 10.65.126.6-9 range-address 10.65.126.6 to 10.65.126.9
set security address-book global address 10.65.131.4-23 range-address 10.65.131.4 to 10.65.131.23
set security address-book global address 10.34.121.6-11 range-address 10.34.121.6 to 10.34.121.11
set security address-book global address 10.68.40.4-8 range-address 10.68.40.4 to 10.68.40.8
set security address-book global address 10.34.122.12-18 range-address 10.34.122.12 to 10.34.122.18
set security address-book global address 10.34.122.19-35 range-address 10.34.122.19 to 10.34.122.35
set security address-book global address 10.65.124.7-11 range-address 10.65.124.7 to 10.65.124.11
set security address-book global address 10.65.125.4-12 range-address 10.65.125.4 to 10.65.125.12
set security address-book global address 10.34.121.6-12 range-address 10.34.121.6 to 10.34.121.12
set security address-book global address 10.34.122.12-19 range-address 10.34.122.12 to 10.34.122.19
set security address-book global address 10.65.120.14-21 range-address 10.65.120.14 to 10.65.120.21
set security address-book global address 10.65.123.6-10 range-address 10.65.123.6 to 10.65.123.10
set security address-book global address 10.65.123.11-15 range-address 10.65.123.11 to 10.65.123.15
set security address-book global address 10.65.135.11-57 range-address 10.65.135.11 to 10.65.135.57
set security address-book global address 10.34.122.20-35 range-address 10.34.122.20 to 10.34.122.35
set security address-book global address 10.34.120.14 10.34.120.14
set security address-book global address 10.65.121.4-5 range-address 10.65.121.4 to 10.65.121.5
set security address-book global address 10.65.134.11 10.65.134.11
set security address-book global address 10.65.124.21-22 range-address 10.65.124.21 to 10.65.124.22
set security address-book global address 10.65.127.6-7 range-address 10.65.127.6 to 10.65.127.7
set security address-book global address Security_operators range-address 10.215.195.21 to 10.215.195.25
set security address-book global address Portal 10.64.24.10
set security address-book global address 10.215.195.11-10.215.195.17_ description Nokia_Horizon_access_range_1 range-address 10.215.195.11 to 10.215.195.17
set security address-book global address 10.215.195.44-10.215.195.50 description Nokia_Horizon_access_range_2 range-address 10.215.195.44 to 10.215.195.50
set security address-book global address ITSM_operators range-address 10.215.195.31 to 10.215.195.35
set security address-book global address 10.65.29.25 10.65.29.25
set security address-book global address PAM_Servers range-address 10.64.10.194 to 10.64.10.201
set security address-book global address 10.68.40.9-11 range-address 10.68.40.9 to 10.68.40.11
set security address-book global address 10.68.40.12-14 range-address 10.68.40.12 to 10.68.40.14
set security address-book global address 10.215.195.51-58 range-address 10.215.195.51 to 10.215.195.58
set security address-book global address Horizon_Portal 10.65.29.250
set security address-book global address Infra-machines range-address 10.65.200.11 to 10.65.200.102
set security address-book global address 10.65.128.4-5 range-address 10.65.128.4 to 10.65.128.5
set security address-book global address 10.65.130.4-5 range-address 10.65.130.4 to 10.65.130.5
set security address-book global address 10.65.131.4-21 range-address 10.65.131.4 to 10.65.131.21
set security address-book global address 10.65.120.4-21 range-address 10.65.120.4 to 10.65.120.21
set security address-book global address 10.65.132.11-16 range-address 10.65.132.11 to 10.65.132.16
set security address-book global address 10.65.121.4-20 range-address 10.65.121.4 to 10.65.121.20
set security address-book global address 10.65.122.4-7 range-address 10.65.122.4 to 10.65.122.7
set security address-book global address 10.65.135.11-55 range-address 10.65.135.11 to 10.65.135.55
set security address-book global address 10.65.123.4-19 range-address 10.65.123.4 to 10.65.123.19
set security address-book global address 10.65.136.11-14 range-address 10.65.136.11 to 10.65.136.14
set security address-book global address 10.65.124.4-27 range-address 10.65.124.4 to 10.65.124.27
set security address-book global address 10.32.16.4-5 range-address 10.32.16.4 to 10.32.16.5
set security address-book global address 10.65.125.13-23 range-address 10.65.125.13 to 10.65.125.23
set security address-book global address 10.34.120.4-24 range-address 10.34.120.4 to 10.34.120.24
set security address-book global address 10.65.126.4-13 range-address 10.65.126.4 to 10.65.126.13
set security address-book global address 10.34.121.4-11 range-address 10.34.121.4 to 10.34.121.11
set security address-book global address 10.65.127.4-10 range-address 10.65.127.4 to 10.65.127.10
set security address-book global address 10.34.122.4-39 range-address 10.34.122.4 to 10.34.122.39
set security address-book global address 10.68.40.4-28 range-address 10.68.40.4 to 10.68.40.28
set security address-book global address 10.68.40.15-16 range-address 10.68.40.15 to 10.68.40.16
set security address-book global address 10.65.125.50-51 range-address 10.65.125.50 to 10.65.125.51
set security address-book global address 10.65.129.4-5 range-address 10.65.129.4 to 10.65.129.5
set security address-book global address 10.65.128.5 10.65.128.5
set security address-book global address Nokia-App-1 description Nokia_Application_servers_(BMC) range-address 10.65.85.5 to 10.65.85.9
set security address-book global address Nokia-App-2 description Nokia_Application_servers_(BMC) range-address 10.65.85.37 to 10.65.85.41
set security address-book global address Nokia-App-3 description Nokia_Application_servers_(BMC) range-address 10.65.65.5 to 10.65.65.9
set security address-book global address Nokia-App-4 description Nokia_Application_servers_(BMC) range-address 10.65.100.8 to 10.65.100.10
set security address-book global address Nokia-App-5 description Nokia_Application_servers_(BMC) range-address 10.65.100.13 to 10.65.100.14
set security address-book global address Nokia-App-6 description Nokia_Application_servers_(BMC) range-address 10.65.100.21 to 10.65.100.23
set security address-book global address Remedy-AR description BMC-Remedy-AR_servers_IP_range range-address 10.65.251.6 to 10.65.251.10
set security address-book global address Remedy-mid description BMC-Remedy-Mid-tier_servers_IP_range range-address 10.65.251.11 to 10.65.251.14
set security address-book global address Entuity description BMC_Entuity_servers_IP_range range-address 10.65.253.4 to 10.65.253.7
set security address-book global address TSIM description BMC-TSIM_servers_IP_range range-address 10.65.254.4 to 10.65.254.14
set security address-book global address TSSA-1 description BMC-TSSA_servers_IP_range range-address 10.65.252.67 to 10.65.252.70
set security address-book global address TSSA-2 description BMC-TSSA_servers_IP_range range-address 10.65.252.75 to 10.65.252.76
set security address-book global address Discovery description BMC-Discovery_servers_IP_range range-address 10.65.252.5 to 10.65.252.7
set security address-book global address MSSQL-1 description BMC-MSSQL-DB_servers_IP_range range-address 10.65.250.4 to 10.65.250.8
set security address-book global address MSSQL-2 description BMC-MSSQL-DB_servers_IP_range range-address 10.65.250.10 to 10.65.250.11
set security address-book global address AD-1 description Active_directory_servers range-address 10.34.200.11 to 10.34.200.13
set security address-book global address AD-3 description Active_directory_servers range-address 10.34.200.46 to 10.34.200.47
set security address-book global address AD-4 description Active_directory_servers range-address 10.65.200.46 to 10.65.200.47
set security address-book global address CSTSSAVD02 10.65.252.75
set security address-book global address CSMIDTVD03 10.65.251.13
set security address-book global address CSTSISVD03 10.65.254.13
set security address-book global address CSMIDTVD04 10.65.251.14
set security address-book global address CSFODEPVD01Ext.CDCSSN.DC 10.65.100.5
set security address-book global address CSFOLBVD01Ext.CDCSSN.DC 10.65.100.6
set security address-book global address CSFOLBVD02Ext.CDCSSN.DC 10.65.100.7
set security address-book global address VIP-for-LBExt.CDCSSN.DC 10.65.100.4
set security address-book global address CSFOOMVD01Ext.CDCSSN.DC 10.65.100.8
set security address-book global address CSFOOMVD02Ext.CDCSSN.DC 10.65.100.9
set security address-book global address CSFOOMVD03Ext.CDCSSN.DC 10.65.100.10
set security address-book global address CSFOCATVD01Ext.CDCSSN.DC 10.65.100.11
set security address-book global address CSFOCATVD02Ext.CDCSSN.DC 10.65.100.12
set security address-book global address CSFOOAMVD01Ext.CDCSSN.DC 10.65.100.13
set security address-book global address CSFOOAMVD02Ext.CDCSSN.DC 10.65.100.14
set security address-book global address CSFOILCVD01Ext.CDCSSN.DC 10.65.100.16
set security address-book global address CSFOILCVD02Ext.CDCSSN.DC 10.65.100.17
set security address-book global address VIP-for-ILCExt.CDCSSN.DC 10.65.100.15
set security address-book global address CSFOARCVD01Ext.CDCSSN.DC 10.65.100.19
set security address-book global address CSFOARCVD02Ext.CDCSSN.DC 10.65.100.20
set security address-book global address VIP-for-ARCExt.CDCSSN.DC 10.65.100.18
set security address-book global address AV_UTIL_Server01 10.64.68.5
set security address-book global address AV_UTIL_Server02 10.64.68.10
set security address-book global address AV_UTIL_Server03 10.65.20.5
set security address-book global address AV_UTIL_Server04 10.65.20.10
set security address-book global address AV_UTIL_Server05 10.65.20.6
set security address-book global address AV_UTIL_Server06 10.65.20.7
set security address-book global address AV_UTIL_Server07 10.65.20.8
set security address-book global address AV_UTIL_Server08 10.65.20.9
set security address-book global address DD_System01 10.64.68.30
set security address-book global address DD_System02 10.64.68.31
set security address-book global address DD_System03 10.64.68.32
set security address-book global address DD_System04 10.65.20.30
set security address-book global address DD_System05 10.65.20.31
set security address-book global address DD_System06 10.65.20.34
set security address-book global address DD_System07 10.65.20.35
set security address-book global address DD_System08 10.65.20.38
set security address-book global address DD_System09 10.65.20.39
set security address-book global address DD_System10 10.65.20.42
set security address-book global address DD_System11 10.65.20.43
set security address-book global address DD_System12 10.65.20.46
set security address-book global address DD_System13 10.65.20.47
set security address-book global address DD_System14 10.65.20.50
set security address-book global address AV_SMTP01 10.65.204.63
set security address-book global address AV_SMTP02 10.65.200.52
set security address-book global address AV_SMTP03 10.65.200.53
set security address-book global address DD_IPMI01 10.64.17.30
set security address-book global address DD_IPMI02 10.64.17.31
set security address-book global address DD_IPMI03 10.64.17.32
set security address-book global address 10.64.17.7-12 range-address 10.64.17.7 to 10.64.17.12
set security address-book global address 10.65.254.8 10.65.254.8
set security address-book global address 10.65.254.9 10.65.254.9
set security address-book global address 10.65.254.10 10.65.254.10
set security address-book global address 10.65.254.11 10.65.254.11
set security address-book global address 10.65.254.12 10.65.254.12
set security address-book global address 10.65.254.13 10.65.254.13
set security address-book global address 10.65.254.5 10.65.254.5
set security address-book global address 10.65.253.5 10.65.253.5
set security address-book global address 10.65.254.7 10.65.254.7
set security address-book global address 10.65.252.5 10.65.252.5
set security address-book global address 10.65.254.4 10.65.254.4
set security address-book global address 10.65.254.6 10.65.254.6
set security address-book global address 10.65.252.75 10.65.252.75
set security address-book global address 10.65.252.69 10.65.252.69
set security address-book global address 10.65.250.6 10.65.250.6
set security address-book global address 10.65.250.8 10.65.250.8
set security address-book global address 10.65.253.4 10.65.253.4
set security address-book global address 10.65.252.67 10.65.252.67
set security address-book global address 10.65.250.4 10.65.250.4
set security address-book global address 10.65.250.5 10.65.250.5
set security address-book global address 10.65.252.68 10.65.252.68
set security address-book global address CSUIVWRKRVD01 10.65.90.12
set security address-book global address CSUIVWRKRVD02 10.65.90.13
set security address-book global address CSUIVWRKRVD03 10.65.90.14
set security address-book global address CSUIVWRKRVD04 10.65.90.15
set security address-book global address CSUIVWRKRVD05 10.65.90.16
set security address-book global address CSUIVWRKRVD06 10.65.90.17
set security address-book global address CSUIVWRKRVD07 10.65.90.18
set security address-book global address CSUIVWRKRVD08 10.65.90.19
set security address-book global address CSUIVWRKRVD09 10.65.90.20
set security address-book global address CSUIVWRKRVD10 10.65.90.21
set security address-book global address CSOHWRKRVD01 10.65.90.22
set security address-book global address CSOHWRKRVD02 10.65.90.23
set security address-book global address CSOHWRKRVD03 10.65.90.24
set security address-book global address 10.65.120.0-10.65.136.255 range-address 10.65.120.0 to 10.65.136.255
set security address-book global address 10.68.40.0_24 10.68.40.0/24
set security address-book global address PAM_Range 10.64.10.192/28
set security address-book global address RH-Management-Test 10.64.24.120
set security address-book global address 10.65.12.20 10.65.12.20
set security address-book global address 10.65.12.21 10.65.12.21/32
set security address-book global address 10.65.12.30 10.65.12.30
set security address-book global address 10.65.12.31 10.65.12.31
set security address-book global address IAM_Production_Range 10.64.10.208/29
set security address-book global address IAM_DB_Range 10.64.10.184/29
set security address-book global address Forcepoint_Mange_Range1 10.64.10.32/29
set security address-book global address Forcepoint_Mange_Range2 10.64.10.112/29
set security address-book global address RH-Cluster-Test range-address 10.64.43.9 to 10.64.43.10
set security address-book global address 10.65.124.4-28 range-address 10.65.124.4 to 10.65.124.28
set security address-book global description SFTP_Server address CSSFTPVD01 10.65.240.21
set security address-book global description SFTP_Server address CSSFTPVD02 10.65.240.22
set security address-book global description SFTP_Server address 10.65.240.20 10.65.240.20
set security address-book global address 10.215.195.0_24 10.215.195.0/24
set security address-book global address 10.64.10.48_29 10.64.10.48/29
set security address-book global address 10.64.43.0_25 10.64.43.0/25
set security address-book global address 10.64.10.0_28 10.64.10.0/28
set security address-book global address 10.64.10.16_29 10.64.10.16/29
set security address-book global address 10.64.10.24_29 10.64.10.24/29
set security address-book global address 10.64.10.40_29 10.64.10.40/29
set security address-book global description DB_Listener address LSCSREDBVD 10.65.250.12
set security address-book global address Infra_range 10.65.200.0/24
set security address-book global description CEP_Data_Base_Server address CEP_DB_failover 10.34.120.27
set security address-book global description Open_Data_Data_Base_Server address CEP_Open_Data__DB_failover 10.34.122.41
set security address-book global description Portal_Data_Base_Server address CEP_Portal_DB_failover 10.34.120.28
set security address-book global description CCP_GIS_QPN_Op_PostgreSQL address CCP_GIS_QPN_Op_PostgreSQL_failover 10.34.122.47
set security address-book global description CCP_GIS_QPN_Op_PostgreSQL address CCP_GIS_QPN_Op_PostgreSQL_sqlins 10.34.122.48
set security address-book global description CEP_Data_Base_Server address CEP_DB_sqlIns 10.34.120.26
set security address-book global description Open_Data_Data_Base_Server address CEP_Open_Data__DB_sqlIns 10.34.122.42
set security address-book global description Portal_Data_Base_Server address CEP_Portal_DB_sqlIns 10.34.120.29
set security address-book global description Load_balancer address LoadBalancer_External_QPN_VIP 10.34.121.13
set security address-book global description Load_Balancer-_External address LoadBalancer_External_DMZ_Cluster 10.32.16.6
set security address-book global description Load_Balancer-_External address LoadBalancer_External_DMZ_VIP 10.32.16.7
set security address-book global address SSN-Oracle-ExaAdmin 10.64.43.0/25
set security address-book global address SSN-Oracle-ExaSelfMon 10.64.47.0/28
set security address-book global address SSN-Oracle-ClientProd 10.65.40.16/28
set security address-book global address SSN-Oracle-ClientProd2 10.65.40.0/28
set security address-book global address SSN-Oracle-Bkup 10.65.41.0/28
set security address-book global address 10.65.13.6 10.65.13.6
set security address-book global address 10.65.13.4 10.65.13.4
set security address-book global address 10.65.13.5 10.65.13.5
set security address-book global address 10.65.200.0/24 10.65.200.0/24
set security address-book global address 10.65.210.0/24 10.65.210.0/24
set security address-book global address 10.65.13.0/24 10.65.13.0/24
set security address-book global address 10.65.204.0/24 10.65.204.0/24
set security address-book global address 10.65.40.9-11 range-address 10.65.40.9 to 10.65.40.11
set security address-book global address 10.65.22.14_Isilon 10.65.22.14
set security address-book global address 10.65.123.6-17 range-address 10.65.123.6 to 10.65.123.17
set security address-book global address 10.65.124.4-19 range-address 10.65.124.4 to 10.65.124.19
set security address-book global description Application_Server-_Data_Collection address ADMS_Data_collection_Cluster 10.65.121.16
set security address-book global description Application_Server-_OMS address ADMS_Data_OMS_Cluster 10.65.121.17
set security address-book global description Application_Server-_DMS address ADMS_Data_DMS_Cluster 10.65.121.18
set security address-book global description CEP_Engine address CCP_CEP_Engine_Cluster 10.65.124.25
set security address-book global description GIS_-_GIS_Application_Server address CCP_GIS_App_cluster 10.65.124.27
set security address-book global description IoT_Ops address CCP_IoTOPs_Cluster 10.65.124.26
set security address-book global description CCP_Application___Administration_Server_Software address CCP_APP_administration_Cluster 10.65.126.10
set security address-book global description Dashboard___Report_Server address CCP_Dashboard_Report_Cluster 10.65.126.11
set security address-book global description Application_Server address CCP_E_P_APP_Server_Cluster 10.65.127.8
set security address-book global description Identity/key_management_server address CCP_key_management_cluster 10.65.124.28
set security address-book global description PowerBI_Report_Server address CCP_PowerBI_Report_failover 10.65.125.15
set security address-book global description Application_Server-_Historian/Archive address ADMS_Historian_Failover 10.65.121.19
set security address-book global description Database_Server address AMI_Connexo_DB_Failover 10.65.123.18
set security address-book global description CCP_Database_Server_Software address CCP_DB_Failover 10.65.126.12
set security address-book global description Parking___Lighting_Server_Software address CCP_Parking_Lighting_Failover 10.65.127.9
set security address-book global description Analytics_Engine_Server_(SSAS___SSIS) address CCP_Analytics_Engine_Failover 10.68.40.17
set security address-book global description Platform_Database_Server_Software address CCP_Platform_Database_Failover 10.68.40.25
set security address-book global description GIS_-_GIS_Database_Server address CCP_GIS_DB_Failover 10.68.40.23
set security address-book global description PowerBI_Report_Server address CCP_PowerBI_Report_sqlins 10.65.125.16
set security address-book global description Application_Server-_Historian/Archive address ADMS_Historian_SqlIns 10.65.121.20
set security address-book global description Database_Server address AMI_Connexo_DB_SqlIns 10.65.123.19
set security address-book global description CCP_Database_Server_Software address CCP_DB_SqlIns 10.65.126.13
set security address-book global description Parking___Lighting_Database_Server address CCP_Parking_Lighting_SqlIns 10.65.127.10
set security address-book global description Analytics_Engine_Server_(SSAS___SSIS) address CCP_Analytics_Engine_SqlIns 10.68.40.18
set security address-book global description Platform_Database_Server_Software address CCP_Platform_Database_SqlIns 10.68.40.26
set security address-book global description GIS_-_GIS_Database_Server address CCP_GIS_DB_SqlIns 10.68.40.24
set security address-book global description Load_balancer-_internal address CCPP_Loadbalancer_Cluster 10.65.130.6
set security address-book global description Load_balancer-_internal address CCPP_Loadbalancer_VIP 10.65.130.7
set security address-book global address 10.65.130.4-7 range-address 10.65.130.4 to 10.65.130.7
set security address-book global address 10.65.124.4-7 range-address 10.65.124.4 to 10.65.124.7
set security address-book global address 10.65.13.0_24 10.65.13.0/24
set security address-book global address SIEM_Eventprocessor description SIEM_Event_processor range-address 10.64.10.227 to 10.64.10.232
set security address-book global address DDI_DNSDHCP description DDI_DNS_DHCP range-address 10.65.10.5 to 10.65.10.25
set security address-book global description DDI_PAM address DDI_PAM 10.64.10.176/29
set security address-book global description SSN_NFS_GroupNet_for_Client_#1__(Etisalat) address ISI_AccessZone_1 10.65.22.0/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#2 address ISI_AccessZone_2 10.65.22.16/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#3 address ISI_AccessZone_3 10.65.22.32/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#4 address ISI_AccessZone_4 10.65.22.48/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#5 address ISI_AccessZone_5 10.65.22.64/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#6 address ISI_AccessZone_6 10.65.22.80/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#7 address ISI_AccessZone_7 10.65.22.96/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#8 address ISI_AccessZone_8 10.65.22.112/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#9 address ISI_AccessZone_9 10.65.22.128/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#10 address ISI_AccessZone_10 10.65.22.144/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#11 address ISI_AccessZone_11 10.65.22.160/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#12 address ISI_AccessZone_12 10.65.22.176/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#13 address ISI_AccessZone_13 10.65.22.192/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#14 address ISI_AccessZone_14 10.65.22.208/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#15 address ISI_AccessZone_15 10.65.22.224/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#16 address ISI_AccessZone_16 10.65.22.240/28
set security address-book global description SSN_NFS_GroupNet_for_Client_#17 address ISI_Node_1 10.64.70.32
set security address-book global description SSN_NFS_GroupNet_for_Client_#18 address ISI_Node_2 10.64.70.33
set security address-book global description SSN_NFS_GroupNet_for_Client_#19 address ISI_Node_3 10.64.70.34
set security address-book global description SSN_NFS_GroupNet_for_Client_#20 address ISI_Node_4 10.64.70.35
set security address-book global address 10.65.23.0/29 10.65.23.0/29
set security address-book global address 10.65.23.8/29 10.65.23.8/29
set security address-book global address 10.65.22.5-14 range-address 10.65.22.5 to 10.65.22.14
set security address-book global address 10.68.0.0_16 10.68.0.0/16
set security address-book global address 10.215.0.0_16 10.215.0.0/16
set security address-book global address CSNCSVD01-EDG1EXT-CDCSSN-DC 10.65.110.21
set security address-book global address CSNCSVD01-EDG2EXT-CDCSSN-DC 10.65.110.22
set security address-book global address CSCCFACUD.CDCSSN.DC 10.65.110.29
set security address-book global address Beacon_UI 10.65.90.5
set security address-book global address 10.65.125.4-5 range-address 10.65.125.4 to 10.65.125.5
set security address-book global address Network-1 range-address 10.64.9.11 to 10.64.9.13
set security address-book global address Network-2 range-address 10.64.9.21 to 10.64.9.22
set security address-book global address Network-3 range-address 10.64.9.201 to 10.64.9.206
set security address-book global address Network-4 range-address 10.64.9.101 to 10.64.9.112
set security address-book global address Network-5 range-address 10.64.18.11 to 10.64.18.13
set security address-book global address Network-6 range-address 10.64.18.21 to 10.64.18.22
set security address-book global address Network-7 range-address 10.64.18.201 to 10.64.18.206
set security address-book global address Trilio-Src1 range-address 10.64.20.251 to 10.64.20.253
set security address-book global address Trilio-Src2 range-address 10.65.20.251 to 10.65.20.253
set security address-book global address 10.64.43.1-126 range-address 10.64.43.1 to 10.64.43.126
set security address-book global address 10.64.47.1-14 range-address 10.64.47.1 to 10.64.47.14
set security address-book global address 10.215.195.61-70 range-address 10.215.195.61 to 10.215.195.70
set security address-book global address 10.64.10.224_28 10.64.10.224/28
set security address-book global address CSTSISVD04 10.65.254.14
set security address-book global address Network-8 range-address 10.64.18.101 to 10.64.18.112
set security address-book global address Nokia-1 range-address 10.65.90.6 to 10.65.90.11
set security address-book global address Nokia-2 range-address 10.65.65.5 to 10.65.65.9
set security address-book global address Nokia-3 range-address 10.68.1.68 to 10.68.1.70
set security address-book global address Nokia-4 range-address 10.65.110.5 to 10.65.110.118
set security address-book global address Nokia-5 range-address 10.65.90.12 to 10.65.90.21
set security address-book global address Nokia-6 range-address 10.65.90.22 to 10.65.90.24
set security address-book global address 10.215.193.0_24 10.215.193.0/24
set security address-book global address Iscasi1 10.65.123.5
set security address-book global address Iscasi2 10.65.123.6
set security address-book global address Iscasi3 10.65.123.13
set security address-book global address Iscasi4 10.65.123.14
set security address-book global description CCP_GIS_SSN_Op_PostgreSQL address CCP_GIS_SSN_Op_PostgreSQL_failover 10.65.131.22
set security address-book global description CCP_GIS_SSN_Op_PostgreSQL address CCP_GIS_SSN_Op_PostgreSQL_sqlins 10.65.131.23
set security address-book global address 10.65.123.4-17 range-address 10.65.123.4 to 10.65.123.17
set security address-book global address 10.68.40.4-14 range-address 10.68.40.4 to 10.68.40.14
set security address-book global address 10.34.121.4-20 range-address 10.34.121.4 to 10.34.121.20
set security address-book global address 10.34.122.4-46 range-address 10.34.122.4 to 10.34.122.46
set security address-book global address CCPP_Load_balancer_cluster 10.65.130.6
set security address-book global address CCPP_Load_balancer_vip 10.65.130.7
set security address-book global address CCP_APP_Server_cluster 10.65.127.8
set security address-book global description Load_balancer address LoadBalancer_External_QPN_Cluster 10.34.121.12
set security address-book global description Load_Balancer-_External address LoadBalancer_External_DMZ_Floating 10.32.16.6
set security address-book global description Load_Balancer-_External address LoadBalancer_External_DMZ_01 10.32.16.4
set security address-book global description Load_Balancer-_External address LoadBalancer_External_DMZ_02 10.32.16.5
set security address-book global description Load_balancer address LoadBalancer_External_QPN_01 10.34.121.6
set security address-book global description Load_balancer address LoadBalancer_External_QPN_02 10.34.121.7
set security address-book global description CEP_Application_Server address CEP_APP_Server_Cluster 10.34.120.25
set security address-book global description MEAP_Application_server address CEP_MEAPApplication_Cluster 10.34.121.14
set security address-book global description Notification_Server address CEP_Notification_Cluster 10.34.122.40
set security address-book global description Internal_Media_Server address CCP_InternalMedia_Cluster 10.34.121.15
set security address-book global address 10.64.12.0_24 10.64.12.0/24
set security address-book global address AR_LB1 10.65.13.14
set security address-book global address AR_LB2 10.65.13.15
set security address-book global address MIDTIER_LB1 10.65.13.16
set security address-book global address MIDTIER_LB2 10.65.13.17
set security address-book global address MSSQL-3 range-address 10.65.250.4 to 10.65.250.11
set security address-book global address Discovery-1 range-address 10.65.252.4 to 10.65.252.7
set security address-book global address Capacity range-address 10.65.251.67 to 10.65.251.68
set security address-book global address TSSA-3 range-address 10.65.252.67 to 10.65.252.75
set security address-book global description Intermediated_database_server_1 address CSIntDBVD01 10.65.240.6
set security address-book global description Intermediated_database_server_2 address CSIntDBVD02 10.65.240.7
set security address-book global description Intermediated_database_Cluster_IP address 10.65.240.8 10.65.240.8
set security address-book global description Intermediated_database_Listener_IP address 10.65.240.9 10.65.240.9
set security address-book global address 10.64.11.0_28 10.64.11.0/28
set security address-book global address 10.65.131.11-21 range-address 10.65.131.11 to 10.65.131.21
set security address-book global address CCP_GIS_SSN_PostgreSQL_VIP 10.65.13.18
set security address-book global address CCP_GIS_SSN_GEO_VIP 10.65.13.19
set security address-book global address CCP_GIS_SSN_manager_VIP 10.65.13.20
set security address-book global address CCP_SocialMed_App_01 10.65.125.4
set security address-book global address CCP_SocialMed_App_02 10.65.125.5
set security address-book global address AMI_Connexo_GUI_VIP 10.65.13.26
set security address-book global address AMI_Connexo_Communication_VIP 10.65.13.25
set security address-book global address AMI_Connexo_App_WS_VIP 10.65.13.24
set security address-book global address 10.64.9.13 10.64.9.13
set security address-book global address 10.64.9.201 10.64.9.201
set security address-book global address 10.64.9.101 10.64.9.101
set security address-book global address 10.64.10.65 10.64.10.65
set security address-book global address 10.64.10.26-27 range-address 10.64.10.26 to 10.64.10.27
set security address-book global address 10.65.8.4 10.65.8.4
set security address-book global address 10.215.195.71-75 range-address 10.215.195.71 to 10.215.195.75
set security address-book global address 10.64.10.72_29 10.64.10.72/29
set security address-book global address 10.64.10.168_29 10.64.10.168/29
set security address-book global address 10.64.10.136_29 10.64.10.136/29
set security address-book global address 10.64.10.160_29 10.64.10.160/29
set security address-book global address VDI_SSN_ESXI_MGMT01 10.64.67.5
set security address-book global address VDI_SSN_ESXI_MGMT02 10.64.67.10
set security address-book global address VDI_SSN_ESXI_MGMT03 10.64.67.15
set security address-book global address VDI_SSN_ESXI_MGMT04 10.64.67.20
set security address-book global address VDI_SSN_ESXI_VDI01 10.64.64.135
set security address-book global address VDI_SSN_ESXI_VDI02 10.64.64.140
set security address-book global address VDI_SSN_ESXI_VDI03 10.64.64.145
set security address-book global address VDI_SSN_ESXI_VDI04 10.64.64.150
set security address-book global address VDI_SSN_ESXI_VDI05 10.64.64.155
set security address-book global address VDI_SSN_ESXI_VDI06 10.64.64.160
set security address-book global address VDI_SSN_ESXI_VDI07 10.64.64.165
set security address-book global address VDI_SSN_ESXI_VDI08 10.64.64.170
set security address-book global address VDI_SSN_ESXI_VDI09 10.64.64.175
set security address-book global address VDI_SSN_ESXI_VDI10 10.64.64.180
set security address-book global address VDI_SSN_ESXI_VDI11 10.64.64.185
set security address-book global address VDI_SSN_ESXI_VDI12 10.64.64.190
set security address-book global address VDI_SSN_ESXI_VAPP01 10.64.64.200
set security address-book global address VDI_SSN_ESXI_VAPP02 10.64.64.205
set security address-book global address VDI_SSN_ESXI_VAPP03 10.64.64.210
set security address-book global address VDI_SSN_ESXI_CITRIX01 10.64.64.10
set security address-book global address VDI_SSN_ESXI_CITRIX02 10.64.64.15
set security address-book global address VDI_SSN_ESXI_VMCLOUD01 10.64.67.200
set security address-book global address VDI_SSN_ESXI_VMCLOUD02 10.64.67.205
set security address-book global address VDI_SSN_TS01 10.64.67.70
set security address-book global address VDI_SSN_TS02 10.64.67.75
set security address-book global address VDI_SSN_VCENTER01 10.65.48.10
set security address-book global address VDI_SSN_VROPS01 10.65.48.15
set security address-book global address VDI_SSN_VROPS_Replica01 10.65.48.20
set security address-book global address VDI_SSN_VROPS_Replica02 10.65.48.25
set security address-book global address VDI_SSN_STOREONCE_MGMT01 10.64.65.10
set security address-book global address VDI_SSN_RMC_STOREONCE_MGMT01 10.64.65.15
set security address-book global address VDI_SSN_PRIMERA_MGMT01 10.64.65.40
set security address-book global address VDI_SSN_SSMC_PRIMERA_MGMT01 10.64.65.50
set security address-book global address VDI_SSN_RMC_Primera_MGMT01 10.64.65.45
set security address-book global address Remedy-AR_VIP range-address 10.65.13.14 to 10.65.13.15
set security address-book global address Remedy-mid_VIP range-address 10.65.13.16 to 10.65.13.17
set security address-book global address Remedy_Ticketing_AR_server range-address 10.65.251.33 to 10.65.251.34
set security address-book global address Remedy_Ticketing_Mid_Tier range-address 10.65.251.27 to 10.65.251.28
set security address-book global address LoraWan_SRV 10.65.124.30
set security address-book global address 10.32.16.4-10 range-address 10.32.16.4 to 10.32.16.10
set security address-book global address 10.64.9.0_24 10.64.9.0/24
set security address-book global address 10.65.254.14 10.65.254.14
set security address-book global address CCP_IoTOPs_APP_Cluster 10.65.124.46
set security address-book global address CCP_Dashboard_Report_App_Cluster 10.65.126.21
set security address-book global address CCP_APP_administration_APP_Cluster 10.65.126.20
set security address-book global address GCC_Datacenter description External-GCC_integration range-address 10.251.9.25 to 10.251.9.26
set security address-book global description External_-_FMC_integration address FMC_Datacenter NA
set security address-book global address CCC-Datacenter description External_-_CCC_integration range-address 10.1.21.45 to 10.1.21.48
set security address-book global address 10.64.11.16_29 10.64.11.16/29
set security address-book global address SSN-SFTP range-address 10.65.8.24 to 10.65.8.25
set security address-book global address SSN-EP0101 10.64.12.50
set security address-book global address SSN-EP0102 10.64.12.52
set security address-book global address SSN-EP0201 10.64.12.56
set security address-book global address SSN-EP0202 10.64.12.58
set security address-book global address SSN-EP01-VIP 10.64.12.51
set security address-book global address SSN-EP02-VIP 10.64.12.55
set security address-book global address 10.64.10.160_29 10.64.10.160/29
set security address-book global description Load_Balancer_internal_SSN address LB_I_SSN 10.65.130.0/24
set security address-book global description Load_Balancer_internal_QPN address LB_I_QPN 10.34.121.0/24
set security address-book global description Load_Balancer_External_DMZ address LB_E_DMZ 10.32.16.0/24
set security address-book global description CEP_Application_QPN_Core address CEP_QPN 10.34.120.0/24
set security address-book global description CCP_Application_QPN_Core address CCP_QPN 10.34.121.0/24
set security address-book global description CEP_&_GIS_Application_QPN_Core address CEP___GIS_QPN 10.34.122.0/24
set security address-book global description CCP_Platform_Application_SSN_Core address CCP_Platform_SSN 10.65.124.0/24
set security address-book global description Social_Media_Citizen_Sentiment_Analytics_Application_Server address SocialMed_App_SSN 10.65.125.0/24
set security address-book global description CCP_Dashboard_&_ML address CCP_BI_ML_SSN 10.65.125.0/24
set security address-book global description CCP_Platform_Database_SSN address CCP_DB_SSN 10.65.126.0/24
set security address-book global description CCP_Energy_&_Parking_Applications address CCP_App_SSL_SP_SSN 10.65.127.0/24
set security address-book global description CCP_Deployment_SSN address CCP_deployment_SSN 10.65.128.0/24
set security address-book global description GIS_Application address CCP_GIS_SSN 10.65.131.0/24
set security address-book global description CCP_Big_Data address CCP_BIG_DB_SSN 10.68.40.0/24
set security address-book global description ERP address ERP_System 10.65.136.0/24
set security address-book global address CRM_System description CRM range-address 10.34.28.5 to 10.34.28.6
set security address-book global address Billing_System range-address 10.34.28.5 to 10.34.28.24
set security address-book global address sFTP_for_DG_FW 10.65.8.16/28
set security address-book global address sFTP_Nokia_ITSM_iDB 10.65.240.16/28
set security address-book global address Smart_Parking-NN1 10.95.64.0/19
set security address-book global address Smart_Parking-NN2 10.95.64.0/21
set security address-book global address Smart_Parking-NN4 10.95.72.0/21
set security address-book global address Smart_Parking-NN5 10.95.80.0/22
set security address-book global address Smart_Parking-NN6 10.95.84.0/22
set security address-book global address Smart_Parking-NN7 10.95.88.0/22
set security address-book global address Smart_Parking-NN8 10.95.92.0/22
set security address-book global address Water_meter-NN1 10.80.0.0/17
set security address-book global address Water_meter-NN2 10.80.128.0/17
set security address-book global address Water_meter-NN4 10.81.0.0/18
set security address-book global address Water_meter-NN5 10.81.64.0/18
set security address-book global address Water_meter-NN7 10.81.128.0/18
set security address-book global address Water_meter-NN8 10.81.192.0/18
set security address-book global address irrigation_meter-NN1 10.88.0.0/18
set security address-book global address irrigation_meter-NN2 10.88.64.0/18
set security address-book global address irrigation_meter-NN4 10.88.128.0/19
set security address-book global address irrigation_meter-NN5 10.88.160.0/19
set security address-book global address irrigation_meter-NN7 10.88.192.0/19
set security address-book global address irrigation_meter-NN8 10.88.224.0/19
set security address-book global address Electricity_meter-NN1 10.82.0.0/17
set security address-book global address Electricity_meter-NN2 10.82.128.0/17
set security address-book global address Electricity_meter-NN4 10.83.0.0/18
set security address-book global address Electricity_meter-NN5 10.83.64.0/18
set security address-book global address Electricity_meter-NN7 10.83.128.0/18
set security address-book global address Electricity_meter-NN8 10.83.192.0/18
set security address-book global address Gas_meter-NN1 10.84.0.0/17
set security address-book global address Gas_meter-NN2 10.84.128.0/17
set security address-book global address Gas_meter-NN4 10.85.0.0/18
set security address-book global address Gas_meter-NN5 10.85.64.0/18
set security address-book global address Gas_meter-NN7 10.85.128.0/18
set security address-book global address Gas_meter-NN8 10.85.192.0/18
set security address-book global address AMI_Connexo_Communication_01 10.65.123.11/32
set security address-book global address AMI_Connexo_Communication_02 10.65.123.12/32
set security address-book global address AMI_Connexo_Communication_03 10.65.123.13/32
set security address-book global address AMI_Connexo_Communication_04 10.65.123.14/32
set security address-book global address AMI_Connexo_Communication_05 10.65.123.15/32
set security address-book global address Container-NN1 10.95.0.0/21
set security address-book global address Container-NN2 10.95.8.0/21
set security address-book global address Container-NN4 10.95.16.0/22
set security address-book global address Container-NN5 10.95.20.0/22
set security address-book global address Container-NN7 10.95.24.0/22
set security address-book global address Container-NN8 10.95.28.0/22
set security address-book global address Street_lights-NN1 10.94.0.0/19
set security address-book global address Street_lights-NN2 10.94.32.0/19
set security address-book global address Street_lights-NN4 10.94.64.0/20
set security address-book global address Street_lights-NN5 10.94.80.0/20
set security address-book global address Street_lights-NN7 10.94.96.0/20
set security address-book global address Street_lights-NN8 10.94.112.0/20
set security address-book global address CCPP_Loadbalancer_01 10.65.130.4/32
set security address-book global address CCPP_Loadbalancer_02 10.65.130.5/32
set security address-book global address CCPP_Loadbalancer_Cluster 10.65.130.6/32
set security address-book global address CCPP_Loadbalancer_VIP 10.65.130.7/32
set security address-book global address Air_quality_devices-NN1 10.95.96.0/21
set security address-book global address Air_quality_devices-NN2 10.95.104.0/21
set security address-book global address Air_quality_devices-NN4 10.95.112.0/22
set security address-book global address Air_quality_devices-NN5 10.95.116.0/22
set security address-book global address Air_quality_devices-NN7 10.95.120.0/22
set security address-book global address Air_quality_devices-NN8 10.95.124.0/22
set security address-book global address Bicycle_flow_devices-NN1 10.95.160.0/21
set security address-book global address Bicycle_flow_devices-NN2 10.95.168.0/21
set security address-book global address Bicycle_flow_devices-NN4 10.95.176.0/22
set security address-book global address Bicycle_flow_devices-NN5 10.95.180.0/22
set security address-book global address Bicycle_flow_devices-NN7 10.95.184.0/22
set security address-book global address Bicycle_flow_devices-NN8 10.95.188.0/22
set security address-book global address People_flow_devices-NN1 10.95.192.0/22
set security address-book global address People_flow_devices-NN2 10.95.196.0/22
set security address-book global address People_flow_devices-NN4 10.95.200.0/23
set security address-book global address People_flow_devices-NN5 10.95.202.0/23
set security address-book global address People_flow_devices-NN7 10.95.204.0/23
set security address-book global address People_flow_devices-NN8 10.95.206.0/23
set security address-book global address Traffic_devices-NN1 10.95.208.0/22
set security address-book global address Traffic_devices-NN2 10.95.212.0/22
set security address-book global address Traffic_devices-NN4 10.95.216.0/23
set security address-book global address Traffic_devices-NN5 10.95.218.0/23
set security address-book global address Traffic_devices-NN7 10.95.220.0/23
set security address-book global address Traffic_devices-NN8 10.95.222.0/23
set security address-book global address Weather_devices-NN1 10.95.224.0/22
set security address-book global address Weather_devices-NN2 10.95.228.0/22
set security address-book global address Weather_devices-NN4 10.95.232.0/23
set security address-book global address Weather_devices-NN5 10.95.234.0/23
set security address-book global address Weather_devices-NN7 10.95.236.0/23
set security address-book global address Weather_devices-NN8 10.95.238.0/23
set security address-book global address Noise_devices-NN1 10.95.240.0/22
set security address-book global address Noise_devices-NN2 10.95.244.0/22
set security address-book global address Noise_devices-NN4 10.95.248.0/23
set security address-book global address Noise_devices-NN5 10.95.250.0/23
set security address-book global address Noise_devices-NN7 10.95.252.0/23
set security address-book global address Noise_devices-NN8 10.95.254.0/23
set security address-book global address Cameras_installed-NN1 10.86.0.0/17
set security address-book global address Cameras_installed-NN2 10.86.128.0/17
set security address-book global address Cameras_installed-NN4 10.87.0.0/18
set security address-book global address Cameras_installed-NN5 10.87.64.0/18
set security address-book global address Cameras_installed-NN7 10.87.128.0/18
set security address-book global address Cameras_installed-NN8 10.87.192.0/18
set security address-book global address Cameras_analytics-NN1 10.89.0.0/18
set security address-book global address Cameras_analytics-NN2 10.89.64.0/18
set security address-book global address Cameras_analytics-NN4 10.89.128.0/19
set security address-book global address Cameras_analytics-NN5 10.89.160.0/19
set security address-book global address Cameras_analytics-NN7 10.89.192.0/19
set security address-book global address Cameras_analytics-NN8 10.89.224.0/19
set security address-book global address Station_CCTV_-NN1 10.95.128.0/21
set security address-book global address Station_CCTV_-NN2 10.95.136.0/21
set security address-book global address Station_CCTV_-NN4 10.95.144.0/22
set security address-book global address Station_CCTV_-NN5 10.95.148.0/22
set security address-book global address Station_CCTV_-NN7 10.95.152.0/22
set security address-book global address Station_CCTV_-NN8 10.95.156.0/22
set security address-book global address Pole_package-NN1 10.94.128.0/19
set security address-book global address Pole_package-NN2 10.94.160.0/19
set security address-book global address Pole_package-NN4 10.94.192.0/20
set security address-book global address Pole_package-NN5 10.94.208.0/20
set security address-book global address Pole_package-NN7 10.94.224.0/20
set security address-book global address Pole_package-NN8 10.94.240.0/20
set security address-book global address UPS_Smart_pole-NN1 10.91.64.0/20
set security address-book global address UPS_Smart_pole-NN2 10.91.80.0/20
set security address-book global address UPS_Smart_pole-NN4 10.91.96.0/21
set security address-book global address UPS_Smart_pole-NN5 10.91.104.0/21
set security address-book global address UPS_Smart_pole-NN7 10.91.112.0/21
set security address-book global address UPS_Smart_pole-NN8 10.91.120.0/21
set security address-book global address Pole_package_Digital_Signage_-NN1 10.91.0.0/20
set security address-book global address Pole_package_Digital_Signage_-NN2 10.91.16.0/20
set security address-book global address Pole_package_Digital_Signage_-NN4 10.91.32.0/21
set security address-book global address Pole_package_Digital_Signage_-NN5 10.91.40.0/21
set security address-book global address Pole_package_Digital_Signage_-NN7 10.91.48.0/21
set security address-book global address Pole_package_Digital_Signage_-NN8 10.91.56.0/21
set security address-book global address Water_Grid-NN1 10.91.128.0/19
set security address-book global address Water_Grid-NN2 10.91.160.0/19
set security address-book global address Water_Grid-NN4 10.91.192.0/20
set security address-book global address Water_Grid_-NN5 10.91.208.0/20
set security address-book global address Water_Grid_-NN7 10.91.224.0/20
set security address-book global address Water_Grid_-NN8 10.91.240.0/20
set security address-book global address Irrigation_Grid-NN1 10.92.0.0/19
set security address-book global address Irrigation_Grid-NN2 10.92.32.0/19
set security address-book global address Irrigation_Grid-NN4 10.92.64.0/20
set security address-book global address Irrigation_Grid-NN5 10.92.80.0/20
set security address-book global address Irrigation_Grid-NN7 10.92.96.0/20
set security address-book global address Irrigation_Grid-NN8 10.92.112.0/20
set security address-book global address Electricity_Grid-NN1 10.92.128.0/19
set security address-book global address Electricity_Grid-NN2 10.92.160.0/19
set security address-book global address Electricity_Grid-NN4 10.92.192.0/20
set security address-book global address Electricity_Grid-NN5 10.92.208.0/20
set security address-book global address Electricity_Grid-NN7 10.92.224.0/20
set security address-book global address Electricity_Grid-NN8 10.92.240.0/20
set security address-book global address Gas_Grid-NN1 10.93.0.0/19
set security address-book global address Gas_Grid-NN2 10.93.32.0/19
set security address-book global address Gas_Grid-NN4 10.93.64.0/20
set security address-book global address Gas_Grid-NN5 10.93.80.0/20
set security address-book global address Gas_Grid-NN7 10.93.96.0/20
set security address-book global address Gas_Grid-NN8 10.93.112.0/20
set security address-book global address BMS_Monitor_Point-NN1 10.90.0.0/18
set security address-book global address BMS_Monitor_Point-NN2 10.90.64.0/18
set security address-book global address BMS_Monitor_Point-NN4 10.90.128.0/19
set security address-book global address BMS_Monitor_Point-NN5 10.90.160.0/19
set security address-book global address BMS_Monitor_Point-NN7 10.90.192.0/19
set security address-book global address BMS_Monitor_Point-NN8 10.90.224.0/19
set security address-book global address Access_Control_Reader-NN1 10.93.128.0/19
set security address-book global address Access_Control_Reader-NN2 10.93.160.0/19
set security address-book global address Access_Control_Reader-NN4 10.93.192.0/20
set security address-book global address Access_Control_Reader-NN5 10.93.208.0/20
set security address-book global address Access_Control_Reader-NN7 10.93.224.0/20
set security address-book global address Access_Control_Reader-NN8 10.93.240.0/20
set security address-book global address Facility_Management_-NN1 10.95.32.0/21
set security address-book global address Facility_Management_-NN2 10.95.40.0/21
set security address-book global address Facility_Management_-NN4 10.95.48.0/22
set security address-book global address Facility_Management_-NN5 10.95.52.0/22
set security address-book global address Facility_Management_-NN7 10.95.56.0/22
set security address-book global address Facility_Management_-NN8 10.95.60.0/22
set security address-book global address SSN-Navori01 10.65.132.11/32
set security address-book global address SSN-Navori02 10.65.132.12/32
set security address-book global address Navori-QL-4 10.65.132.14/32
set security address-book global address Navori-QL-5 10.65.132.15/32
set security address-book global address SCADA_Water_Server_A 10.65.120.17/32
set security address-book global address SCADA_Water_Server_B 10.65.120.18/32
set security address-book global address SCADA_Electrical_Server_A 10.65.120.15/32
set security address-book global address SCADA_Electrical_Server_B 10.65.120.16/32
set security address-book global address SCADA_Gas_Server_A 10.65.120.14/32
set security address-book global address SCADA_Gas_Server_B 10.65.120.19/32
set security address-book global address Smart_meters 10.254.22.0/23
set security address-book global address IoT_gateway 10.254.30.0/23
set security address-book global address SCADA_Electrical 10.254.26.0/23
set security address-book global address 10.34.251.11-14 range-address 10.34.251.11 to 10.34.251.14
set security address-book global address ITSM_G_1 range-address 10.65.251.6 to 10.65.251.14
set security address-book global address ITSM_G_2 range-address 10.65.253.4 to 10.65.253.5
set security address-book global address ITSM_G_3 range-address 10.65.251.67 to 10.65.251.68
set security address-book global address ITSM_G_4 range-address 10.65.252.67 to 10.65.252.75
set security address-book global address ITSM_G_5 range-address 10.65.250.4 to 10.65.252.16
set security address-book global address ITSM_G_6 range-address 10.65.252.4 to 10.65.252.5
set security address-book global address ITSM_G_7 range-address 10.65.254.4 to 10.65.254.14
set security address-book global address CSTSDBVD02 10.65.250.10
set security address-book global address CSTSDBVD03 10.65.250.11
set security address-book global address 10.20.54.8 10.20.54.8
set security address-book global address 10.20.54.9 10.20.54.9
set security address-book global address 10.20.54.17 10.20.54.17
set security address-book global address 10.20.54.18 10.20.54.18
set security address-book global address 10.20.53.5 10.20.53.5
set security address-book global address 10.20.53.9 10.20.53.9
set security address-book global address 10.65.110.5 10.65.110.5
set security address-book global address 10.65.110.6 10.65.110.6
set security address-book global address 10.65.110.7 10.65.110.7
set security address-book global address 10.65.110.8 10.65.110.8
set security address-book global address 10.65.110.9 10.65.110.9
set security address-book global address 10.65.110.10 10.65.110.10
set security address-book global address 10.65.110.11 10.65.110.11
set security address-book global address 10.65.110.12 10.65.110.12
set security address-book global address 10.65.110.13 10.65.110.13
set security address-book global address 10.65.110.14 10.65.110.14
set security address-book global address 10.65.110.15 10.65.110.15
set security address-book global address 10.65.110.16 10.65.110.16
set security address-book global address 10.65.110.17 10.65.110.17
set security address-book global address 10.65.110.18 10.65.110.18
set security address-book global address CSFODEPVD01Ext.CDCSSN.DC 10.65.100.5
set security address-book global address CSFOLBVD01Ext.CDCSSN.DC 10.65.100.6
set security address-book global address CSFOLBVD02Ext.CDCSSN.DC 10.65.100.7
set security address-book global address 10.65.100.8 10.65.100.8
set security address-book global address CSFOOMVD02Ext.CDCSSN.DC 10.65.100.9
set security address-book global address CSFOOMVD03Ext.CDCSSN.DC 10.65.100.10
set security address-book global address CSFOCATVD01Ext.CDCSSN.DC 10.65.100.11
set security address-book global address CSFOCATVD02Ext.CDCSSN.DC 10.65.100.12
set security address-book global address 10.65.100.13 10.65.100.13
set security address-book global address CSFOOAMVD02Ext.CDCSSN.DC 10.65.100.14
set security address-book global address CSFOILCVD01Ext.CDCSSN.DC 10.65.100.16
set security address-book global address CSFOILCVD02Ext.CDCSSN.DC 10.65.100.17
set security address-book global address CSFOARCVD01Ext.CDCSSN.DC 10.65.100.19
set security address-book global address CSFOARCVD02Ext.CDCSSN.DC 10.65.100.20
set security address-book global address CCP_GIS_SSN_GEO_VIP 10.65.13.19
set security address-book global address 10.65.85.5 10.65.85.5
set security address-book global address 10.65.85.6 10.65.85.6
set security address-book global address 10.65.85.7 10.65.85.7
set security address-book global address 10.65.85.8 10.65.85.8
set security address-book global address 10.65.85.9 10.65.85.9
set security address-book global address 10.65.85.37 10.65.85.37
set security address-book global address 10.65.85.38 10.65.85.38
set security address-book global address 10.65.85.39 10.65.85.39
set security address-book global address 10.65.85.40 10.65.85.40
set security address-book global address 10.65.85.41 10.65.85.41
set security address-book global address CSCBOVMDSD01 10.65.65.5
set security address-book global address CSCBOGSST01 10.65.65.6
set security address-book global address CSCBOINTD01 10.65.65.7
set security address-book global address CSCBOJOBD01 10.65.65.8
set security address-book global address CSCBOTSD01 10.65.65.9
set security address-book global address CCPP_Loadbalancer_VIP 10.65.130.7
set security address-book global description DB_Listener address LSCSREDBVD 10.65.250.12
set security address-book global address AR_LB1 10.65.13.14
set security address-book global address AR_LB2 10.65.13.15
set security address-book global address Remedy_Ticketing_Mid_Tier range-address 10.65.251.27 to 10.65.251.28
set security address-book global address 10.65.251.25 10.65.251.25
set security address-book global address 10.65.251.26 10.65.251.26
set security address-book global address 10.65.251.31 10.65.251.31
set security address-book global address 10.65.251.32 10.65.251.32
set security address-book global address 10.65.251.29 10.65.251.29
set security address-book global address 10.65.251.30 10.65.251.30
set security address-book global address 10.64.11.0_28 10.64.11.0/28
set security address-book global address 10.33.11.22 10.33.11.22
set security address-book global address 10.64.10.168_29 10.64.10.168/29
set security address-book global address 10.33.11.4 10.33.11.4
set security address-book global address SSN-EP0101 10.64.12.50
set security address-book global address SSN-EP0102 10.64.12.52
set security address-book global address SSN-EP0201 10.64.12.56
set security address-book global address SSN-EP0202 10.64.12.58
set security address-book global address SSN-EP01-VIP 10.64.12.51
set security address-book global address SSN-EP02-VIP 10.64.12.55
set security address-book global address 10.33.7.50 10.33.7.50
set security address-book global address 10.33.10.64_29 10.33.10.64/29
set security address-book global address 10.64.10.65 10.64.10.65
set security address-book global address 10.64.10.74 10.64.10.74
set security address-book global address 10.65.251.33 10.65.251.33
set security address-book global address 10.65.251.34 10.65.251.34
set security address-book global address 10.65.251.35 10.65.251.35
set security address-book global address CQDR-db0.VD.CDCQPN.DC 10.34.23.5
set security address-book global address CQDR-db1.VD.CDCQPN.DC 10.34.23.6
set security address-book global address CQDR-dbvip.VD.CDCQPN.DC 10.34.23.7
set security address-book global address CQDR-ui1.VD.CDCQPN.DC 10.34.23.8
set security address-book global address CQDR-uivip.VD.CDCQPN.DC 10.34.23.10
set security address-book global address CQDR-procon11.VD.CDCQPN.DC 10.34.23.11
set security address-book global address CQDR-procoff00.VD.CDCQPN.DC 10.34.23.12
set security address-book global address CQDR-procoff11.VD.CDCQPN.DC 10.34.23.13
set security address-book global address CQDR-procoffvip.VD.CDCQPN.DC 10.34.23.15
set security address-book global address CQDR-oam1.VD.CDCQPN.DC 10.34.23.16
set security address-book global address CQCPASVD01EXT.CDCQPN.DC 10.34.28.5
set security address-book global address CQCPASVD02EXT.CDCQPN.DC 10.34.28.6
set security address-book global address CQCPRMVD01EXT.CDCQPN.DC 10.34.28.7
set security address-book global address CQCPRMVD02EXT.CDCQPN.DC 10.34.28.8
set security address-book global address CQEPCPASVD01EXT.CDCQPN.DC 10.34.28.9
set security address-book global address CQEPCPASVD02EXT.CDCQPN.DC 10.34.28.10
set security address-book global address CQCPODBVD01EXT.CDCQPN.DC 10.34.28.11
set security address-book global address CQCPODBVD02EXT.CDCQPN.DC 10.34.28.12
set security address-book global address CQCPOSVD01EXT.CDCQPN.DC 10.34.28.13
set security address-book global address CQCPOSVD02EXT.CDCQPN.DC 10.34.28.14
set security address-book global address CQCPIMVD01EXT.CDCQPN.DC 10.34.28.15
set security address-book global address CQCPTSVD01EXT.CDCQPN.DC 10.34.28.16
set security address-book global address CQCPTSVD02EXT.CDCQPN.DC 10.34.28.17
set security address-book global address CQCPBSVD01EXT.CDCQPN.DC 10.34.28.18
set security address-book global address CQCPBSVD02EXT.CDCQPN.DC 10.34.28.19
set security address-book global address CQCHAPROXYD01EXT.CDCQPN.DC 10.34.28.20
set security address-book global address CQCHAPROXYD02EXT.CDCQPN.DC 10.34.28.21
set security address-book global address CQCANSIBLED01EXT.CDCQPN.DC 10.34.28.22
set security address-book global address CSCNIPWDBVD01EXT.CDCQPN.DC 10.34.28.24
set security address-book global address CRM.EXTVIP.CDCQPN.DC 10.34.28.23
set security address-book global address CQMIDTVD03 10.34.251.13
set security address-book global address CQMIDTVD04 10.34.251.14
set security address-book global address CQFODEPVD01Ext.CDCQPN.DC 10.34.100.5
set security address-book global address CQFOLBVD01Ext.CDCQPN.DC 10.34.100.6
set security address-book global address CQFOLBVD02Ext.CDCQPN.DC 10.34.100.7
set security address-book global address VIP-for-LBExt. 10.34.100.4
set security address-book global address CQFOOMVD01Ext.CDCQPN.DC 10.34.100.8
set security address-book global address CQFOOMVD02Ext.CDCQPN.DC 10.34.100.9
set security address-book global address CQFOOMVD03Ext.CDCQPN.DC 10.34.100.10
set security address-book global address CQFOCATVD01Ext.CDCQPN.DC 10.34.100.11
set security address-book global address CQFOCATVD02Ext.CDCQPN.DC 10.34.100.12
set security address-book global address CQFOOAMVD01Ext.CDCQPN.DC 10.34.100.13
set security address-book global address CQFOOAMVD02Ext.CDCQPN.DC 10.34.100.14
set security address-book global address CQFOILCVD01Ext.CDCQPN.DC 10.34.100.16
set security address-book global address CQFOILCVD02Ext.CDCQPN.DC 10.34.100.17
set security address-book global address VIP-for-ILCExt.CDCQPN.DC 10.34.100.15
set security address-book global address CQFOARCVD01Ext.CDCQPN.DC 10.34.100.19
set security address-book global address CQFOARCVD02Ext.CDCQPN.DC 10.34.100.20
set security address-book global address VIP-for-ARCExt.CDCQPN.DC 10.34.100.18
set security address-book global address CQREDBLIS 10.34.250.21
set security address-book global address 10.65.11.236 10.65.11.236
set security address-book global address 10.65.11.237 10.65.11.237
set security address-book global address 10.34.240.9 10.34.240.9
set security address-book global address 10.34.120.4-29 range-address 10.34.120.4 to 10.34.120.29
set security address-book global address 10.34.121.4-17 range-address 10.34.121.4 to 10.34.121.17
set security address-book global address 10.34.122.4-11 range-address 10.34.122.4 to 10.34.122.11
set security address-book global address 0 10.34.122.40
set security address-book global address 0 10.34.122.41
set security address-book global address 0 10.34.122.42
set security address-book global address 10.65.124.4-28 range-address 10.65.124.4 to 10.65.124.28
set security address-book global address 10.65.125.13-23 range-address 10.65.125.13 to 10.65.125.23
set security address-book global address 10.65.126.4-13 range-address 10.65.126.4 to 10.65.126.13
set security address-book global address 10.65.127.4-10 range-address 10.65.127.4 to 10.65.127.10
set security address-book global address 10.65.128.4-5 range-address 10.65.128.4 to 10.65.128.5
set security address-book global address 10.68.40.4-28 range-address 10.68.40.4 to 10.68.40.28
set security address-book global address Trilio-Dst1 range-address 10.65.29.250 to 10.65.29.254
set security address-book global address Trilio-Dst2 10.64.35.250
set security address-book global address Trilio-Dst3 10.64.31.250
set security address-book global address Trilio-Dst4 range-address 10.65.243.5 to 10.65.243.8
set security address-book global address Trilio-Dst5 10.65.29.250
set security address-book global address 10.34.12.21 10.34.12.21
set security address-book global address 10.34.12.22 10.34.12.22
set security address-book global address 10.34.12.16 10.34.12.16
set security address-book global address 10.34.12.17 10.34.12.17
set security address-book global address 10.65.9.5 10.65.9.5
set security address-book global address 10.65.9.6 10.65.9.6
set security address-book global address 10.65.202.201-210 range-address 10.65.202.201 to 10.65.202.210
set security address-book global description BMC-Remedy-DWP-Catalog address CSQDWCGVD01 10.65.251.35
set security address-book global description BMC-Remedy-Smart-Reporting address CSQRESRVD01 10.65.251.29
set security address-book global address Remedy_Ticketing_DWP description BMC-Remedy-DWP_servers_IP_range range-address 10.65.251.31 to 10.65.251.32
set security address-book global address Remedy_Ticketing_Smart_IT description BMC-Remedy-SmIT_servers_IP_range range-address 10.65.251.25 to 10.65.251.26
set security address-book global address sFTP_Nokia_ITSM_iDB 10.65.240.16/28
set security address-book global address CSDCIMApp01 192.168.8.17/32
set security address-book global address AD-Bridge1 10.65.87.11/32
set security address-book global address AD-Bridge2 10.65.87.12/32
set security address-book global address SSN-Gemalto 10.64.10.136/29
set security address-book global address Unity_Group range-address 10.64.70.20 to 10.64.70.22
set security address-book global address IAM_Servers_1 range-address 10.64.10.186 to 10.64.10.187
set security address-book global address IAM_Servers_2 range-address 10.64.10.210 to 10.64.10.213
set security address-book global description CEP_Data_Base_Server address CEP_DB_failover 10.34.120.27/32
set security address-book global description Open_Data_Data_Base_Server address CEP_Open_Data__DB_failover 10.34.122.41/32
set security address-book global description Portal_Data_Base_Server address CEP_Portal_DB_failover 10.34.120.28/32
set security address-book global description CCP_GIS_QPN_Op_PostgreSQL address CCP_GIS_QPN_Op_PostgreSQL_failover 10.34.122.47/32
set security address-book global description CCP_GIS_QPN_Op_PostgreSQL address CCP_GIS_QPN_Op_PostgreSQL_sqlins 10.34.122.48/32
set security address-book global description CEP_Data_Base_Server address CEP_DB_sqlIns 10.34.120.26/32
set security address-book global description Open_Data_Data_Base_Server address CEP_Open_Data__DB_sqlIns 10.34.122.42/32
set security address-book global description Portal_Data_Base_Server address CEP_Portal_DB_sqlIns 10.34.120.29/32
set security address-book global description Load_balancer address LoadBalancer_External_QPN_VIP 10.34.121.13/32
set security address-book global description Load_Balancer-_External address LoadBalancer_External_DMZ_Cluster 10.32.16.6/32
set security address-book global description Load_Balancer-_External address LoadBalancer_External_DMZ_VIP 10.32.16.7/32
set security address-book global address VDI_SSN_ESXI_MGMT01 10.64.67.5/32
set security address-book global address VDI_SSN_ESXI_MGMT02 10.64.67.10/32
set security address-book global address VDI_SSN_ESXI_MGMT03 10.64.67.15/32
set security address-book global address VDI_SSN_ESXI_MGMT04 10.64.67.20/32
set security address-book global address VDI_SSN_ESXI_VDI01 10.64.64.135/32
set security address-book global address VDI_SSN_ESXI_VDI02 10.64.64.140/32
set security address-book global address VDI_SSN_ESXI_VDI03 10.64.64.145/32
set security address-book global address VDI_SSN_ESXI_VDI04 10.64.64.150/32
set security address-book global address VDI_SSN_ESXI_VDI05 10.64.64.155/32
set security address-book global address VDI_SSN_ESXI_VDI06 10.64.64.160/32
set security address-book global address VDI_SSN_ESXI_VDI07 10.64.64.165/32
set security address-book global address VDI_SSN_ESXI_VDI08 10.64.64.170/32
set security address-book global address VDI_SSN_ESXI_VDI09 10.64.64.175/32
set security address-book global address VDI_SSN_ESXI_VDI10 10.64.64.180/32
set security address-book global address VDI_SSN_ESXI_VDI11 10.64.64.185/32
set security address-book global address VDI_SSN_ESXI_VDI12 10.64.64.190/32
set security address-book global address VDI_SSN_ESXI_VAPP01 10.64.64.200/32
set security address-book global address VDI_SSN_ESXI_VAPP02 10.64.64.205/32
set security address-book global address VDI_SSN_ESXI_VAPP03 10.64.64.210/32
set security address-book global address VDI_SSN_ESXI_CITRIX01 10.64.64.10/32
set security address-book global address VDI_SSN_ESXI_CITRIX02 10.64.64.15/32
set security address-book global address VDI_SSN_ESXI_VMCLOUD01 10.64.67.200/32
set security address-book global address VDI_SSN_ESXI_VMCLOUD02 10.64.67.205/32
set security address-book global address VDI_SSN_TS01 10.64.67.70/32
set security address-book global address VDI_SSN_TS02 10.64.67.75/32
set security address-book global address VDI_SSN_VCENTER01 10.65.48.10/32
set security address-book global address VDI_SSN_VROPS01 10.65.48.15/32
set security address-book global address VDI_SSN_VROPS_Replica01 10.65.48.20/32
set security address-book global address VDI_SSN_VROPS_Replica02 10.65.48.25/32
set security address-book global address VDI_SSN_STOREONCE_MGMT01 10.64.65.10/32
set security address-book global address VDI_SSN_RMC_STOREONCE_MGMT01 10.64.65.15/32
set security address-book global address VDI_SSN_PRIMERA_MGMT01 10.64.65.40/32
set security address-book global address VDI_SSN_SSMC_PRIMERA_MGMT01 10.64.65.50/32
set security address-book global address VDI_SSN_RMC_Primera_MGMT01 10.64.65.45/32
set security address-book global address CCP_IoTOPs_APP_Cluster 10.65.124.46/32
set security address-book global address CCP_Dashboard_Report_App_Cluster 10.65.126.21/32
set security address-book global address CCP_APP_administration_APP_Cluster 10.65.126.20/32
set security address-book global address GCC_Datacenter description External_-_GCC_integration range-address 10.251.9.25 to 10.251.9.26
set security address-book global address CCC-Datacenter description External_-_CCC_integration range-address 10.1.21.45 to 10.1.21.48
set security address-book global description Load_Balancer_internal_SSN address LB_I_SSN 10.65.130.0/24
set security address-book global description Load_Balancer_internal_QPN address LB_I_QPN 10.34.121.0/24
set security address-book global description Load_Balancer_External_DMZ address LB_E_DMZ 10.32.16.0/24
set security address-book global description CEP_Application_QPN_Core address CEP_QPN 10.34.120.0/24
set security address-book global description CCP_Application_QPN_Core address CCP_QPN 10.34.121.0/24
set security address-book global description CEP_&_GIS_Application_QPN_Core address CEP___GIS_QPN 10.34.122.0/24
set security address-book global description CCP_Platform_Application_SSN_Core address CCP_Platform_SSN 10.65.124.0/24
set security address-book global description Social_Media_Citizen_Sentiment_Analytics_Application_Server address SocialMed_App_SSN 10.65.125.0/24
set security address-book global description CCP_Dashboard_&_ML address CCP_BI_ML_SSN 10.65.125.0/24
set security address-book global description CCP_Platform_Database_SSN address CCP_DB_SSN 10.65.126.0/24
set security address-book global description CCP_Energy_&_Parking_Applications address CCP_App_SSL_SP_SSN 10.65.127.0/24
set security address-book global description CCP_Deployment_SSN address CCP_deployment_SSN 10.65.128.0/24
set security address-book global description GIS_Application address CCP_GIS_SSN 10.65.131.0/24
set security address-book global description CCP_Big_Data address CCP_BIG_DB_SSN 10.68.40.0/24
set security address-book global description ERP address ERP_System 10.65.136.0/24
set security address-book global address CRM_System description CRM range-address 10.34.28.5 to 10.34.28.6
set security address-book global address sFTP_for_DG_FW 10.65.8.16/28
set security address-book global address sFTP_Nokia_ITSM_iDB 10.65.240.16/28
set security address-book global address NFM_T 10.20.16.2/32
set security address-book global address NSO_NN-1 10.20.58.26/32
set security address-book global address NSO_NN-2 10.20.58.20/32
set security address-book global address Zhone 10.20.11.16/32
set security address-book global address GIS_SSN 10.65.13.19/32
set security address-book global address Redhat-Nokia-1 10.64.24.19/32
set security address-book global address Redhat-Nokia-2 10.64.24.20/32
set security address-book global address Redhat-Nokia-3 10.64.24.21/32
set security address-book global address Redhat-Nokia-4 10.64.34.8/32
set security address-book global address Redhat-Nokia-5 10.64.34.9/32
set security address-book global address CNI_1 10.65.85.6/32
set security address-book global address CNI_2 10.65.85.7/32
set security address-book global address CNI_3 10.65.85.8/32
set security address-book global address CNI_4 10.65.85.9/32
set security address-book global address CNI_5 10.65.85.38/32
set security address-book global address CNI_6 10.65.85.39/32
set security address-book global address CNI_7 10.65.85.40/32
set security address-book global address CNI_8 10.65.85.41/32
set security address-book global address HDM_1 range-address 10.20.11.193 to 10.20.11.206
set security address-book global address HDM_2 range-address 10.20.11.225 to 10.20.11.238
set security address-book global address NAF_1 range-address 10.20.11.209 to 10.20.11.222
set security address-book global address NAF_2 range-address 10.20.11.241 to 10.20.11.254
set security address-book global address QPN_DB_AM 10.34.240.9/32
set security address-book global address 10.215.193.11-42 description Operator_Access_04 range-address 10.215.193.11 to 10.215.193.42
set security address-book global address 10.215.193.53-58 description Operator_Access_05 range-address 10.215.193.53 to 10.215.193.58
set security address-book global description TriplePlay-Signage address DS-TP-01 10.65.124.31/32
set security address-book global address 10.68.4.5-200 description Staging-Env range-address 10.68.4.5 to 10.68.4.200
set security address-book global address Etisalat_WIN_1 range-address 10.65.121.4 to 10.65.121.13
set security address-book global address Etisalat_WIN_2 range-address 10.65.125.13 to 10.65.125.16
set security address-book global address Etisalat_WIN_3 range-address 10.65.124.18 to 10.65.124.24
set security address-book global address Etisalat_WIN_4 range-address 10.65.125.21 to 10.65.125.22
set security address-book global address Etisalat_WIN_5 range-address 10.65.126.4 to 10.65.126.9
set security address-book global address Etisalat_WIN_6 range-address 10.65.127.4 to 10.65.127.7
set security address-book global address Etisalat_WIN_7 range-address 10.65.129.4 to 10.65.129.5
set security address-book global address Etisalat_WIN_8 range-address 10.65.121.14 to 10.65.121.15
set security address-book global address Etisalat_WIN_9 range-address 10.65.120.14 to 10.65.120.21
set security address-book global address Etisalat_WIN_10 range-address 10.65.123.6 to 10.65.123.17
set security address-book global address Etisalat_LIN_1 range-address 10.65.124.4 to 10.65.124.17
set security address-book global address Etisalat_LIN_2 range-address 10.65.125.17 to 10.65.125.23
set security address-book global address Etisalat_LIN_3 10.65.128.4
set security address-book global address Etisalat_LIN_4 range-address 10.65.130.4 to 10.65.130.5
set security address-book global address Etisalat_LIN_5 range-address 10.65.123.4 to 10.65.123.5
set security address-book global address Etisalat_LIN_6 range-address 10.65.131.4 to 10.65.131.21
set security address-book global address Etisalat_LIN_7 range-address 10.65.125.4 to 10.65.125.12
set security address-book global address BMC_remedy_NEW range-address 10.65.251.25 to 10.65.251.34
set security address-book global address VPN_FW_MGM 10.32.10.96/29
set security address-book global address 10.215.193.45-65 range-address 10.215.193.45 to 10.215.193.65
set security address-book global address 10.65.131.4-20 range-address 10.65.131.4 to 10.65.131.20
set security address-book global address Zhone 10.20.11.0/27
set security address-book global address pacudsraingest01 10.65.42.5
set security address-book global address pacudsraingest02 10.65.42.6
set security address-book global address pacudsraingest01-vip 10.65.42.7
set security address-book global address pacudsraingest02-vip 10.65.42.8
set security address-book global address pacudsraingest-scan1 10.65.42.9
set security address-book global address pacudsraingest-scan2 10.65.42.10
set security address-book global address pacudsraingest-scan3 10.65.42.11
set security address-book global address VIP_Oracle 10.65.13.28

'''
def load_configurations(cu,config_set):
    try:    
        command_err=''
        #load configuration changes
        print (">Loading configuration changes in progress...")
        for command in config_set.splitlines():
            command_err = command
            cu.load(command, format='set')
        #print the candidate configuration on screen
        cu.pdiff()
        print (">Configuration loaded succesfully\n")
        print("Press any key to continue...")
        input()
    except (ConfigLoadError, CommitError) as err:
        print ('Error at: ' ,command_err)
        print ("Unable to load configuration changes:\n{0}".format(err))
        print("Press any key to continue...")
        input()
def retrive_configurations(find_data): #(dev)
    # data = dev.rpc.get_config(options={'format':'set'},filter_xml='security/address-book')
    # retrived__data = etree.tostring(data, encoding='unicode', pretty_print=True)
    # retrived_data = retrived__data.strip().split('\n')
    # retrived_data.pop()
    # retrived_data.pop(0)
    # retrived_data = [
        # 'set security address-book global address DMC 10.32.10.96/29',
        # 'set security address-book global address asd 10.32.10.96/29',
        # 'set security address-book global address csa123 10.32.10.96/29'
        # ]
        
    retrived_data = [line.strip() for line in sets.strip().split('\n')]
     # [[each line.split], [each line.split], [each line.split]]

    # for each_line1 in result:
    for each_line in retrived_data:
        if f'address {find_data}' in each_line: return True

    return False
    
    
    
    