#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    
    Args:
        dictionary: The Python dictionary to serialize
        filename: The filename to save the XML data
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file to a Python dictionary.
    
    Args:
        filename: The filename to read the XML data from
        
    Returns:
        A Python dictionary with the deserialized data
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result = {}
        for child in root:
            result[child.tag] = child.text
            
        return result
    except Exception as e:
        return None
