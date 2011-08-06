#!/usr/bin/python

from xml.dom import minidom
import httplib
import urllib
import re

ACTION_EXECBUILTIN = 0x01
ACTION_BUTTON      = 0x02

IP_ADDRESS = "192.168.1.22"
PORT = "80"

def print_status():
    print get_status()

def print_tuner_status():
    print get_tuner_status()

def print_tuner_presets():
    print get_tuner_presets()
    
def get_xml(XML):
    conn = httplib.HTTPConnection("%s:%s" % ( IP_ADDRESS, PORT ))
    headers = { "Content-type": "text/xml" }
    conn.request("POST", "/YamahaRemoteControl/ctrl", "", headers)
    conn.send(XML)
    response = conn.getresponse()
    rval = response.read()
    conn.close()
    return rval

def get_status():
    return get_xml('<YAMAHA_AV cmd="GET"><Main_Zone><Basic_Status>GetParam</Basic_Status></Main_Zone></YAMAHA_AV>')

def get_tuner_status():
    return get_xml('<YAMAHA_AV cmd="GET"><Tuner><Play_Info>GetParam</Play_Info></Tuner></YAMAHA_AV>')

def get_tuner_presets():
    return get_xml('<YAMAHA_AV cmd="GET"><Tuner><Play_Control><Preset><Data>GetParam</Data></Preset></Play_Control></Tuner></YAMAHA_AV>')
    
def send_xml(XML):
    conn = httplib.HTTPConnection("192.168.1.22:80")
    headers = { "Content-type": "text/xml" }
    conn.request("POST", "/YamahaRemoteControl/ctrl", "", headers)
    conn.send(XML)
    conn.close()

def increase_volume(inc = 0.5):
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Volume><Lvl><Val>%i</Val><Exp>1</Exp><Unit>dB</Unit></Lvl></Volume></Main_Zone></YAMAHA_AV>' % int(get_volume() + 10 * inc))
    
def decrease_volume(dec = 0.5):
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Volume><Lvl><Val>%i</Val><Exp>1</Exp><Unit>dB</Unit></Lvl></Volume></Main_Zone></YAMAHA_AV>' % int(get_volume() - 10 * dec))

def change_volume(diff):
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Volume><Lvl><Val>%i</Val><Exp>1</Exp><Unit>dB</Unit></Lvl></Volume></Main_Zone></YAMAHA_AV>' % int(get_volume() + 10 * diff))
    
def get_volume():
    return get_int_param('Val')
    
def set_volume(value):
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Volume><Lvl><Val>%i</Val><Exp>1</Exp><Unit>dB</Unit></Lvl></Volume></Main_Zone></YAMAHA_AV>' % int(value * 10.0))

def mute_on():
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Volume><Mute>On</Mute></Volume></Main_Zone></YAMAHA_AV>')

def mute_off():
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Volume><Mute>Off</Mute></Volume></Main_Zone></YAMAHA_AV>')

def get_mute():
    return get_is_param_on('Mute')

def power_on():
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Power_Control><Power>On</Power></Power_Control></Main_Zone></YAMAHA_AV>')
    
def power_off():
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Power_Control><Power>Off</Power></Power_Control></Main_Zone></YAMAHA_AV>')
    
def power_standby():
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Power_Control><Power>Standby</Power></Power_Control></Main_Zone></YAMAHA_AV>')
    
def toggle_on_standby():
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Power_Control><Power>On/Standby</Power></Power_Control></Main_Zone></YAMAHA_AV>')    
    
def toggle_mute():
    if get_mute():
        mute_off()
    else:
        mute_on()

def change_source(source):
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Input><Input_Sel>%s</Input_Sel></Input></Main_Zone></YAMAHA_AV>' % source)

def straight():
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Surround><Program_Sel><Current><Straight>On</Straight><Sound_Program>Straight</Sound_Program></Current></Program_Sel></Surround></Main_Zone></YAMAHA_AV>')

def surround_decode():
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Surround><Program_Sel><Current><Straight>Off</Straight><Sound_Program>Surround Decoder</Sound_Program></Current></Program_Sel></Surround></Main_Zone></YAMAHA_AV>')

def toggle_straight_decode():
    if get_straight():
        surround_decode()
    else:
        straight()
    
def get_straight():
    return get_is_param_on('Straight')

def set_enhancer(arg):
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Surround><Program_Sel><Current><Enhancer>%s</Enhancer></Current></Program_Sel></Surround></Main_Zone></YAMAHA_AV>' % arg)

def get_enhancer():
    return get_is_param_on('Enhancer')

def get_sound_program_name():
    return get_string_param('Sound_Program')
    
def get_source_number():
    return get_int_param('Src_Number')

def get_is_param_on(param):
    return get_string_param(param) == "On"

def get_int_param(param):
    return int(get_string_param(param))
    
def get_string_param(param):
    xml = get_status()
    xmldoc = minidom.parseString(xml)
    value = xmldoc.getElementsByTagName(param)[0].firstChild.data
    return value

def get_is_tuner_param_on(param):
    return get_string_tuner_param(param) == "On"    
    
def get_int_tuner_param(param):
    return int(get_string_tuner_param(param))    
    
def get_string_tuner_param(param):
    xml = get_tuner_status()
    xmldoc = minidom.parseString(xml)
    value = xmldoc.getElementsByTagName(param)[0].firstChild.data
    return value
    
def toggle_enhancer():
    if get_enhancer():
        set_enhancer("Off")
    else:
        set_enhancer("On")

def next_source():
    set_source_number(get_source_number() + 1)

