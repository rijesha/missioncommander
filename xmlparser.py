import xml.etree.ElementTree as ET

class xmlreader:
    def __init__(self):
        self.waypoints = []
        self.commands = []
    

    def openfile(self, filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()
        for waypoint in root.iter('waypoint'):
            waypoints.append(waypoint.attrib)

        for command in root.iter('command'):
            commands.append(waypoint.attrib)
