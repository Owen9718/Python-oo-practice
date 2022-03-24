"""Word Finder: finds random words from a dictionary."""

# cont = open('words.txt', 'r')



# x = 0
# lst = []
# for word in cont:
#     x += 1
#     new_word = word.strip()
#     lst.append(new_word)

# print(f'{x} words read')
# print(lst)
import random
class WordFinder:
    ...
    def __init__(self,path):
        self.path = path
        self.cont = open(path, 'r')
        self.lst = []
        for word in self.cont:
            new_word = word.strip()
            self.lst.append(new_word)
        print(f'{len(self.lst)} words read')

    def random(self):
        return random.choice(self.lst)