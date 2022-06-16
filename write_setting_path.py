import configparser 
import getpass 
user = getpass.getuser()

#path = project_config_path = "/home/"+str(user)+"/Roboreactor_Gen_config/"
#project_config_path = "/home/"+str(user)+"/Roboreactor_projects"
try:   
        print("Start writing config file......")
        config = configparser.ConfigParser() 
        config.add_section('Directory_project')
        path_num = 'Camera_raw2'
        Path = "/home/"+str(user)+"/Roboreactor_projects/Camera_raw_2"
        config.set('Directory_project', 'path',Path)
        configfile = open(Path+"/"+str(path_num)+".cfg",'w')
        config.write(configfile)
                    
except: 
     print("Configfile was created!")  