def previous_source():
    set_source_number(get_source_number() - 1)

def set_source_number(num):
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Input><Current_Input_Sel_Item><Src_Number>%i</Src_Number></Current_Input_Sel_Item></Input></Main_Zone></YAMAHA_AV>' % num)

def set_sleep(arg):
    send_xml('<YAMAHA_AV cmd="PUT"><Main_Zone><Power_Control><Sleep>On</Sleep></Power_Control></Main_Zone></YAMAHA_AV>')  
    
def toggle_sleep():
    if (get_is_param_on('Sleep')):
        set_sleep('Off')
    else:
        set_sleep('On')

def set_radio_preset(preset):
    send_xml('<YAMAHA_AV cmd="PUT"><Tuner><Play_Control><Preset><Preset_Sel>%i</Preset_Sel></Preset></Play_Control></Tuner></YAMAHA_AV>' % preset)

def get_radio_band():
    return get_string_tuner_param('Band')

def toggle_radio_amfm():
    if get_radio_band() == 'FM':
        set_radio_band('AM')
    else:
        set_radio_band('FM')
    
def set_radio_band(band):
    send_xml('<YAMAHA_AV cmd="PUT"><Tuner><Play_Control><Tuning><Band>%s</Band></Tuning></Play_Control></Tuner></YAMAHA_AV>' % band)
     
def next_radio_preset_old():
    if is_radio_on():
        oldpreset = get_int_tuner_param('Preset_Sel')
        preset = oldpreset + 1
        set_radio_preset(preset)
        count = get_radio_preset_count()
        if preset > count:
            preset = 1
            set_radio_preset(preset)
    else:
        change_source('TUNER')

def next_radio_preset():
	
		
def previous_radio_preset():
    if is_radio_on():
        oldpreset = get_int_tuner_param('Preset_Sel')
        preset = oldpreset - 1
        set_radio_preset(preset)
        count = get_radio_preset_count()
        if preset < 1:
            preset = count
            set_radio_preset(preset)
    else:
        change_source('TUNER')    

def is_radio_on():
    return get_string_param('Input_Sel') == "TUNER"
        
def auto_radio_freq(updown):
    send_xml('<YAMAHA_AV cmd="PUT"><Tuner><Play_Control><Auto_Freq>%s</Auto_Freq></Play_Control></Tuner></YAMAHA_AV>' % updown)

def manual_radio_freq(updown):
    send_xml('<YAMAHA_AV cmd="PUT"><Tuner><Play_Control><Tuning><Freq>%s</Freq></Tuning></Play_Control></Tuner></YAMAHA_AV>' % updown)    
    
def set_radio_freq(freq):
    print "Not implemented!"

def get_radio_preset_count():
    xml = get_tuner_presets()
    xmldoc = minidom.parseString(xml)
    count = 0
    done = False
    while ((not done) and count <= 40):
        num = "Number_%s" % (count + 1)
        value = xmldoc.getElementsByTagName(num)[0].getElementsByTagName('Status')[0].firstChild.data
        if value == 'Exist':
            count = count + 1
        else:
            done = True
    return count
        
class RXV867Client:
    def __init__(self):
        print "Init"

    def send_action(self, msg = "", type = ACTION_EXECBUILTIN):
        if msg == 'VolumeUp':
            increase_volume()
        elif msg == 'VolumeDown':
            decrease_volume()
        elif msg == 'ToggleMute':
            toggle_mute()
        elif msg == "PowerOn":
            power_on()
        elif msg == "PowerOff":
            power_off()
        elif msg == "PowerStandby":
            power_standby()    
        elif msg == "ToggleOnStandby":
            toggle_on_standby()  
        elif msg == "Source_HDMI1":
            change_source("HDMI1")
        elif msg == "Source_HDMI2":
            change_source("HDMI2")
        elif msg == "Source_HDMI3":
            change_source("HDMI3")
        elif msg == "Source_HDMI4":
            change_source("HDMI4")
        elif msg == "Source_HDMI5":
            change_source("HDMI5")
        elif msg == "Source_AV1":
            change_source("AV1")
        elif msg == "Source_AV2":
            change_source("AV2")
        elif msg == "Source_AV3":
            change_source("AV13")
        elif msg == "Source_AV4":
            change_source("AV4")
        elif msg == "Source_AV5":
            change_source("AV5")
        elif msg == "Source_AV6":
            change_source("AV6")
        elif msg == "Source_Radio":
            change_source("TUNER")
        elif msg == "Source_V_AUX":
            change_source("V-AUX")
        elif msg == "Straight":
            straight()
        elif msg == "SurroundDecode":
            surround_decode()
        elif msg == "ToggleStraightAndDecode":
            toggle_straight_decode()
        elif msg == "ToggleEnhancer":
            toggle_enhancer()
        elif msg == "PreviousSource":
            next_source()
        elif msg == "NextSource":
            previous_source()
        elif msg == "ToggleSleep":
            toggle_sleep()
        elif msg == "NextRadioPreset":
            next_radio_preset()
        elif msg == "PreviousRadioPreset":
            previous_radio_preset()
        elif msg == "ToggleRadioAMFM":
            toggle_radio_amfm();
        elif msg == "RadioAutoFeqUp":
            auto_radio_freq('Up')
        elif msg == "RadioAutoFreqDown":
            auto_radio_freq('Down')
        elif msg == "RadioFeqUp":
            manual_radio_freq('Up')
        elif msg == "RadioFreqDown":
            manual_radio_freq('Down')
            
            
            