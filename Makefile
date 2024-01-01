all: clean data/trie.pkl

data:
	mkdir -p $@

data/trie.pkl: | data
	src/build_trie.py --output $@

data/dict: | data
	wget -O $@ https://raw.githubusercontent.com/freebee-game/enable/master/enable1.txt
	touch $@

.PHONY: clean
clean:
	rm -rf data src/__pycache__
