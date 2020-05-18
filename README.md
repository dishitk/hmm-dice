# hmm-dice
Hidden Markov Model Application

Consider a casino game, where the dealer is a three-sided dice with labels 1, 2, and 3. The dealer has three loaded dice D1 D2 D3. For die Di, the probability of rolling the number j is pij. At each turn, the dealer must decide whether to: (1) keep the same die; (2) switch to one of the other two dice randomly. She chooses (1) with probability p and (2) with probability 1-p. At the beginning the dealer chooses any of 3 dice with equal probability.

Structure of the Input File:
All lines that begin with # (hash/pound sign) are comments and can be ignored.
First Line of the file has probability of keeping the same dice.
p
Next 3 lines of the input file have:
p11, p12, p13
p21, p22, p23
p31, p32, p33

Then, there is X, which is a list of 100 labels 1,2,3 corresponding to the emissions (observations).

Output:
A sequence of states which best explains the sequence of rolls and the probability of the sequence.
