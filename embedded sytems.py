def dishwasher():
    print("A dishwasher is an embedded device because it has one function")
    print("Function: Wash and clean dishes")
    print("User Interface: Display with buttons to control settings")
    print("Inputs: Buttons used to set wash time, buttons used to set temperature")
    print("Outputs: Noise when finished, message on display screen, clean dishes")

def microwave():
    print("A microwave is an embedded device because it has one function")
    print("Function: Cook and heat food")
    print("User Interface: Display with buttons")
    print("Inputs: Buttons and dials to control time and power")
    print("Outputs: Noise when finished, hot food")

def digitalCam():
    print("A digital camera is an embedded device because it has one function")
    print("Function: Take photos and videos")
    print("User Interface: Display with buttons and dials")
    print("Inputs: Buttons and dials to change settings and take photos and videos")
    print("Outputs: Photo and video on screen")

def trafficLights():
    print("Traffic lights are an embedded device because it has one function")
    print("Function: Tell people when to cross the road and tell cars when to stop and go")
    print("User Interface: Button")
    print("Inputs: Button to tell it that there is sombody waiting to cross")
    print("Outputs: Red, yeloow and green lights")

def washingMachine():
    print("A washing machine is an embedded device because it has one function")
    print("Function: Clean clothes")
    print("User Interface: Display with buttons to change settings")
    print("Inputs: Buttons to change temperature and time")
    print("Outputs: Noise when finished, message on display, clean clothes")

def satNav():
    print("A sat nav is an embedded device because it has one function")
    print("Function: Give directions")
    print("User Interface: Display with touchscreen")
    print("Inputs: Touchscreen to change destination")
    print("Outputs: Directions on screen")

def cpu():
    print("The CPU completes all instructions, completes the Fetch-Execute cycle \nALU - Arithmetic Logic Unit - Performs all arithmetic and logical operations \nCache - Stores frequently used instructions for fast retrieval because it is located on or close to the CPU")

def mar():
    print("Memory Address Register \nThe MAR stores the address of the data that will be fetched \nTells where data will be stored in memory")

def mdr():
    print("Memory Data Register \nHold data that is being sent to and from memory")

def pc():
    print("Program Counter \nPoints to the next instruction to be executed \nKeeps the instructions in sequence")

def acc():
    print("

device = input("Enter the name of an embedded device \n1.Dishwasher \n2.Microwave \n3.Digital Camera \n4.Traffic Lights \n5.Washing Machine \n6.Sat Nav \n")
if device.lower() == "dishwasher":
    dishwasher()
if device.lower() == "microwave":
    microwave()
if device.lower() == "digital camera":
    digitalCam()
if device.lower() == "traffic lights":
    trafficLights()
if device.lower() == "washing machine":
    washingMachine()
if device.lower() == "sat nav":
    satNav()

fact = input("\n \nName of CPU component \n1.CPU \n2.MAR \n3.MDR \n4.PC \n5.ACC \n5.CPU performance factors \n")
if fact.lower() == "CPU":
    cpu()
