from statemachine import State, StateMachine
from statemachine.contrib.diagram import DotGraphMachine

class stateM(StateMachine):
    init = State(initial=True)
    run = State()
    fforward = State()
    next = State()

    def isLongPress(self):
        return True
    
    def isShortPress(self):
        return False

    t_go = init.to(run)
    t_ffpressed = run.to(fforward, cond=isLongPress)
    t_ffpressed = run.to(next, cond=isShortPress)
    stop = fforward.to(init) | next.to(init)

m = stateM()
graph = DotGraphMachine(m)
graph().write_png("2.png")