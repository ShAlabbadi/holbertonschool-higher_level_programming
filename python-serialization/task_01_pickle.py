#!/usr/bin/python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to a file.
        
        Args:
            filename: The filename to save the serialized object
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a file.
        
        Args:
            filename: The filename to load the serialized object from
            
        Returns:
            An instance of CustomObject or None if deserialization fails
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            return None
