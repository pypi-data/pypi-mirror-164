'''
Author: Hendrik Koester
Date: 23/08/2022
Version: 1.0.2
'''
import requests
from lxml import etree

class nerdlerxml:
    '''
    Converts XML to a dictionary. Can take inputs from URL, a file and binary data
    Args:
        url:str -> default None
        filepath:str -> default None
        fileobject:bytes -> default None
    
    One arg have to be injected during init!

    Example: object nerdlerxml(url="https://example.org/example.xml").to_dict()
    '''
    def __init__(self,url:str=None,filepath:str=None,fileobject:bytes=None)->None:
        self.bytes = None
        self.tree = None
        self._validate_inputs(url=url,filepath=filepath,fileobject=fileobject)
        self._to_tree(xml=self.bytes)

    def _validate_inputs(self,url,filepath,fileobject)->None:
        '''
        Validates if data is injected
        '''
        if url != None:
            self.bytes = self._get_xml_from_url(url=url)
        elif filepath != None:
            '''
            read in file in bytes
            '''
            with open(filepath, "rb") as f:
                self.bytes = f.read()
        elif fileobject != None:
            self.bytes = fileobject
            self.fileobject = None
        else:
            raise AttributeError("No url, filepath or fileobject given")

    def _get_xml_from_url(self,url:str)->bytes:
        '''
        Receives data from URL in bytes
        '''
        return requests.request("GET", url, headers={}, data={}).content

    def _to_tree(self,xml)->None:
        '''
        Parsing XML and generates a tree
        '''
        self.tree = etree.fromstring(xml)

    def _get_key(self,element)->None:
        '''
        Returning the key during converting into dictionary
        '''
        return element.tag.split('}')[1] if '}' in element.tag else element.tag

    def _get_value(self,element)->None:
        '''
        Returning the value during converting into dictionary
        '''
        return element.text if element.text and element.text.strip() else self._convert_element(element)

    def _convert_element(self,tree)->dict:
        '''
        Converting XML tree to dictionary
        '''
        result = {}

        for element in tree.iterchildren():
            key = self._get_key(element)
            val = self._get_value(element)

            if key in result:                
                if type(result[key]) is list:
                    result[key].append(val)
                else:
                    temp = result[key].copy()
                    result[key] = [temp, val]
            else:
                result[key] = val

        return result

    def to_dict(self)->dict:
        '''
        End user wrapper for convert
        '''
        return self._convert_element(self.tree)