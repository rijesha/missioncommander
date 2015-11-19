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
            for element in command:
                if element == "id":
                    print("do Nothing")
                elif element == "name":
                    print("do Nothing")
                else:
                    self.commandmsg = self.commandmsg + element + ":" + command.get(element)
            self.commands.append(command.attrib)
            self.commands[i]['msg'] = self.commandmsg                   
            
        
        if callback != None :
            callback(self.commands)




