CHIP-8 Information

* 35 opcodes, all 2 bytes 
* 4K memory 
* 16 8-bit registers 
* address register, I, for memory operations 
* 2048 pixels (64 x 32)
* 2 timer registers 

the interpreter occupies the first 512 bytes (up to 0x200), so an offset is required for else. (0x000 -> 0x200)

