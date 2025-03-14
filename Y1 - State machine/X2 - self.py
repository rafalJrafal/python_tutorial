from statemachine import State
from statemachine import StateMachine
from statemachine import Event

class States(StateMachine):
    draft = State(initial=True)

    externalTransition = draft.to.itself(event=("ext", "external"))
    internalTransition = draft.to.itself(internal=True, event=("int", "internal"))

    def on_enter_draft(self):
        print("On enter draft state")

    def on_transition(self, event, state):
        print(f"On '{event}', on the '{state.id}' state.")

    def on_exit_state(self, event, state):
        print(f"Exiting '{state.id}' state from '{event}' event.")

    def on_enter_state(self, event, state):
        print(f"Entering '{state.id}' state from '{event}' event.")

print("INIT")
s = States()
print("INTERNAL TRANISTION")
s.internalTransition()
print("EXTERNAL TRANISTION")
s.externalTransition()
print("EVENT")
s.send("ext")