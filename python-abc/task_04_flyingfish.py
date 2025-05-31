#!/usr/bin/env python3

class Fish:
    """Fish class representing aquatic animals"""
    
    def swim(self):
        """Standard swimming behavior"""
        print("The fish is swimming")
    
    def habitat(self):
        """Fish habitat"""
        print("The fish lives in water")


class Bird:
    """Bird class representing avian animals"""
    
    def fly(self):
        """Standard flying behavior"""
        print("The bird is flying")
    
    def habitat(self):
        """Bird habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A creature that inherits from both Fish and Bird"""
    
    def fly(self):
        """Override flying behavior"""
        print("The flying fish is soaring!")
    
    def swim(self):
        """Override swimming behavior"""
        print("The flying fish is swimming!")
    
    def habitat(self):
        """Override habitat description"""
        print("The flying fish lives both in water and the sky!")
