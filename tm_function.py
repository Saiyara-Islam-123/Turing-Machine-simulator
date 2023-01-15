import turing_machine as tm

def tm_function(tm_object):
    for i in range(9000):
        for instruction in tm_object.instructions:
            for i in range(len(instruction)):
                if instruction[0] == tm_object.state and int(instruction[1]) == tm_object.tape[tm_object.header]:
                    tm_object.execute(instruction)
        