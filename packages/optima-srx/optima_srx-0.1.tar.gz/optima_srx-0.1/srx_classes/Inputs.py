# full set commands : enter a list of set commands to push in srx
# address : enter a list of addresses from sheet excel does not matter it is an address or address range or address group
#warning do not delete varibles just empty it
full_set_commands = '''

'''
addresses = '''
address	FMC_Datacenter	External - FMC integration	NA	


'''
applications = '''
Application	TCP_2049		tcp	any 	2049
Application	UDP_2049		udp	any 	2049
Application	TCP_3000		tcp	any 	3000
Application	TCP_6800		tcp	any 	6800
Application	TCP_4739		tcp	any 	4739
Application	UDP_4739		udp	any 	4739
Application	UDP_1194		udp	any 	1194
Application	TCP_1194		tcp	any 	1194
Application	TCP_1200		tcp	any 	1200
Application	TCP_1220		tcp	any 	1220
Application	TCP_1334		tcp	any 	1334
Application	TCP_11344		tcp	any 	11344
Application_Group	UDP_TCP_AD_IM				
Application_Group	Infra_Comm_Rule1_SrvGrp				
Application_Group	Infra_Comm_Rule2_SrvGrp				
Application-defult	junos-dns-udp			any 	
Application-defult	junos-ntp			any 	
Application-defult	junos-icmp-all			any 	
Application-defult	junos-dns-tcp			any 	
Application-defult	junos-https			any 	
Application-defult	junos-http			any 	
Application-defult	any			any 	
Application	UDP_88		udp	any 	88
Application	UDP_445		udp	any 	445
Application	TCP_46262		tcp	any 	46262
Application	TCP_4750		tcp	any 	4750
Application	TCP_9843		tcp	any 	9843
Application	TCP_5432		tcp	any 	5432
Application	TCP_9080		tcp	any 	9080
Application	TCP_1828		tcp	any 	1828
Application	TCP_8043		tcp	any 	8043
Application	TCP_3306		tcp	any 	3306
Application	TCP_8280		tcp	any 	8280
Application	TCP_6667		tcp	any 	6667
Application	TCP_2181		tcp	any 	2181
Application	TCP_8080		tcp	any 	8080
Application	TCP_50070		tcp	any 	50070
Application	TCP_8020		tcp	any 	8020
Application	TCP_9000		tcp	any 	9000
Application	TCP_50075		tcp	any 	50075
Application	TCP_50475		tcp	any 	50475
Application	TCP_50010		tcp	any 	50010
Application	TCP_1019		tcp	any 	1019
Application	TCP_50020		tcp	any 	50020
Application	TCP_1022		tcp	any 	1022
Application	TCP_50090		tcp	any 	50090
Application	TCP_8019		tcp	any 	8019
Application	TCP_16000		tcp	any 	16000
Application	TCP_16010		tcp	any 	16010
Application	TCP_16020		tcp	any 	16020
Application	TCP_16030		tcp	any 	16030
Application	TCP_8085		tcp	any 	8085
Application	TCP_9095		tcp	any 	9095
Application	TCP_6379		tcp	any 	6379
Application	TCP_1883		tcp	any 	1883
Application	TCP_8083		tcp	any 	8083
Application	TCP_18083		tcp	any 	18083
Application	TCP_9443		tcp	any 	9443
Application	TCP_10390		tcp	any 	10390
Application	TCP_10389		tcp	any 	10389
Application	TCP_8200		tcp	any 	8200
Application	TCP_9999		tcp	any 	9999
Application	TCP_11111		tcp	any 	11111
Application	TCP_8000		tcp	any 	8000
Application	TCP_10500		tcp	any 	10500
Application	TCP_8888		tcp	any 	8888
Application	TCP_8002		tcp	any 	8002
Application	TCP_8003		tcp	any 	8003
Application	TCP_8004		tcp	any 	8004
Application	TCP_8005		tcp	any 	8005
Application	TCP_2003		tcp	any 	2003
Application	TCP_10051		tcp	any 	10051
Application	TCP_10052		tcp	any 	10052
Application	TCP_10050		tcp	any 	10050
Application	TCP_1432		tcp	any 	1432
Application	TCP_5044		tcp	any 	5044
Application	TCP_9200		tcp	any 	9200
Application	TCP_5601		tcp	any 	5601
Application	TCP_9446		tcp	any 	9446
Application	TCP_9445		tcp	any 	9445
Application	TCP_10000		tcp	any 	10000
Application	TCP_9447		tcp	any 	9447
Application	TCP_10002		tcp	any 	10002
Application	TCP_9098		tcp	any 	9098
Application	TCP_29098		tcp	any 	29098
Application	TCP_9696		tcp	any 	9696
Application	TCP_29696		tcp	any 	29696
Application	TCP_7071		tcp	any 	7071
Application	TCP_27071		tcp	any 	27071
Application	TCP_8082		tcp	any 	8082
Application	TCP_8084		tcp	any 	8084
Application	TCP_8087		tcp	any 	8087
Application	TCP_8091		tcp	any 	8091
Application	TCP_8092		tcp	any 	8092
Application	TCP_27777		tcp	any 	27777
Application	TCP_28082		tcp	any 	28082
Application	TCP_28084		tcp	any 	28084
Application	TCP_28087		tcp	any 	28087
Application	TCP_28091		tcp	any 	28091
Application	TCP_28092		tcp	any 	28092
Application	TCP_28001		tcp	any 	28001
Application	TCP_10001		tcp	any 	10001
Application	TCP_9781		tcp	any 	9781
Application	TCP_9782		tcp	any 	9782
Application	TCP_9783		tcp	any 	9783
Application	TCP_9784		tcp	any 	9784
Application	TCP_9785		tcp	any 	9785
Application	TCP_9786		tcp	any 	9786
Application	TCP_9787		tcp	any 	9787
Application	TCP_9788		tcp	any 	9788
Application	TCP_9091		tcp	any 	9091
Application	TCP_3478		tcp	any 	3478
Application	TCP_3479		tcp	any 	3479
Application	TCP_5222		tcp	any 	5222
Application	TCP_5223		tcp	any 	5223
Application	TCP_5229		tcp	any 	5229
Application	TCP_7070		tcp	any 	7070
Application	TCP_7443		tcp	any 	7443
Application	TCP_5269		tcp	any 	5269
Application	TCP_5275		tcp	any 	5275
Application	TCP_5276		tcp	any 	5276
Application	TCP_5262		tcp	any 	5262
Application	TCP_5263		tcp	any 	5263
Application	TCP_9092		tcp	any 	9092
Application	TCP_9093		tcp	any 	9093
Application	TCP_84		tcp	any 	84
Application	TCP_8081		tcp	any 	8081
Application	TCP_9115		tcp	any 	9115
Application	TCP_9390		tcp	any 	9390
Application	TCP_9543		tcp	any 	9543
Application	TCP_8283		tcp	any 	8283
Application	TCP_5701		tcp	any 	5701
Application	TCP_9743		tcp	any 	9743
Application	TCP_6464		tcp	any 	6464
Application	TCP_26464		tcp	any 	26464
Application	TCP_6465		tcp	any 	6465
Application	TCP_26465		tcp	any 	26465
Application	TCP_6565		tcp	any 	6565
Application	TCP_8282		tcp	any 	8282
Application	TCP_5001		tcp	any 	5001
Application	TCP_8090		tcp	any 	8090
Application	TCP_3008		tcp	any 	3008
Application	TCP_8585		tcp	any 	8585
Application	TCP_858		tcp	any 	858
Application	TCP_280		tcp	any 	280
Application	TCP_82		tcp	any 	82
Application	TCP_8765		tcp	any 	8765
Application	TCP_9191		tcp	any 	9191
Application	TCP_29191		tcp	any 	29191
Application	TCP_1188		tcp	any 	1188
Application	TCP_21188		tcp	any 	21188
Application	TCP_8086		tcp	any 	8086
Application	TCP_4840		tcp	any 	4840
Application	TCP_21		tcp	any 	21
Application	TCP_6443		tcp	any 	6443
Application	TCP_5434		tcp	any 	5434
Application_Group	Group_1				
Application_Group	Group_11				
Application_Group	Group_14				
Application_Group	Group_19				
Application_Group	Group_22				
Application_Group	Group_27				
Application_Group	Group_20				
Application_Group	Group_18				
Application_Group	Group_15				
Application_Group	Group_12				
Application_Group	Group_2				
Application_Group	Group_16				
Application_Group	Group_3				
Application_Group	Group_9				
Application_Group	Group_26				
Application_Group	Group_4				
Application_Group	Group_24				
Application_Group	Group_28				
Application_Group	Group_10				
Application_Group	Group_13				
Application_Group	Group_5				
Application_Group	Group_6				
Application_Group	Group_23				
Application_Group	Group_25				
Application_Group	Group_8				
Application_Group	Group_7				
Application_Group	Group_17				
Application_Group	Group_21				
Application	TCP_6080		tcp	any 	6080
Application	TCP_3389		tcp	any 	3389
Application_Group	Group_sec				
Application_Group	Group_ITSM				
Application_Group	Group_NCS				
Application_Group	Group_infra				
Application_Range	TCP_49152-65535 		tcp	any 	49152-65535 
Application_Range	UDP_49152-65535 		udp	any 	49152-65535 
Application_Group	Group_extFO				
Application	TCP_44043		tcp	any 	44043
Application	TCP_44343		tcp	any 	44343
Application	TCP_44006		tcp	any 	44006
Application	TCP_44100		tcp	any 	44100
Application	TCP_44731		tcp	any 	44731
Application	TCP_45081		tcp	any 	45081
Application	TCP_45090		tcp	any 	45090
Application	TCP_45080		tcp	any 	45080
Application	TCP_8281		tcp	any 	8281
Application	TCP_9444		tcp	any 	9444
Application	TCP_8243		tcp	any 	8243
Application	TCP_20		tcp	any 	20
Application	TCP_703		tcp	any 	703
Application	TCP_1234		tcp	any 	1234
Application	TCP_7543		tcp	any 	7543
Application	TCP_7544		tcp	any 	7544
Application	TCP_27000		tcp	any 	27000
Application	TCP_29000		tcp	any 	29000
Application	TCP_30001		tcp	any 	30001
Application	TCP_30003		tcp	any 	30003
Application	TCP_30002		tcp	any 	30002
Application	TCP_28002		tcp	any 	28002
Application	TCP_7		tcp	any 	7
Application	TCP_2051		tcp	any 	2051
Application	TCP_2052		tcp	any 	2052
Application	UDP_2051		udp	any 	2051
Application	UDP_2052		udp	any 	2052
Application	TCP_61619		tcp	any 	61619
Application_Range	TCP_7778-7781		tcp	any 	7778-7781
Application_Range	TCP_19000-19500		tcp	any 	19000-19500
Application_Range	TCP_20000-20500		tcp	any 	20000-20500
Application_Range	TCP_25000-25500		tcp	any 	25000-25500
Application_Range	TCP_26000-26500		tcp	any 	26000-26500
Application_Range	TCP_27000-27500		tcp	any 	27000-27500
Application_Range	TCP_29000-30003		tcp	any 	29000-30003
Application_Range	UDP_19000-19500		udp	any 	19000-19500
Application_Range	UDP_20000-20500		udp	any 	20000-20500
Application_Range	UDP_25000-25500		udp	any 	25000-25500
Application_Range	UDP_26000-26500		udp	any 	26000-26500
Application_Range	UDP_27000-27500		udp	any 	27000-27500
Application_Range	UDP_29000-30003		udp	any 	29000-30003
Application_Group	Etisalat-Yumaccess				
Application_Group	AV_GSAN_Communication				
Application_Group	AV_UTL_MCS_Communication				
Application_Group	Avamar_service_group01				
Application_Group	Avamar_service_group02				
Application_Group	Avamar_service_group03				
Application_Group	Avamar_service_group04				
Application_Group	Avamar_service_group05				
Application	TCP_8089		tcp	any 	8089
Application_Group	TCP_5900-6923		tcp	tcp	5900-6923
Application	TCP_8123		tcp	any 	8123
Application	UDP_1521		udp	any 	1521
Application	TCP_4045		tcp	any 	4045
Application	TCP_4046		tcp	any 	4046
Application	TCP_4047		tcp	any 	4047
Application	TCP_4048		tcp	any 	4048
Application	TCP_4049		tcp	any 	4049
Application	UDP_4045		udp	any 	4045
Application	UDP_4046		udp	any 	4046
Application	UDP_4047		udp	any 	4047
Application	UDP_4048		udp	any 	4048
Application_Group	Isilon_ports_group1				
Application	UDP_4049		udp	any 	4049
Application_Group	Group_39				
Application_Group	Group_40				
Application_Group	Group_42				
Application_Group	Group_43				
Application_Group	Group_41				
Application	TCP_7766		tcp	any 	7766
Application	TCP_5006		tcp	any 	5006
Application	TCP_5055		tcp	any 	5055
Application	TCP_9099		tcp	any 	9099
Application	TCP_7072		tcp	any 	7072
Application	TCP_7778		tcp	any 	7778
Application	TCP_8883		tcp	any 	8883
Application	TCP_85		tcp	any 	85
Application	TCP_5985		tcp	any 	5985
Application	TCP_5986		tcp	any 	5986
Application	TCP_90		tcp	any 	90
Application	TCP_543		tcp	any 	543
Application	TCP_544		tcp	any 	544
Application	TCP_749		tcp	any 	749
Application	TCP_754		tcp	any 	754
Application	TCP_2105		tcp	any 	2105
Application	TCP_4444		tcp	any 	4444
Application	UDP_749		udp	any 	749
Application	TCP_3260	Unity - iSCSI	tcp	any 	3260   
Application	UDP_3260	Unity - iSCSI	udp	any 	3260          
Application	TCP_860	Unity - iSCSI	tcp	any 	860    
Application	UDP_860	Unity - iSCSI	udp	any 	860
Application	TCP_3268	Unity - iSCSI	tcp	any 	3268   
Application	UDP_3268	Unity - iSCSI	udp	any 	3268   
Application	TCP_389	Unity - iSCSI	tcp	any 	389
Application	TCP_636	Unity - iSCSI	tcp	any 	636
Application	UDP_389	Unity - iSCSI	udp	any 	636
Application_Group	Unity_iSCSI_ports_GRP				
Application	TCP_10617		tcp	any 	10617
Application	TCP_290		tcp	any 	290
Application	TCP_5900-5950		tcp	any 	5900-5950
Application	TCP_10042		tcp	any 	10042
Application	TCP_10045		tcp	any 	10045
Application	UDP_10045		udp	any 	10045
Application	TCP_3183		tcp	any 	3183
Application	TCP_3181		tcp	any 	3181
Application	TCP_5002		tcp	any 	5002
Application	TCP_1159		tcp	any 	1159
Application	TCP_587		tcp	any 	587
Application_Group	OPER_SSN_Oracle-SrvGrp				
Application	TCP_11000		tcp	any 	11000
Application_Group	Group_45				
Application	TCP_1884		tcp	any 	1884
Application	TCP_4059		tcp	any 	4059
Application	TCP_102		tcp	any 	102
Application	TCP_2406		tcp	any 	2406
Application	TCP_502		tcp	any 	502
Application	TCP_20000		tcp	any 	20000
Application 	TCP_4060		tcp	any 	4060
Application 	TCP_153		tcp	any 	153
Application 	TCP_49152		tcp	any 	49152
Application 	TCP_65535		tcp	any 	65535
Application 	TCP_9767		tcp	any 	9767
Application 	TCP_8284		tcp	any 	8284
Application 	TCP_8246		tcp	any 	8246
Application 	TCP_9763		tcp	any 	9763
Application 	TCP_6444		tcp	any 	6444
Application 	TCP_6445		tcp	any 	6445
Application 	TCP_6658		tcp		6658
Application 	TCP_3799		tcp		3799
Application 	UDP_3799		udp		3799
Application	TCP_7780		tcp		7780
Application	TCP_7781		tcp		7781
Application	UDP_2068		udp		2068
Application	TCP_902		tcp		902
Application	UDP_902		udp		902
Application	TCP_903		tcp		903
Application	UDP_903		udp		903
Application	TCP_5480		tcp		5480
Application	TCP_9087		tcp		9087
Application	TCP_9084		tcp		9084
Application	TCP_10080		tcp		10080
Application	TCP_5988		tcp		5988
Application	TCP_5989		tcp		5989
Application	UDP_6500		udp		6500
Application	TCP_9000-9100		tcp		9000-9100
Application	TCP_9388		tcp		9388
Application	TCP_9387		tcp		9387
Application	TCP_9386		tcp		9386
Application	TCP_37		tcp		37
Application	UDP_37		udp		37
Application	TCP_17988		tcp		17988
Application	TCP_17990		tcp		17990
Application	TCP_1564		tcp		1564
Application	TCP_1565		tcp		1565
Application	TCP_2233		tcp		2233
Application	TCP_5201		tcp		5201
Application	TCP_5696		tcp		5696
Application	TCP_8010		tcp		8010
Application	TCP_9096		tcp		9096
Application	TCP_9097		tcp		9097
Application	TCP_12443		tcp		12443
Application	UDP_5001		udp		5001
Application	UDP_5201		udp		5201
Application	UDP_12321		udp		12321
Application	UDP_12345		udp		12345
Application	UDP_23451		udp		23451
Application	TCP_8182		tcp		8182
Application	UDP_8182		udp		8182
Application	TCP_2868		tcp		2868
Application	TCP_6969		tcp		6969
Application	TCP_1337		tcp		1337
Application	TCP_9987		tcp		9987
Application	TCP_9989		tcp		9989
Application	TCP_2383		tcp		2383
Application	TCP_5785		tcp		5785
Application	TCP_7404		tcp		7404
Application	TCP_8205		tcp		8205
Application	TCP_8215		tcp		8215
Application	TCP_8210		tcp		8210
Application	TCP_7098		tcp		7098
Application	TCP_9126		tcp		9126
Application	TCP_9398		tcp		9398
Application	TCP_9399		tcp		9399
Application	TCP_7202		tcp		7202
Application	TCP_7201		tcp		7201
Application	TCP_7877		tcp		7877
Application	TCP_7977		tcp		7977
Application	TCP_2382		tcp		2382
Application_Group	Group_52				
Application_Group	Group_53				
Application_Group	Group_54				
Application_Group	Group_55				
Application_Group	Group_56				
Application_Group	Group_57				
Application_Group	Group_58				
Application_Group	Group_59				
Application_Group	Group_60				
Application	UDP_1812		udp		1812
Application	UDP_1813		udp		1813
Application_Group	Group_47				
Application_Group	Group_48				
Application_Group	Group_49				
Application	TCP-4059		tcp		4059
Application	TCP-4060		tcp		4060
Application	TCP-4064		tcp		4064
Application_Group	Group_Smart_Energy_Management				
Application_Group	Group_OH				
Application	TCP_44022		tcp		44022
Application	TCP_28666		tcp		28666
Application	TCP_45082		tcp		45082
Application	TCP_45083		tcp		45083
Application	TCP_43043		tcp		43043
Application	TCP_44101		tcp		44101
Application	TCP_9544		tcp		9544
Application	TCP_1034		tcp		1034
Application	TCP_1443		tcp	any 	1443
Application	TCP_8834		tcp	any 	8834
Application	TCP_8835		tcp	any 	8835
Application-Group	sec-direc-app-grp				
Application	TCP_4514		tcp	any 	4514
Application	TCP_9300		tcp	any 	9300
Application	TCP_8543		tcp	any 	8543
Application	UDP_5000		udp		5000
Application	TCP_5000		tcp		5000
Application	TCP_35357		tcp		35357
Application	UDP_35357		udp		35357
Application	TCP_13000		tcp		13000
Application	UDP_13000		udp		13000
Application	TCP_8780		tcp		8780
Application	UDP_8780		udp		8780
Application	TCP_3001		tcp		3001
Application	UDP_3001		udp		3001
Application	TCP_4567		tcp		4567
application	UDP_9996		UDP		9996
					
Application	TCP_4899_4908		TCP	any	4899-4908
Application	TCP_4889_4898		TCP	any	4889-4898
Application	TCP_7799_7809		TCP	any	7799-7809
Application	TCP_7788_7798		TCP	any	7788-7798
Application	TCP_1830_1849		TCP	any	1830-1849
					
Application	TCP_80		TCP	any	80
Application	TCP_88		TCP	any	88
Application	UDP_88		UDP	any	88
Application	TCP_111		TCP	any	111
Application	UDP_111		UDP	any	111
Application	TCP_123		TCP	any	123
Application	UDP_123		UDP	any	123
Application	TCP_135		TCP	any	135
Application	UDP_137		UDP	any	137
Application	UDP_138		UDP	any	138
Application	TCP_139		TCP	any	139
Application	TCP_162		TCP	any	162
Application	UDP_199		UDP	any	199
Application	TCP_389		TCP	any	389
Application	UDP_389		UDP	any	389
Application	TCP_445		TCP	any	445
Application	TCP_464		TCP	any	464
Application	UDP_464		UDP	any	464
Application	TCP_636		TCP	any	636
Application	UDP_636		UDP	any	636
Application	TCP_1234		TCP	any	1234
Application	UDP_1234		UDP	any	1234
Application	TCP_2049		TCP	any	2049
Application	UDP_2049		UDP	any	2049
Application	UDP_3268		UDP	any	3268
Application	TCP_3269		TCP	any	3269
Application	UDP_3269		UDP	any	3269
Application	TCP_4000		TCP	any	4000
Application	UDP_4000		UDP	any	4000
Application	TCP_4001		TCP	any	4001
Application	UDP_4001		UDP	any	4001
Application	TCP_4002		TCP	any	4002
Application	UDP_4002		UDP	any	4002
Application	TCP_4658		TCP	any	4658
Application	TCP_5080		TCP	any	5080
Application	TCP_5085		TCP	any	5085
Application	TCP_8000		TCP	any	8000
Application	TCP_8443		TCP	any	8443
Application	TCP_9443		TCP	any	9443
Application	TCP_10000		TCP	any	10000
Application	TCP_12228		TCP	any	12228
Application	TCP_32768		TCP	any	32768
Application	UDP_32768		UDP	any	32768
Application	TCP_39494		TCP	any	39494
Application	UDP_39494		UDP	any	39494
Application	TCP_49152_65335		TCP	any	49152-65335
Application	UDP_49152_65335		UDP	any	49152-65335

'''