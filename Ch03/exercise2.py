import sys

keyword = sys.argv[1]
words = list(sys.argv[2:])
print('{keyword}出現了{num_times}次'
        .format(keyword = keyword, num_times = words.count(keyword)))
