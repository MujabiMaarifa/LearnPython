# Crew_module.py

class Crews:
    def __init__(self, danceCrew, number, performing, position):
        self.danceCrew = danceCrew
        self.number = number
        self.performing = performing
        self.position = position

    def display(self):
        # This method returns a dictionary with crew data
        return {
            'danceCrew': self.danceCrew,
            'number': self.number,
            'performing': 'Yes' if self.performing else 'No',
            'position': self.position
        }
