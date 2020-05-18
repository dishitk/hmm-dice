import pre_processing
import ViterbiAlgo as V

if __name__ == "__main__":
    states = ['D1', 'D2', 'D3']
    prob_initial = {'D1': 0.333, 'D2': 0.333, 'D3': 0.333}
    prob_sameDice, emissionProb_d1, emissionProb_d2, emissionProb_d3, emissions = pre_processing.file_read("hmm_dice_1586654669612.txt")
    prob_transition = {
        'D1': {'D2': ((1 - prob_sameDice) / 2), 'D3': ((1 - prob_sameDice) / 2), 'D1': prob_sameDice},
        'D2': {'D1': ((1 - prob_sameDice) / 2), 'D3': ((1 - prob_sameDice) / 2), 'D2': prob_sameDice},
        'D3': {'D1': ((1 - prob_sameDice) / 2), 'D2': ((1 - prob_sameDice) / 2), 'D3': prob_sameDice},
    }
    prob_emissions = {
        'D1': {'1': float(emissionProb_d1[0]), '2': float(emissionProb_d1[1]), '3': float(emissionProb_d1[2])},
        'D2': {'1': float(emissionProb_d2[0]), '2': float(emissionProb_d2[1]), '3': float(emissionProb_d2[2])},
        'D3': {'1': float(emissionProb_d3[0]), '2': float(emissionProb_d3[1]), '3': float(emissionProb_d3[2])}
    }
    mle_sequence, prob_sequence = V.viterbi(emissions, states, prob_initial, prob_transition, prob_emissions)
    print("Most Likely State Sequence is: " + ' '.join(mle_sequence))
    print("Probability of the above sequence is: ", prob_sequence)
