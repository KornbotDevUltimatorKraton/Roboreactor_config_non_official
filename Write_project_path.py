import os,glob 
import getpass 
import configparser

from jsoncfg import expect_array 
user = getpass.getuser()
Path = '/home/'+str(user)+"/Roboreactor_projects"
config = configparser.ConfigParser()
config.read(Path+'/config_project_path.cfg') 
path_project_config = config['Project_path']['path'] 
path_num = "Camera_raw_2"
try:
    print(path_project_config+"/"+path_num)
    os.mkdir(path_project_config+"/"+path_num,mode=0o777) 

except:
    pass     