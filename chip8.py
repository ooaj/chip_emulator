import pyglet 
import sys 

class Chip(pyglet.window.Window):
    def initialize(self):
        self.clear()
        self.key_inputs = [0] * 16
        self.display_buffer = [0] * 64 * 32 # 64 x 32 pixels 
        self.memory = [0] * 4096 # 4KB
        self.gpio = [0] * 16 # 16 general purpose registers
        # Two timer registers that count at 60Hz
        self.sound_timer = 0
        self.delay_timer = 0
        self.should_draw = False # Flag to indicate if the screen should be redrawn
        self.opcode = 0 # Current opcode
        # Index/address register (I), which stores memory addresses for use in operations
        self.index = 0 
        # Program counter (PC), which stores the address of the current instruction
        self.pc = 0
        # Stack pointer (SP), includes the address of the current top of the stack, which is 16 levels deep
        self.sp = 0x200
        
        i = 0
        while i < 80:
            self.memory[i] = self.fonts[i]
            i += 1
    def _0ZZZZ(self):
        extracted_op = self.opcode & 0x00ff
        try: 
            self.funcmap[extracted_op]() 
        except:
            print("Unknown opcode: 0x%x" % self.opcode)
    def load_rom(self, rom_path):
        """Load a ROM file into memory"""
        log("Loading %s.." % rom_path)
        binary = open(rom_path, 'rb').read()
        i = 0  
        while i < len(binary):
            self.memory[0x200 + i] = binary[i]
            i += 1
    def cycle(self):
        """Fetch, decode, and execute an opcode"""
        self.opcode = self.memory[self.pc]

        # Decode opcode
        self.vx = (self.opcode & 0x0f00) >> 8
        self.vy = (self.opcode & 0x00f0) >> 4
        self.pc += 2 # Move to next opcode, each opcode is 2 bytes long 

        extracted_op = self.opcode & 0xf000
        try:
            self.funcmap[extracted_op]() # Call the function that corresponds to the opcode
        except:
            print("Unknown opcode: 0x%x" % self.opcode)

        # Update timers
        if self.delay_timer > 0:
            self.delay_timer -= 1
        if self.sound_timer > 0:
            self.sound_timer -= 1
            if self.sound_timer == 0:
                log("BEEP!")

    def main(self):
        self.initialize()
        self.load_rom(sys.argv[1])
