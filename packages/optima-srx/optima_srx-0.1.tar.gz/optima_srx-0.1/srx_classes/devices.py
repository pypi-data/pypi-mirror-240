import os



# Get the current script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path to the Backup folder
backup_folder = os.path.join(script_directory, "..", "Backup")  # Adjust the path here

# List files in the Backup folder
backup_files = os.listdir(backup_folder)

# enter your firewall cridential here 
first_input= [
    'Exit (0)',
    'Loacal (1)',
    'NetConf (2)',
    
    ]
 
FWs= {
    'SSN_PFW' : ['20.10.115.201','root1','Password'],
    'SSN_DFW' : ['30.10.15.202','root1','Password'],
    'QPN_PFW' : ['40.10.15.201','root1','Password'],
    'QPN_DFW' : ['50.10.15.202','root1','Password'],
    'vm' : ['192.168.16.199','root','Password'],
    'vmware Work' : ['10.10.15.201','root','Password'],
    'vmware Home' : ['192.168.1.201','root','Password']
    }
    


def loacls_Backup():

    chosen_files = []
    for i, file in enumerate(backup_files):
        chosen_files.append(file[:-4])
    return chosen_files

        
 
def open_local_backup_file(file_name):
    chosen_file = os.path.join(backup_folder, f'{file_name}.txt')

    # Search for the word 'World!' in the chosen file
    with open(chosen_file, "r") as file:
    
        lines = file.read()
        
        file_contents = lines.strip().split('\n')
        
        return file_contents
            