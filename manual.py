class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def proses_input(self, input_str):
        state_saat_ini = self.start_state
        for char in input_str:
            state_saat_ini = self.transitions[state_saat_ini][char]
        return state_saat_ini in self.accept_states

def input_dfa():
    states = input("Masukkan states (dipisahkan dengan koma): ").split(',')
    alphabet = input("Masukkan simbol alfabet (dipisahkan dengan koma): ").split(',')
    transitions = {}
    for state in states:
        transitions[state] = {}
        for symbol in alphabet:
            next_state = input(f"Masukkan state berikutnya dari {state} dengan simbol {symbol}: ")
            transitions[state][symbol] = next_state

    start_state = input("Masukkan state awal: ")
    accept_states = input("Masukkan states penerima (dipisahkan dengan koma): ").split(',')

    return DFA(set(states), set(alphabet), transitions, start_state, set(accept_states))

def apakah_dfa_ekivalen(dfa1, dfa2):
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
    print("Masukkan detail untuk DFA 1:")
    dfa1 = input_dfa()

    print("\nMasukkan detail untuk DFA 2:")
    dfa2 = input_dfa()

    if apakah_dfa_ekivalen(dfa1, dfa2):
        print("\nDFA 1 dan DFA 2 adalah ekivalen.")
    else:
        print("\nDFA 1 dan DFA 2 tidak ekivalen.")

if __name__ == "__main__":
    main()
