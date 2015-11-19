import xml.etree.ElementTree as ET

class xmlreader:
    def __init__(self):
        self.waypoints = []
        self.commands = []
        self.processedcommands = []
    

    def openfile(self,  filepath, callback=None):
        tree = ET.parse(filepath)
        root = tree.getroot()
        for waypoint in root.iter('waypoint'):
            self.waypoints.append(waypoint.attrib)
        
        i = 0
        for command in root.iter('command'):
            self.commandmsg = ""
            self.element =""
            self.command =""
            for element in command.keys():
                if (element != "id" and element != "name"):
                    self.commandmsg = self.commandmsg + element + "=" + command.get(element) + " "
                    self.element = element
            self.command=command
            
            self.commands.append(command.attrib)
            self.commands[i]['msg'] = self.commandmsg
            i = i+1
            
        
        if callback != None :
            callback(self.commands)




