def Create_node_pub(topic,message,addresses,initial_port): # Create the node public from the json file input from component selection and define function of the code in the node to control 
       #Create the module of the node component input into the function                
       #Before running the loop of publisher check that the module node is created
       port = initial_port
       address = addresses
       exec("pub_"+str(port)+ "= Internal_Publish_subscriber()")  
       exec("pub_"+str(port)+".Publisher_dict('"+str(address)+"',{"+"'"+str(topic)+"'"+":"+str(message)+"},"+str(port)+")") # Sending the data type dicationary now thinking about getting the value input from json file and convert data into the specific data type 
              
#Create the sensor receiver as the subscriber for each sensor parameter input from the json component input but this function going to define by json type code generator 
def Create_node_sub(t,addresses,buffer,initial_port):
             
           port = initial_port 
           address = addresses        
           exec("sub_"+str(t)+" = Internal_Publish_subscriber()")  
           exec("global data_return;data_return"+" = sub_"+str(t)+".Subscriber_dict('"+str(address)+"',"+str(buffer)+","+str(port)+")")
           return  data_return 
def Face_recognition(path_data,display,ip,port,title_name,cam_num,Buffers,portdata,ip_number):

        face_rec = Visual_Cam_optic()
        face_rec.Camera_Face_recognition(path_data,display,ip,port,title_name,cam_num,Buffers,portdata,ip_number)


def Speech_recognition(initial_lang,address,port):
           
           speech_recog = Audio_function() 
           speech_recog.Speech_recognition(initial_lang,address,port)

def Speaking_languages(text,destination_lang,speed,loudness): 
           audio_speech = Audio_function() 
           audio_speech.Text_to_speech(text,destination_lang,speed,loudness)

def Sensor_array_input(sensor_name,number,sensor_list_input,vis_output,size_video):

        exec(str(sensor_name)+"_"+str(number)+" = Tactile_sensor()")
        Sensor_name_data = str(sensor_name)+"_"+str(number)
        title_name = "'"+str(Sensor_name_data)+"'"
        exec("global data_return;data_return = "+str(sensor_name)+"_"+str(number)+".Numpy_array_image_frame("+str(sensor_list_input)+","+str(title_name)+","+str(vis_output)+","+str(size_video)+")")
        return data_return   


def Sensor_anaiter(sensor_name,number,sensor_serial):
           exec("sensor_name_"+str(number)+" = Analog_sensor_read()")
           exec("sensor_name_"+str(number)+".Analog_Iteration_tools('"+str(sensor_name)+"',sensor_serial)")

def Sensor_anasetpins(sensor_name,number,sensor_serial,pins_array):
           exec("sensor_name_"+str(number)+" = Analog_sensor_read()")
           exec("sensor_name_"+str(number)+".Analog_setting_pins(sensor_serial,"+str(pins_array)+")")

def Sensor_anafirmserial(sensor_name,number,sensor_serial,pins,ip,port):
            exec("sensor_name_"+str(number)+" = Analog_sensor_read()")
            exec("sensor_name_"+str(number)+".Analog_firmware_serial(sensor_name,"+str(number)+","+"sensor_serial"+","+str(pins)+",'"+str(ip)+"',"+str(port)+")") 

def Array_streamer_input(cam_num,array_frame,Buffers,ip_number,portdata):
           exec("Sensor_"+str(cam_num)+"= Array_image_streamer()") 
           exec("Sensor_"+str(cam_num)+".Array_image_transfer("+str(cam_num)+","+str(array_frame)+","+str(Buffers)+",'"+str(ip_number)+"',"+str(portdata)+")")
           

def Gyroscope_sensor(module,ip,port):  # Getting i2c address 
             gyro_pos_1 = Gyroscope_function()
             gyro_pos_1.Gyro_sensor_module(module,i2c_bus,ip,port)# Getting i2c address and name of module

def Language_translator(text,ip,port,lang):
           trans_lang = NLP_language_trans()  
           trans_lang.Language_translator(text,ip,port,lang)    
# Checking if serial is main_node or node 
def Serial_write_multipurpose(number,serial_name,text_input,encode_mode,encode): 
       exec("board_name_"+str(number)+" = Serial_write_read()")
       exec("board_name_"+str(number)+".Serial_write(serial_name,"+str(text_input)+","+str(encode_mode)+",'"+str(encode)+"')")

