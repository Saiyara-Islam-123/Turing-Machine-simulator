class TuringMachine:
    
    def __init__(self, tape, instructions, header = 0, state = "q0"):
        self.tape = tape
        self.instructions = instructions
        self.header = header
        self.state = state
    
    def __str__(self):
        return str(self.tape) + " at index " + str(self.header) + " with instructions " + str(self.instructions) + " and state " + self.state

    #second index of instruction
    def move(self, direction):
        if direction == "R":
            if self.header != len(self.tape) - 1:
                self.header += 1
        elif direction == "L":
            if self.header != 0:
                self.header -= 1
    
    
    def write(self, digit):
        self.tape[self.header] = digit

    def execute(self, instruction):
        if instruction[2] == "1":
            self.write(1)
        elif instruction[2] == "0":
            self.write(0)
        elif instruction[2] == "L":
            self.move("L")
        elif instruction[2] == "R":
            self.move("R")
