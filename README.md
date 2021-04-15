# TIC TAC TOE

This is a tic-tac-toe game implemented with an AI as an opponent. As a project
created at first as a school project, I implemented the game in an advanced package manner so later it can be improved and add more amazing AI algorithms
to it.

Feel free to discover, improve and use this software as you please.

## Installation

This project run with Python 3.8.0 or higher. Some of the packages included here might have compatibility issues so I won't risk it.

```bash
$ pip install -r requirements.txt
```

## Usage

I tried arranging this in a detailed package manner so I suggest using it as a module. Starting the game should be done with:
```bash
$ python -m tic-tac-toe
```

To actually play the game and place a marker, you will be asked for the x and y coordinates that both can range from 0 to 2.

> Note: At any given time during input you can pass `exit` as a command to stop
the program

## Configuration

Configuration for texts and parameters is found in `config.yaml` obviously.

You can change the configuration so the algorithm can be set to not use the alpha-beta pruning.
