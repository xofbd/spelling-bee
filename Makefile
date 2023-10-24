all: clean data/trie.pkl

data:
	mkdir -p $@

data/trie.pkl: | data
	src/build_trie.py --output $@

.PHONY: clean
clean:
	rm -rf data
