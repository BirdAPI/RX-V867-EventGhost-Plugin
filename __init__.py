from rxv867 import *

# expose some information about the plugin through an eg.PluginInfo subclass

eg.RegisterPlugin(
    name = "RX-V867",
    author = "Anthony Casagrande",
    version = "0.9",
    kind = "program",
    createMacrosOnAdd = True,
    url = "",
    description = "Adds actions to control Yamaha RX-V867 (or similar) receiver.",
)

ACTIONS = (   
    ("VolumeUp", "Volume Up", "Increase the volume one step (0.5 dB)", "VolumeUp"),
    ("VolumeDown", "Volume Down", "Decrease the volume one step (0.5 dB)", "VolumeDown"),
    ("VolumeUp_1.0", "Volume Up 1.0dB", "Increase the volume 1.0 dB", "VolumeUp_1.0"),
    ("VolumeDown_1.0", "Volume Down 1.0dB", "Decrease the volume 1.0 dB", "VolumeDown_1.0"),
    ("VolumeUp_1.5", "Volume Up 1.5dB", "Increase the volume 1.5 dB", "VolumeUp_1.5"),
    ("VolumeDown_1.5", "Volume Down 1.5dB", "Decrease the volume 1.5 dB", "VolumeDown_1.5"),
    ("VolumeUp_2.0", "Volume Up 2.0dB", "Increase the volume 2.0 dB", "VolumeUp_2.0"),
    ("VolumeDown_2.0", "Volume Down 2.0dB", "Decrease the volume 2.0 dB", "VolumeDown_2.0"),
    ("VolumeUp_2.5", "Volume Up 2.5dB", "Increase the volume 2.5 dB", "VolumeUp_2.5"),
    ("VolumeDown_2.5", "Volume Down 2.5dB", "Decrease the volume 2.5 dB", "VolumeDown_2.5"),
    ("VolumeUp_3.0", "Volume Up 3.0dB", "Increase the volume 3.0 dB", "VolumeUp_3.0"),
    ("VolumeDown_3.0", "Volume Down 3.0dB", "Decrease the volume 3.0 dB", "VolumeDown_3.0"),
    ("VolumeUp_3.5", "Volume Up 3.5dB", "Increase the volume 3.5 dB", "VolumeUp_3.5"),
    ("VolumeDown_3.5", "Volume Down 3.5dB", "Decrease the volume 3.5 dB", "VolumeDown_3.5"),
    ("VolumeUp_4.0", "Volume Up 4.0dB", "Increase the volume 4.0 dB", "VolumeUp_4.0"),
    ("VolumeDown_4.0", "Volume Down 4.0dB", "Decrease the volume 4.0 dB", "VolumeDown_4.0"),
    ("VolumeUp_4.5", "Volume Up 4.5dB", "Increase the volume 4.5 dB", "VolumeUp_4.5"),
    ("VolumeDown_4.5", "Volume Down 4.5dB", "Decrease the volume 4.5 dB", "VolumeDown_4.5"),
    ("VolumeUp_5.0", "Volume Up 5.0dB", "Increase the volume 5.0 dB", "VolumeUp_5.0"),
    ("VolumeDown_5.0", "Volume Down 5.0dB", "Decrease the volume 5.0 dB", "VolumeDown_5.0"),
    ("ToggleMute", "Toggle Mute", "Toggles mute state", "ToggleMute"),
    ("PowerOff", "Power Off", "Powers off machine", "PowerOff"),
    ("PowerStandby", "Power Standby", "Turns machine to standby", "PowerStandby"),
    ("PowerOn", "Power On", "Powers on machine", "PowerOn"),
    ("ToggleOnStandby", "Toggle On / Standby", "Toggles machine between on and standby", "ToggleOnStandby"),
    ("Source_HDMI1", "Source HDMI1", "Changes source to HDMI1", "Source_HDMI1"),
    ("Source_HDMI2", "Source HDMI2", "Changes source to HDMI2", "Source_HDMI2"),
    ("Source_HDMI3", "Source HDMI3", "Changes source to HDMI3", "Source_HDMI3"),
    ("Source_HDMI4", "Source HDMI4", "Changes source to HDMI4", "Source_HDMI4"),
    ("Source_HDMI5", "Source HDMI5", "Changes source to HDMI5", "Source_HDMI5"),
    ("Source_HDMI6", "Source HDMI6", "Changes source to HDMI6", "Source_HDMI6"),
    ("Source_HDMI7", "Source HDMI7", "Changes source to HDMI7", "Source_HDMI7"),
    ("Source_HDMI8", "Source HDMI8", "Changes source to HDMI8", "Source_HDMI8"),
    ("Source_HDMI9", "Source HDMI9", "Changes source to HDMI9", "Source_HDMI9"),
    ("Source_V-AUX", "Source V-AUX", "Changes source to V-AUX", "Source_V-AUX"),
    ("Source_AV1", "Source AV1", "Changes source to AV1", "Source_AV1"),
    ("Source_AV2", "Source AV2", "Changes source to AV2", "Source_AV2"),
    ("Source_AV3", "Source AV3", "Changes source to AV3", "Source_AV3"),
    ("Source_AV4", "Source AV4", "Changes source to AV4", "Source_AV4"),
    ("Source_AV5", "Source AV5", "Changes source to AV5", "Source_AV5"),
    ("Source_AV6", "Source AV6", "Changes source to AV6", "Source_AV6"),
    ("Source_TUNER", "Source Tuner", "Changes source to radio", "Source_TUNER"),
    ("Straight", "Straight", "Straight", "Straight"),
    ("SurroundDecode", "Surround Decode", "Surround Decode", "SurroundDecode"),
    ("ToggleStraightAndDecode", "Toggle Straight And Decode", "Toggles between Straight and Sourround Decode", "ToggleStraightAndDecode"),
    ("ToogleEnhancer", "Toggle Enhancer", "Toggles the enhancer on and off", "ToggleEnhancer"),
    #("NextSource", "Next Source", "Goes to the next source", "NextSource"),
    #("PreviousSource", "Previous Source", "Goes to the previous source", "PreviousSource"),
    #("ToggleSleep", "Toggle Sleep", "Toggles sleep mode", "ToggleSleep"),
    ("NextRadioPreset", "Next Radio Preset", "Goes to next radio preset, or if radio is not on, it turns it on. Also wraps when you go past the last preset.", "NextRadioPreset"),
    ("PreviousRadioPreset", "Previous Radio Preset", "Goes to previous radio preset, or if radio is not on, it turns it on. Also wraps to the end when you go past the first preset.", "PreviousRadioPreset"),
    ("ToggleRadioAMFM", "Toggle Radio AM / FM", "Toggles radio between AM and FM", "ToggleRadioAMFM"),
    ("RadioAutoFreqUp", "Radio Auto Freq Up", "Auto increases the radio frequency", "RadioAutoFreqUp"),
    ("RadioAtuoFreqDown", "Radio Auto Freq Down", "Auto decreases the radio frequency", "RadioAutoFreqDown"),
    ("RadioFreqUp", "Radio Freq Up", "Increases the radio frequency", "RadioFreqUp"),
    ("RadioFreqDown", "Radio Freq Down", "Decreases the radio frequency", "RadioFreqDown"),
	("Scene1", "Scene 1", "Changes the current scene to be Scene 1", "Scene1"),
	("Scene2", "Scene 2", "Changes the current scene to be Scene 2", "Scene2"),
	("Scene3", "Scene 3", "Changes the current scene to be Scene 3", "Scene3"),
	("Scene4", "Scene 4", "Changes the current scene to be Scene 4", "Scene4"),
	("Scene5", "Scene 5", "Changes the current scene to be Scene 5", "Scene5"),
	("Scene6", "Scene 6", "Changes the current scene to be Scene 6", "Scene6"),
	("Scene7", "Scene 7", "Changes the current scene to be Scene 7", "Scene7"),
	("Scene8", "Scene 8", "Changes the current scene to be Scene 8", "Scene8"),
	("Scene9", "Scene 9", "Changes the current scene to be Scene 9", "Scene9"),
	("Scene10", "Scene 10", "Changes the current scene to be Scene 10", "Scene10"),
	("Scene11", "Scene 11", "Changes the current scene to be Scene 11", "Scene11"),
	("Scene12", "Scene 12", "Changes the current scene to be Scene 12", "Scene12"),
)    

class ActionPrototype(eg.ActionClass):
    def __call__(self):
        try:
            self.plugin.rxv867.send_action(self.value, ACTION_BUTTON)
        except:
            raise self.Exceptions.ProgramNotRunning

class RXV867(eg.PluginClass):
    def __init__(self):
        self.AddActionsFromList(ACTIONS, ActionPrototype)
        self.rxv867 = RXV867Client()
