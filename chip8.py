import pyglet 
import sys 

class Chip(pyglet.window.Window):
    def initialize(self):
        self.key_inputs = [0] * 16
        self.display_buffer = [0] * 64 * 32 # 64 x 32 pixels 
        self.memory = [0] * 4096 # 4KB
        self.gpio = [0] * 16 # 16 general purpose registers
        # Two timer registers that count at 60Hz
        self.sound_timer = 0
        self.delay_timer = 0
        # Index/address register (I), which stores memory addresses for use in operations
        self.index = 0 
        # Program counter (PC), which stores the address of the current instruction
        self.pc = 0
        # Stack pointer (SP), includes the address of the current top of the stack, which is 16 levels deep
        self.sp = []

    def main(self):
        self.initialize()
        self.load_rom(sys.argv[1])
