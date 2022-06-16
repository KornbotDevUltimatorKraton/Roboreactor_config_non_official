import configparser # getting the config parse to write the config code 
import json 
import os 
import sys 
import glob 
import getpass

#+++++++++++++++++Warning ! the file should created in authorized directory inorder to create the config file +++++++++++++++++++++++++++# 
#data_requested = {'Camera_raw_1': '127.0.0.1,5080', 'face_recog_2': '127.0.0.1,5080,5081', 'Multiple_node_logic_3': '[object Object]', 'Speech_recognition_4': '127.0.0.1,5070,5071,English', 'Serial_com_connect_5': '127.0.0.1,5071,English,Thai', 'Text_to_speech_6': 'English,undefined', 'Text_to_speech_7': 'English,undefined'}
#data_requested = {'Camera_raw_1': '127.0.0.1,5080', 'face_recog2': '127.0.0.1,5080,5081', 'Multiple_node_logic_3': '[object Object]', 'Serial_com_connect_4': 'Serial USB', 'Sensor_array_5': '640,480,Display activate', 'NLP_languageprocessing_7': '127.0.0.1,5071,5072,English', 'tts_8': 'English,undefined', 'Speech_recognition_9': '127.0.0.1,5070,5071,English'}
#data_requested = {'Camera_raw_1': '127.0.0.1,5080', 'face_recog_2': '127.0.0.1,5080,5081', 'Multiple_node_logic_3': '[object Object]', 'Speech_recognition_4': '127.0.0.1,5070,5071,English', 'NLP_languageprocessing_5': '127.0.0.1,5071,5072,English', 'Text_to_speech_6': 'English,undefined', 'QR_code_scanner_pub_7': '127.0.0.1,5080,5082'}
#data_requested = {'Camera_raw_1': '127.0.0.1,5080', 'face_recog_2': '127.0.0.1,5080,5081', 'Multiple_node_logic_3': [1, 2, 3, 4, 5, 6, 7, 9], 'Speech_recognition_4': '127.0.0.1,5070,5071,English', 'Serial_com_connect_5': 'Serial USB', 'Sensor_array_6': '640,480,Display activate', 'NLP_languageprocessing_7': '127.0.0.1,5071,5072,English'}
#data_requested = {'tts_1': 'Chinese,90', 'Camera_raw_2': '127.0.0.1,5080', 'face_recog_3': '127.0.0.1,5080,5081', 'Multiple_node_logic_4': [1, 2, 3, 4, 5, 6, 7, 8], 'NLP_languageprocessing_5': '127.0.0.1,5071,5072,English', 'Speech_recognition_6': '127.0.0.1,5070,5071,English', 'Serial_com_connect_7': 'Serial USB', 'Sensor_array_8': '640,480,Display activate'}
#data_requested = {'Camera_raw_2': '127.0.0.1,5080', 'Multi_cache_server_1': '127.0.0.1,127.0.1.7,5080', 'face_recog_3': '127.0.1.7,5080,5081', 'Multiple_node_logic_4': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'body_detect_pub_5': '127.0.1.7,5080,5082', 'QR_code_scanner_pub_6': '127.0.1.7,5080,5082', 'Speech_recognition_7': '127.0.0.1,5070,5071,English', 'NLP_languageprocessing_8': '127.0.0.1,5071,5072,English', 'tts_9': 'English,100'}
data_requested = {'Camera_raw_1': '127.0.0.1,5080,0', 'Multi_cache_server_2': '0,127.0.1.7,5080', 'face_recog_3': '127.0.1.7,0,5080,5081,Non', 'Multiple_node_logic_4': [1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13], 'QR_code_scanner_pub_5': '127.0.1.7,0,5080,5071,Non', 'Serial_com_connect_6': 'Serial USB', 'Sensor_array_7': '640,480,Non', 'subscriber_data_11': '127.0.0.1,5080', 'publish_data_10': '127.0.0.1,5071', 'Servo_control_13': '127.0.0.1,5081,I2C'}
user = getpass.getuser() # Getting the user host 
Home_path = '/home/'+str(user)+"/" #Home path to get the config file and project setting outside the node generator
# Reading the path of the project config

Path = '/home/'+str(user)+"/Roboreactor_projects"
config = configparser.ConfigParser()
config.read(Path+'/config_project_path.cfg') 
path_project_config = config['Project_path']['path']   # Reading the path of the project 
Path_local = '/home/'+str(user)+"/Roboreactor_Gen_config"  # Generate the main path for config gen and code generator
print("Current project path",path_project_config)
try:
    os.mkdir(Path,mode=0o777) # Give permission to create path of directory 
