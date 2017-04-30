import sys

words = set(sys.argv[1:])
print('有{num_words}個不重複的字串:{words}'
        .format(num_words = len(words),words = words))
