from algopy import ARC4Contract, String
from algopy.arc4 import abimethod


class AtomTrade(ARC4Contract):
    def __init__(self):
        self.name = String(16)
        self.message = String(16)
    


    
    