except:
   print("Directory")
try:
   print("Start writing config file......") 
   config = configparser.ConfigParser()    
   config.add_section('Project_path')
   config.set('Project_path','path',Path) # Created the path file of config 
   configfile = open(Path+"/config_codegen.cfg",'w') # Reading the path file of the project 
   config.write(configfile)
   
except: 
   print("Configfile was created!")
   
config.read('config_codegen.cfg') 
path_config = config['Project_path']['path']
print("Reading current path:",path_config) # Reading current path file 
message_path = Path_local+"/roboreactor_node/message_node/"
vision_path = Path_local+"/roboreactor_node/vision/"
navigation_path = Path_local+"/roboreactor_node/navigation/"
motion_path = Path_local+"/roboreactor_node/motion/motor/"
audio_path = Path_local+"/roboreactor_node/audio/"
nlp_path = Path_local+"/roboreactor_node/nlp/"
serial_path = Path_local+"/roboreactor_node/Serialcom/"
Sensor_array_path = Path_local+"/roboreactor_node/sensor_array/"
Multiple_logic_path = Path_local+"/roboreactor_node/multiple_logic_node/"

#Generate config code 
class config_from_keys(object):
       def pub_node(self,path_num,data_requested):
             print(message_path)
             config = configparser.ConfigParser()    
             config.read(message_path+'publisher_node.cfg') 
             list_data = os.listdir(message_path)
             print(list_data)
             pub_buffer= config['pub_node']['pub_node_buffers'] # Getting the path data of the buffers          
             print(pub_buffer) 
             #Write config code 
             print("Start writing path....")
             project_config_path = path_project_config+"/"+path_num  # Config path for create config file in the project 
             try:
               os.mkdir(path_project_config+"/"+path_num,mode=0o777) # Making the directory 
             except:
                print("Directory was created!")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")                

       def sub_node(self,path_num,data_requested): 
             print(message_path)
             config = configparser.ConfigParser()    
             config.read(message_path+'subscriber_node.cfg') 
             list_data = os.listdir(message_path)
             print(list_data)
             sub_buffer= config['sub_node']['sub_node_buffers'] # Getting the path data of the buffers          
             print(sub_buffer) 
             #write config code 
             print("Start writing path....")
             project_config_path = path_project_config+"/"+path_num  # Config path for create config file in the project 
             try:
               os.mkdir(path_project_config+"/"+path_num,mode=0o777) # Making the directory 
             except:
                print("Directory was created!")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])

                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")     
       #Vision part 
       def Camera_raw(self,path_num,data_requested):
             #Read path 
             print(vision_path)
             config = configparser.ConfigParser()    
             config.read(vision_path+'camera_raw/camera_raw.cfg') 
             list_data = os.listdir(vision_path)
             print(list_data)
             camera_buffer= config['camera_data']['camera_buffer'] # Getting the path data of the buffers          
             print(camera_buffer) 
             #Write path
             print("Start writing path....")     
             project_config_path = path_project_config+"/"+str(path_num)  # Config path for create config file in the project 
             print("Created path",project_config_path) #show the writing path 
             try:
               os.mkdir(path_project_config+"/"+path_num,mode=0o777) # Making the directory 
             except:
                print("Directory was created!")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  config.set(str(path_num),"camera_number",data_requested.split(",")[2])
                  

                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")   
       def Multicache_cache_server(self,path_num,data_requested):
             #Read path 
             print(vision_path)
             config = configparser.ConfigParser()    
             config.read(vision_path+'camera_raw/camera_raw.cfg') 
             list_data = os.listdir(vision_path)
             print(list_data)
             camera_buffer= config['camera_data']['camera_buffer'] # Getting the path data of the buffers          
             print(camera_buffer) 
             #Write path
             print("Start writing path....")     
             project_config_path = path_project_config+"/"+str(path_num)  # Config path for create config file in the project 
             print("Created path",project_config_path) #show the writing path 
             try:
               os.mkdir(path_project_config+"/"+path_num,mode=0o777) # Making the directory 
             except:
                print("Directory was created!")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"camera_number",data_requested.split(",")[0])
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[1])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  config.set(str(path_num),"camera_number",data_requested.split(",")[2])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")           
       def face_rec(self,path_num,data_requested): 
             #Read path 
             print(vision_path)
             config = configparser.ConfigParser()    
             config.read(vision_path+'face_recognition/facerec.cfg') 
             list_data = os.listdir(vision_path)
             print(list_data)
             face_buffer = config['face_rec_dat']['face_rec_buffer'] # Getting the path data of the buffers          
             print(face_buffer) 
             #Write path   
             print("Start writing path....")
             project_config_path = path_project_config+"/"+str(path_num)  # Config path for create config file in the project 
             print("Created path",project_config_path) #show the writing path 
             try:
               os.mkdir(path_project_config+"/"+path_num,mode=0o777) # Making the directory 
             except:
                print("Directory was created!")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"camera_number",data_requested.split(",")[1])
                  config.set(str(path_num),"port",data_requested.split(",")[2])  
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!") 
       def QR_code_scanner_pub(self,path_num,data_requested):
             #Read path 
             print(vision_path)
             config = configparser.ConfigParser()    
             config.read(vision_path+'qr_code/qr_detect.cfg') 
             list_data = os.listdir(vision_path)
             print(list_data)
             qr_buffer = config['qr_detect']['qr_detect_buffer'] # Getting the path data of the buffers          
             print(qr_buffer) 
             #Write path   
             project_config_path = path_project_config+"/"+str(path_num)  # Config path for create config file in the project 
             print("Created path",project_config_path) #show the writing path 
             try:
               os.mkdir(path_project_config+"/"+path_num,mode=0o777) # Making the directory 
             except:
                print("Directory was created!")            
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  config.set(str(path_num),"port_message",data_requested.split(",")[2])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")   
       def OCR_code(self,path_num,data_requested):
             #Read path 
             print(vision_path)
             config = configparser.ConfigParser()    
             config.read(vision_path+'ocr/ocr_detect.cfg') 
             list_data = os.listdir(vision_path)
             print(list_data)
             ocr_buffer = config['ocr_detec']['ocr_detec_buffer'] # Getting the path data of the buffers          
             print(ocr_buffer) 
             #Write path
             project_config_path = path_project_config+"/"+str(path_num)  # Config path for create config file in the project 
             print("Created path",project_config_path) #show the writing path 
             try:
               os.mkdir(path_project_config+"/"+path_num,mode=0o777) # Making the directory 
             except:
                print("Directory was created!")            
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[0])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")     
       def Skeletal_detection(self,path_num,data_requested):
             #Read path 
             print(vision_path)
             config = configparser.ConfigParser()    
             config.read(vision_path+'skeletal_detection/skeletal_detect.cfg') 
             list_data = os.listdir(vision_path)
             print(list_data)
             skeletal_buffer = config['skeletal_detect']['skeletal_detect_buffer'] # Getting the path data of the buffers          
             print(skeletal_buffer) 
             #Write path 
             project_config_path = path_project_config+"/"+str(path_num)  # Config path for create config file in the project 
             print("Created path",project_config_path) #show the writing path 
             try:
               os.mkdir(path_project_config+"/"+path_num,mode=0o777) # Making the directory 
             except:
                print("Directory was created!")

             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")      
       def Body_detection(self,path_num,data_requested):
             #Read path 
             print(vision_path)
             config = configparser.ConfigParser()    
             config.read(vision_path+'body_detection/body_detection.cfg') 
             list_data = os.listdir(vision_path)
             print(list_data)
             body_buffer = config['body_detect']['body_detect_buffer'] # Getting the path data of the buffers          
             print(body_buffer) 
             #Write path    
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created") 
 
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")  
       #Audio part
       def Speech_recognition(self,path_num,data_requested):
             #Read path 
             print(audio_path)
             config = configparser.ConfigParser()    
             config.read(audio_path+'speech_recognition/speech_recognition.cfg') 
             list_data = os.listdir(audio_path)
             print(list_data)
             asr_buffers = config['Speech_recognition']['asr_buffers'] 
             print(asr_buffers) 
             #Write path   
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")    
       def Text_to_speech(self,path_num,data_requested):
             #Read path 
             print(audio_path)
             config = configparser.ConfigParser()    
             config.read(audio_path+'speech_synthesis/speech_synthesis.cfg') 
             list_data = os.listdir(audio_path)
             print(list_data)
             speed = config['Speech_synthesis']['tts_speed'] # Getting the path data of the buffers          
             loudness = config['Speech_synthesis']['tts_loudness']  # Getting loudness of the 
             print(speed,loudness) # Getting speed of voice and loudness  
             #Write path    
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created") 

             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")  
       #NLP part 
       def NLP_language_processing(self,path_num,data_requested):
             #Read path 
             print(nlp_path)
             config = configparser.ConfigParser()    
             config.read(nlp_path+'nlp.cfg') 
             list_data = os.listdir(nlp_path)
             print(list_data)
             language_default = config['nlp']['nlp_lang_default'] # Getting the path data of the buffers          
             print(language_default) 
             #Write path   
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")     
       def Translate_language(self,path_num,data_requested):
             print(nlp_path)
             config = configparser.ConfigParser()    
             config.read(nlp_path+'translate.cfg') # Getting the translator config
             list_data = os.listdir(nlp_path)
             print(list_data)
             path_config = config['translate_lang']['translate_lang_default'] # Getting the path data of the buffers          
             print(path_config) 
             #Write path   
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")     
       #Motion system 
       def BLDC_motor(self,path_num,data_requested):
             print(motion_path)
             config = configparser.ConfigParser()    
             config.read(motion_path+'bldc/bldc_motor.cfg') 
             list_data = os.listdir(motion_path)
             print(list_data)
             bldc_baudrate = config['bldc_motor']['bldc_motor_serial_baudrate'] # Getting the path data of the buffers          
             print(bldc_baudrate) 
             #Write path   
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")  
       def Stepper_motor(self,path_num,data_requested):
             print(motion_path)
             config = configparser.ConfigParser()    
             config.read(motion_path+'stepper/Stepper_motor.cfg') 
             list_data = os.listdir(motion_path)
             print(list_data)
             stepper_baudrate = config['stepper']['stepper_motor_serial'] # Getting the path data of the buffers          
             print(stepper_baudrate) 
             #Write path   
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created") 
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")  
       def DC_motor(self,path_num,data_requested):
             print(motion_path)
             config = configparser.ConfigParser()    
             config.read(motion_path+'dc/Dc_motor.cfg') 
             list_data = os.listdir(motion_path)
             print(list_data)
             path_config = config['DC_motor']['DC_motor_serial_baudrate'] # Getting the path data of the buffers          
             print(path_config) 
             #Write path    
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created") 
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")  
       def Servo_motor(self,path_num,data_requested):
             print(motion_path)
             config = configparser.ConfigParser()    
             config.read(motion_path+'servo/servo.cfg') 
             list_data = os.listdir(motion_path)
             print(list_data)
             servo_baudrate = config['Servo_motor']['Servo_motor_serial_baudrate'] # Getting the path data of the buffers          
             servo_i2c = config['Servo_motor']['Servo_motor_i2c_com']
             print(servo_baudrate,servo_i2c)  
             #Write path     
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")     
       #Serial com 
       def Serial_com(self,path_num,data_requested):
             print(serial_path)
             config = configparser.ConfigParser()    
             config.read(serial_path+'serial_com.cfg') 
             list_data = os.listdir(serial_path)
             print(list_data)
             serial_baudrate = config['serial_com']['serial_com_baud_rate'] # Getting the path data of the buffers          
             print(serial_baudrate) 
             #Write path    
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")   
       #Navigation 
       def Lidar(self,path_num,data_requested):
             print(navigation_path)
             config = configparser.ConfigParser()    
             config.read(navigation_path+'lidar/lidar_detect.cfg') 
             list_data = os.listdir(navigation_path)
             print(list_data)
             lidar_baudrate = config['lidar_detect']['Lidar_sensor_baudrate'] # Getting the path data of the buffers          
             print(lidar_baudrate) #Serial baudrate  
             #Write path   
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!") 
       def GPS(self,path_num,data_requested):
             print(navigation_path)
             config = configparser.ConfigParser()    
             config.read(navigation_path+'gps/gps.cfg') 
             list_data = os.listdir(navigation_path)
             print(list_data)
             gps_config = config['gps']['gps_serial_baudrate'] # Getting the path data of the buffers          
             print(gps_config) 
             #Write path 
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")    
       #Sensor array 
       def Sensor_Array(self,path_num,data_requested):
             print(Sensor_array_path)
             config = configparser.ConfigParser()    
             config.read(Sensor_array_path+'sensor_array.cfg') 
             list_data = os.listdir(Sensor_array_path)
             print(list_data)
             path_config = config['sensor_array']['sensor_array_title'] # Getting the path data of the buffers          
             print(path_config) 
             #Write path   
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"width","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"height",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!")  
       #Logic part  
       def Multiple_node_logic(self,path_num,data_requested):
             print(Multiple_logic_path)
             config = configparser.ConfigParser()    
             config.read(Multiple_logic_path+'multiple_logic_node.cfg') 
             list_data = os.listdir(Multiple_logic_path)
             print(list_data)
             multiplenode_config = config['multiple_node_logic']['multiple_node_title'] # Getting the path data of the buffers          
             print(multiplenode_config) 
             #Write path    
             project_config_path = Path+"/"+path_num  # Config path for create config file in the project 
             try: 
               os.mkdir(Path+"/"+path_num,mode=0o777) # Making the directory 
             except:
               print("Directory was created")
             try:
                  print("Start writing config file......")
                  print(data_requested)
                  config = configparser.ConfigParser() 
                  config.add_section(str(path_num))
                  config.set(str(path_num), 'path',project_config_path)
                  config.set(str(path_num),"ip_address","'"+str(data_requested.split(",")[0])+"'")
                  config.set(str(path_num),"port",data_requested.split(",")[1])
                  configfile = open(project_config_path+"/"+str(path_num)+".cfg",'w')
                  config.write(configfile)
                    
             except: 
                  print("Configfile was created!") 
