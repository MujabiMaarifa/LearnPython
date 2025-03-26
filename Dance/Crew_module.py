# class.py
"""Classes create blueprints to make objects"""
class Crews:
    def __init__(self, danceCrew, number, performing, position):
        self.danceCrew = danceCrew
        self.number = number
        self.performing = performing
        self.position = position

    def display(self) :
        return (f"Dance Crews: {self.danceCrew}\n"
            f"Dance Members Population: {self.number}\n"
            f"Performing: {self.performing}\n"
            f"Position achieved: {self.position}\n")
