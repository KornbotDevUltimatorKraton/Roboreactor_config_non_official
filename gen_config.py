import json
import getpass 
import configparser
user = getpass.getuser() 
config = configparser.ConfigParser() 
config.add_section('Directory_project')
path_num = 'Camera_raw2'
Path = "/home/"+str(user)+"/Roboreactor_projects/Camera_raw_2"
config.set('Directory_project', 'path',Path)
configfile = open(Path+"/"+str(path_num)+".cfg",'w')
config.write(configfile)
