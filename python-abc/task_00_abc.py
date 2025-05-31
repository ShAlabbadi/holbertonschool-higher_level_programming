#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """A class named Animal using the ABC package."""


@abstractmethod
def sound(self):
    """An abstract method named sound"""
    pass


class Dog(Animal):
    """A subclasses of Animal named 'Dog'"""

    def sound(self):
        """Returns the sound a dog makes"""
        return "Bark"


class Cat(Animal):
    """A subclasses of Animal named 'Cat'"""

    def sound(self):
        """Returns the sound a cat makes"""
        return "Meow"
