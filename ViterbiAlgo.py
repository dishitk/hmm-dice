def viterbi(emit, states, init_prob, transition_p, emit_p):
    most_likely_state_sequence = []
    previous_s = None
    possible_sequences = [{}]
    for state in states:
        possible_sequences[0][state] = {"state_prob": init_prob[state] * emit_p[state][emit[0]], "previous_state": None}
    for emission in range(1, len(emit)):
        possible_sequences.append({})
        for state in states:
            max_tran_prob = possible_sequences[emission - 1][states[0]]["state_prob"] * transition_p[states[0]][state]
            prev_state_selected = states[0]
            for prev_st in states[1:]:
                tran_prob = possible_sequences[emission - 1][prev_st]["state_prob"] * transition_p[prev_st][state]
                if tran_prob > max_tran_prob:
                    max_tran_prob = tran_prob
                    prev_state_selected = prev_st
            prob_highest = max_tran_prob * emit_p[state][emit[emission]]
            possible_sequences[emission][state] = {"state_prob": prob_highest, "previous_state": prev_state_selected}

    prob_highest = 0
    for state, state_data in possible_sequences[-1].items():
        if state_data["state_prob"] > prob_highest:
            prob_highest = state_data["state_prob"]
            best_state = state
    most_likely_state_sequence.append(best_state)
    previous_s = best_state

    for sequence in range(len(possible_sequences) - 2, -1, -1):
        most_likely_state_sequence.insert(0, possible_sequences[sequence + 1][previous_s]["previous_state"])
        previous_s = possible_sequences[sequence + 1][previous_s]["previous_state"]
    return most_likely_state_sequence, prob_highest
