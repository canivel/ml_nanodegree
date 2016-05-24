"""Count words."""


def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s
    l_words = []
    rl = s.strip().split(' ')
    for i in rl:
        c = rl.count(i)
        if (i, c) not in l_words:
            c = rl.count(i)
            l_words.append((i, c))

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)

    sl = sorted(l_words, key=lambda tup: (-tup[1], tup[0]))
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return sl[0:n]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
