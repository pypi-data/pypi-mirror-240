import re
import ipaddress
from srx_classes import _configurations_

address_description = 'Address Pushed through Netconf'




excelude_address = [
    'address',
    'address-set',
    'address range',
    'address-range',
    'address group',
    'address-group',
    'address_group',
    ''
    ]

wrong_inputs=[]
  
def address_address_set(dev, input_any_address_to_configure , file_content = None):
    invalid_range = []

    

    invalid_address_set = []
    
    commands=[]
    
    lines = input_any_address_to_configure.strip().split('\n')
     # [[each line.split], [each line.split], [each line.split]]
    result = [line.split('\t') for line in lines]

    for each_line1 in result:
    
# if >>  For address and address-range >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        if len(each_line1) >= 4 and each_line1[3] != '':
            each_line = [element.replace(' ', '_').replace('-', '_').replace('&', 'And').replace('(', '').replace(')', '').replace('\r','').strip() for element in each_line1]

            # if no cloumn 5 add column 5 = ''
            if len(each_line) == 4:
                each_line.append('') 
            
            
            is_ip3 = network_ip(each_line[3], each_line)
            if is_ip3 == 'error': continue
            
            if each_line[4] != '' :
                is_ip4 = network_ip(each_line[4], each_line)
                if is_ip4 == 'error': continue
                
            
            
            # match4 is a prefix in column 5 in excel sheet and must to be 32
            match3 = ip_prefix(each_line[3])
            match4 = ip_prefix(each_line[4])
            
            # no_slash3 is ip with no prefix in column 4 in excel sheet 
            # no_slash4 is ip with no prefix in column 5 in excel sheet 
            no_slash3 = each_line[3].split('/')[0] if '/' in each_line[3] else each_line[3] 
            no_slash4 = each_line[4].split('/')[0] if '/' in each_line[4] else each_line[4]



            #==================== For Address Only ==================================================================================================
            # each_line[3] is the value in column 4 in excel sheet 
            # each_l ine[4] is the value in column 5 in excel sheet
            if each_line[4] == '' or match4 == 32 or no_slash3 == no_slash4 :
                if each_line[2] != '' and  each_line[4] == '': # ['address', word, description, ip , '']
                    if not( f'set security address-book global description {each_line[2]} address {each_line[1]} {each_line[3]}' in commands):
                        commands.append(f'set security address-book global description {each_line[2]} address {each_line[1]} {each_line[3]}')
                    continue
                    
                elif each_line[2] != '' and  each_line[4] != '': # ['address', word, description, ip , ip/prefix]
                    if not(f'set security address-book global description {each_line[2]} address {each_line[1]} {each_line[4]}' in commands):
                        commands.append(f'set security address-book global description {each_line[2]} address {each_line[1]} {each_line[4]}')
                    continue
                    
                elif each_line[2] == '' and  each_line[4] == '': # ['address', word, '', ip , ''] 
                    if not(f'set security address-book global address {each_line[1]} {each_line[3]}' in commands):
                        commands.append(f'set security address-book global address {each_line[1]} {each_line[3]}') 
                    continue
                    
                elif each_line[2] == '' and  each_line[4] != '': # ['address', word, '', ip , ip/prefix] 
                    if not(f'set security address-book global address {each_line[1]} {each_line[4]}' in commands):
                        commands.append(f'set security address-book global address {each_line[1]} {each_line[4]}')
                    continue
                    
            #==================== For Address-range Only ==================================================================================================
            if len(each_line) >= 5 and each_line[4] != '':
                end_ip =network_ip(each_line[4], each_line)
                start_ip =network_ip(each_line[3], each_line)
                
                if end_ip == 'error': continue
                if start_ip == 'error': continue
                
                ip_range = int(end_ip) - int(start_ip)
                
                if ip_range > 0:
                    
                    if each_line[2] != '': # ['address-set', word, description, ip, ip]
                        if not( f'set security address-book global address {each_line[1]} description {each_line[2]} range-address {start_ip} to {end_ip}' in commands):
                            commands.append(f'set security address-book global address {each_line[1]} description {each_line[2]} range-address {start_ip} to {end_ip}')
                        continue
                    elif each_line[2] == '': # ['address', word, '', ip , ip] 
                        if not(f'set security address-book global address {each_line[1]} range-address {start_ip} to {end_ip}' in commands):
                            commands.append(f'set security address-book global address {each_line[1]} range-address {start_ip} to {end_ip}')
                        continue
                elif ip_range < 0:
                    invalid_range.append(f"Error: Invalid IPv4 address Range: \b{each_line} no action had taken.")
                    continue
                    
  # if >>  For address and address-set >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.  
  
        #inilaize each_line1 add more elements '' if have less than 4
        if len(each_line1) < 4:
            for more_element in range(4 - len(each_line1)):
                each_line1.append('')
        
        each_line = [element.replace(' ', '_').replace('&', 'And').replace('(', '').replace('-', '_').replace(')', '').replace('\r','').strip() for element in each_line1]
        if each_line[3] == '':
            
            

            # send column 2 value to retrived data > return true or false
            
            if dev != None:
            
                is_excist_address = _configurations_.retrive_configurations( 'address', each_line[1], is_exist= 'yes', dev = dev)
                
            if file_content != None:
                
                is_excist_address = _configurations_.retrive_configurations( 'address', each_line[1], is_exist= 'yes',file_content=file_content)
                
            if is_excist_address and not(each_line[0].lower() in [s.lower() for s in excelude_address]):   # ['address-set', address, '', ''] 
                if not(f'set security address-book global address-set {each_line[0]} address {each_line[1]}' in commands):
                    commands.append(f'set security address-book global address-set {each_line[0]} address {each_line[1]}')
                continue
                
            else:
                print(f'asdasdsad asdas {each_line[1]} asad')
                print(is_excist_address)
                invalid_address_set.append(f'The address [ {each_line[1]} ] not exist. So you can not add it to address-set [ {each_line[0]} ]. No action had taken.')
                continue
                
    return [commands, wrong_inputs, invalid_range, invalid_address_set, address_description]

def network_ip(ip_str,invalid_line):
    
    try:
    
        ip_network = ipaddress.IPv4Network(ip_str, strict=False)
        
        # Extract the IPv4 address without the subnet
        ipv4_address = ip_network.network_address
        return ipv4_address
        
    except Exception as e:
        wrong_inputs.append(f"Error: Invalid characters in the IPv4 address: \b{invalid_line} no action had taken.")
        return 'error'
        
        
def ip_prefix(ip_str):
        if ip_str.find('/') != -1 :
            ipv4_prefix = ip_str.split('/')[1]
            return ipv4_prefix
            
      

def wrong_inputs_def():
    for x in wrong_inputs:print(x)
    
def invalid_range_def():
    for x in invalid_range: print (x)
    
def invalid_address_set_def():
    for x in invalid_address_set: print (x)


sd
address_address_set()