from statemachine import State
from statemachine import StateMachine
from statemachine import Event

from statemachine.contrib.diagram import DotGraphMachine

class machine(StateMachine):
    init = State(initial = True)
    running = State()

    run = init.to(running)
    stop = running.to(init)

    @running.enter
    def startRunning(self):
        print("running!!")

    @running.exit
    def stopRunning(self):
        print("stop!")

m = machine()

m.run()
m.stop()

graph = DotGraphMachine(m)
dot = graph()
print(dot.to_string())
dot.write("./1.txt")

dot.write_png("1.png")