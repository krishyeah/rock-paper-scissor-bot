def player(prev_play, opponent_history=[], seq_freq = {}):
    rps_rules = {'P': 'S', 'R': 'P', 'S': 'R'}

    if not prev_play:
        # for first move, assume scissors
        prev_play = 'S'

    # opponent_history tracks the history of all moves played by the opponent
    opponent_history.append(prev_play)

    # initialize prediction to rock
    prediction = 'R'

    if len(opponent_history) >= 5:
        # last sequence of 5 moves by opponent
        last_seq = ''.join(opponent_history[-5:])
        # update the frequency of the last sequence appearance
        seq_freq[last_seq] = seq_freq.get(last_seq, 0) + 1
        
        # list of possible next sequences using last 4 recent moves and possible next moves
        next_seq_poss = [''.join([*opponent_history[-4:], next_move]) for next_move in ['R', 'P', 'S']]

        # find the highest frequency sequence based on previous history
        # ensure we don't have look up errors by only searching for sequences that have occurred
        next_seq_freq = {seq: seq_freq[seq] for seq in next_seq_poss if seq in seq_freq}
        
        # dictionary will only be populated if this sequnece has been previously seen
        if next_seq_freq:
            # get last move of the most seen sequence
            prediction = max(next_seq_freq, key=next_seq_freq.get)[-1]
    
    next_move = rps_rules[prediction]
    return next_move