def Serial_read_multipurpose(number,serial_name,decode_mode,decode,ip,port):
       exec("board_name_"+str(number)+" = Serial_write_read()")
       exec("board_name_"+str(number)+".Serial_read(serial_name,"+str(decode_mode)+",'"+str(decode)+"','"+str(ip)+"',"+str(port)+")")
       
def Create_serial_motor(mcu_number,number,pin_number,motor_name):
        #node_type,component_name,Serialdev,mcu_number,number,pin_number,motor_name,speed,gpiol,gpior
        motor_node = Action_control()    # STM32F103C8TX 1 [2, 3] motor_1 1 1 0 
        motor_node.Serial_MCU(mcu_number,number,pin_number,motor_name)
def Create_serial_motor_logic(mcu_number,number,speed,gpiol,gpior):
        motor_logic  = Action_control()
        motor_logic.Serial_DC_motor_pins_drive(mcu_number,number,speed,gpiol,gpior)            
def Create_i2c_Servo(servo_num,servo_name,angle,pin):
     try: 
        # define the name angle and pin of the servo to connect into the board 
        exec("servo_"+str(servo_num)+" = Action_control()") 
        exec("servo_"+str(servo_num)+".I2C_servo_motor('"+str(servo_name)+"',"+str(angle)+","+str(pin)+")")
     except: 
        print("Checking your variables and pins data input")      
def microcontroller_info_dat(mcu_code_name): 
            exec("mcu_"+str(mcu_code_name)+" = Microcontroller_pins()") 
            exec("global data_mcu; data_mcu" +" = mcu_"+str(mcu_code_name)+".request_mcu('"+str(mcu_code_name)+"')") # Getting the request mcu data 
            return data_mcu 

# Non execution pub node 
def Camera_pub_node(cam_num,buffers,port,ip_number): # running all theses in exec 
         
       exec("cam_"+str(cam_num)+" = Visual_Cam_optic()")
       exec("cam_"+str(cam_num)+".Camera_raw("+str(cam_num)+","+str(buffers)+","+str(port)+",'"+str(ip_number)+"')")

# Non execution sub node 
def Camera_QR_sub_node(cam_num,buffers,port,port_message,ip_number): # Input the function into the the command all list of computer vision are { Camera_raw , Camera_QR, Camera_OCR, Camera_yolo, Camera_face_recognition, Camera_Visual_to_text}
  
       exec("cam_"+str(cam_num)+" = Visual_Cam_optic()")
       exec("cam_"+str(cam_num)+".Camera_QR("+str(cam_num)+","+str(buffers)+","+str(port)+","+str(port_message)+",'"+str(ip_number)+"')")

def Camera_OCR_sub_node(cam_num,buffers,port,port_message,ip_number):
       exec("cam_"+str(cam_num)+" = Visual_Cam_optic()")
       exec("cam_"+str(cam_num)+".Camera_OCR("+str(cam_num)+","+str(buffers)+","+str(port)+","+str(port_message)+",'"+str(ip_number)+"')")
       

def Camera_face_rec_sub_node(cam_num,buffers,port,port_message,ip_number):
       exec("cam_"+str(cam_num)+" = Visual_Cam_optic()")
       exec("cam_"+str(cam_num)+".Camera_Face_recongnition("+str(cam_num)+","+str(buffers)+","+str(port)+","+str(port_message)+",'"+str(ip_number)+"')")   
       

def Camera_yolo_sub_node(cam_num,buffers,port,port_message,ip_number): 

        exec("cam_"+str(cam_num)+" = Visual_Cam_optic()")
        exec("cam_"+str(cam_num)+".Camera_yolo("+str(cam_num)+","+str(buffers)+","+str(port)+","+str(port_message)+",'"+str(ip_number)+"')")   
def get_datetime(ip,port):
       time_date = Time_processing()
       time_date.Date_time_realtime(ip,port)
def rssi_indoor(ip,port):
       rssi_distance = Navigation_sensors() 
       distance = rssi_distance.rssi_distance_converter(ip,port)
       return distance
def GPS_navigation(gpsname,serialdev,baudrate,ip,port): 
           gps_nav = Navigation_sensors() 
           gps_nav.GPS_module_nav(gpsname,serialdev,baudrate,ip,port) 
def GPRS_communication_system(sim800l,command_input,ip,port):
          GPRS_mod = Cellular_networking_com() 
          GPRS_mod.raw_command_input(sim800l,command_input,ip,port)
def Location_cellular_network(sim800l,ip,port):
          GPRS_loc = Cellular_networking_com()
          GPRS_loc.Location_cellular_network(sim800l,ip,port)