#Generated code  running this function in the check found class to write the code with the json file 
class code_from_json_gen(object): 
     
       def pub_nodes(self):

           pass

       def sub_node(self): 
           pass 

       #Vision part 
       def Camera_raw(self):
             #Read path 
             config.read(vision_path+'camera_raw/config_codegen.cfg') 
             path_config = config['']['path']         

             #Write path     
             pass 
       def Multicache_cache_server(self,path_num,data_requested):
             pass 
       def face_rec(self): 
            #Read path 
            
            #Write path   
            pass 
       def QR_code_scanner_pub(self):
            pass 

       def OCR_code(self):

            pass 
       def Skeletal_detection(self):
            pass
        
       def Body_detection(self):
            pass 
        
       #Audio part
       def Speech_recognition(self):
           pass 
       
       def Text_to_speech(self):
           pass 

       #NLP part 
       def NLP_language_processing(self):
           pass

       def Translate_language(self):
           pass
     
       #Motion system 
       def BLDC_motor(self):
           pass

       def Stepper_motor(self):
           pass

       def DC_motor(self):
           pass 

       def Servo_motor(self):
           pass  

       #Serial com 
       def Serial_com(self):
           pass 

       #Navigation 
       def Lidar(self):
           pass 

       def GPS(self):
           pass 
       #Sensor array 
       def Sensor_Array(self):
           pass 
      
       #Logic part  
       def Multiple_node_logic(self):
            pass 

