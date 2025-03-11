#https://python-statemachine.readthedocs.io/en/latest/readme.html

import statemachine

class TrafficLight(statemachine.StateMachine):
    red = statemachine.State(initial=True)
    redAndYellow = statemachine.State()
    yellow = statemachine.State()
    green = statemachine.State()

    cycle = (red.to(redAndYellow)|
             redAndYellow.to(green)|
             green.to(yellow)|
             yellow.to(red))

    def on_enter_red(self):
        print("red")
    
    def on_enter_redAndYellow(self):
        print("red/yellow")

    def on_enter_yellow(self):
        print("yellow")
    
    def on_enter_green(self):
        print("green")


light = TrafficLight()

light.cycle()

print(light.current_state)

light.cycle()
light.cycle()
light.cycle()