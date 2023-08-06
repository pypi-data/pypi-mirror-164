from state.finite_state_machine.config import INITIAL_STATE, STATE_MACHINE, TRANSITIONS, TIMESTAMP, PREVIOUS_STATE, \
    NEW_STATE


class ElementFiniteStateMachine:
    def __init__(self, config: dict):
        """
        Initialize the FiniteElementStateMachine.

        :param config: dict. The configuration of the FiniteElementStateMachine.
        """
        self.history = []
        self.current_state = config[INITIAL_STATE]
        self.transitions = config[TRANSITIONS]
        self.state_machine = config[STATE_MACHINE]

    def update_state(self, prev_element_state, current_element_state):
        """
        Update the current state of the FiniteElementStateMachine.

        :param prev_element_state: ElementState or Child Class. The previous element state.
        :param current_element_state: ElementState. The current element state.
        """
        current_state_transitions = self.state_machine[self.current_state]
        for transition_id, target_state in current_state_transitions.items():
            if self.transitions[transition_id](prev_element_state, current_element_state):
                self.history.append({
                    TIMESTAMP: current_element_state.timestamp,
                    PREVIOUS_STATE: self.current_state,
                    NEW_STATE: target_state
                })
                self.current_state = target_state
                break