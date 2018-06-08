#!/usr/bin/python3
'''Class FileStorage'''

import json
from datetime import datetime
from models.base_model import BaseModel

class FileStorage:
        '''Private class attributes for Class FileStorage'''
        __file_path = 'file.json'
        __objects = {}

        def all(self):
                '''Returns the dictionary with objects'''
                return FileStorage.__objects

        def new(self, obj):
                '''Returns __objects with obj set as key'''
                key = '{}.{}'.format( obj.__class__.__name__, id)
                self.__object[key] = obj

        def save(self):
                '''Serializes __objects to JSON file inside'''
                save_file = self.__file_path
                new_dict = {}
                for key, item in self.__objects.items():
                        if type(obj) is dict:
                                new_dic[key] = item
                        else:
                                new_dict[key] = obj.to_dict()
                with open(save_file, "w+", encoding='utf-8') as new_file:
                        json.dump(new_dict, mew_file)

        def reload(self):
                '''deserializes the JSON file to __objects
                (only if the JSON file exists ; otherwise, do nothing)
                '''
                pass
