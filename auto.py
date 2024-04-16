class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def process_input(self, input_str):
        current_state = self.start_state
        for char in input_str:
            current_state = self.transitions[current_state][char]
        return current_state in self.accept_states

def are_dfa_equivalent(dfa1, dfa2):
    if set(dfa1.alphabet) != set(dfa2.alphabet):
        return False

    marked_pairs = set()
    stack = [(dfa1.start_state, dfa2.start_state)]
    while stack:
        state1, state2 = stack.pop()
        if (state1 in dfa1.accept_states) != (state2 in dfa2.accept_states):
            return False
        for symbol in dfa1.alphabet:
            next_state1 = dfa1.transitions[state1][symbol]
            next_state2 = dfa2.transitions[state2][symbol]
            if (next_state1, next_state2) not in marked_pairs:
                marked_pairs.add((next_state1, next_state2))
                stack.append((next_state1, next_state2))
    return True

def main():
    # DFA 1
    dfa1_states = {'q0', 'q1', 'q2'}
    dfa1_alphabet = {'0', '1'}
    dfa1_transitions = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q1'},
        'q2': {'0': 'q2', '1': 'q1'}
    }
    dfa1_start_state = 'q0'
    dfa1_accept_states = {'q2'}

    dfa1 = DFA(dfa1_states, dfa1_alphabet, dfa1_transitions, dfa1_start_state, dfa1_accept_states)

    # DFA 2
    dfa2_states = {'s0', 's1', 's2'}
    dfa2_alphabet = {'0', '1'}
    dfa2_transitions = {
        's0': {'0': 's0', '1': 's1'},
        's1': {'0': 's2', '1': 's1'},
        's2': {'0': 's2', '1': 's1'}
    }
    dfa2_start_state = 's0'
    dfa2_accept_states = {'s2'}

    dfa2 = DFA(dfa2_states, dfa2_alphabet, dfa2_transitions, dfa2_start_state, dfa2_accept_states)

    if are_dfa_equivalent(dfa1, dfa2):
        print("DFA 1 and DFA 2 are equivalent.")
    else:
        print("DFA 1 and DFA 2 are not equivalent.")

if __name__ == "__main__":
    main()
