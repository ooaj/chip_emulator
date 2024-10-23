
class Chip:
    def initialize(self):
        self.key_inputs = [0] * 16
        self.display_buffer = [0] * 64 * 32 # 64 x 32 pixels 