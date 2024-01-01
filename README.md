# Solver for Spelling Bee
A command line solver for New York Times' spelling bee puzzle. You can play a similar game [here](https://6mal5.com/wortendo/).

## Usage
Run `src/spelling_bee.py --help` for usage info. There are two possible approaches:
1. Iterating over a dictionary
1. Building a [trie data structure](https://en.wikipedia.org/wiki/Trie) and using that to look up words

For either approach, you'll need a dictionary to run the solver. In Linux, dictionaries are located in /usr/share/dict. If you need a dictionary, you can download this [one](https://raw.githubusercontent.com/freebee-game/enable/master/enable1.txt). For the trie based approached, you'll need to first build the trie with the `src/build_trie.py` script. You can do so easily with the `Makefile`. The `src/spelling_bee.py` script knows which approach to run based on how it's called. Once again, refer to the usage info.

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information.
