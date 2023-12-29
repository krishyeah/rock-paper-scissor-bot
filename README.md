# Rock Paper Scissors Bot

This bot predicts your next rock paper scissors move and attempts to beat you. The boilerplate starter code is from [freecodecamp](https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors).

The bot stores previous move history in order to predict future moves. It stores sets of 5 moves and then finds the most likely move to follow the last 4 moves that the opponent plays. For example, if you played: `Rock`, `Rock`, `Paper`, `Scissors`, the bot will look at your previous move history and will guess your next move based on your most frequent follow up move to the shown sequence. This of course means that the bot performs best against opponents who use a pattern as opposed to an opponent who picks truly randomly.

The bot also requires a large history to increase its win percentage. Against the other bots it has played, which can be seen in [RPS_game.py](RPS_game.py), its combined win/draw percentage is greater than 60%.