class Check_found_function(object):
         def Function_checker(self,input_function,path_num,sub_data): 

               #Iteratable function 
               read_output_dat = {"publish_data":"pub_node","subscriber_data":"sub_node","Camera_raw":"Camera_raw","face_recog":"face_rec","QR_code_scanner_pub":"QR_code_scanner_pub","Skeletal_detection":"Skeletal_detection","Body_detection":"Body_detection","tts":"Text_to_speech","Speech_recognition":"Speech_recognition","NLP_languageprocessing":"NLP_language_processing","Translate_language":"Translage_language","BLDC_motor":"Stepper_motor","DC_motor":"DC_motor","Servo_control":"Servo_motor","Serial_com_connect":"Serial_com","Lidar_publisher":"Lidar","GPS":"GPS","Sensor_array":"Sensor_Array"}
               for r in range(0,len(list(read_output_dat))):  # Adding the path num to the last parameter input from the loop 
                         print('\nif input_function == "'+str(list(read_output_dat)[r])+'":'+"\n\t"+str(list(read_output_dat)[r])+" = config_from_keys()"+"\n\t"+str(list(read_output_dat)[r])+"."+str(read_output_dat.get(list(read_output_dat)[r]))+"('"+str(path_num)+"','"+str(sub_data)+"')")
                         exec('\nif input_function == "'+str(list(read_output_dat)[r])+'":'+"\n\t"+str(list(read_output_dat)[r])+" = config_from_keys()"+"\n\t"+str(list(read_output_dat)[r])+"."+str(read_output_dat.get(list(read_output_dat)[r]))+"('"+str(path_num)+"','"+str(sub_data)+"')")  
                         #print('\nif input_function == "'+str(list(read_output_dat)[r])+'":'+"\n\t"+str(list(read_output_dat)[r])+" = config_from_keys()"+"\n\t"+str(list(read_output_dat)[r])+"."+str(read_output_dat.get(list(read_output_dat)[r]))+"()")
                                        
for r in list(data_requested):
       
       #print(r,r.split("_")[len(r.split("_"))-1],data_requested.get(r).split(",")) # Getting the key of the header to generate the config based on the category 
       print(r,r.split("_")[len(r.split("_"))-1],data_requested.get(r))# getting the data to classify value after loop process 
       dt = r.split("_")
       dt.remove(r.split("_")[len(r.split("_"))-1])
       f_join = "_".join(dt)
       print(f_join)
       sub_data = data_requested.get(r)
       check_scan = Check_found_function()
       check_scan.Function_checker(f_join,r,sub_data) 
  
