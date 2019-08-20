import sys
from io import TextIOWrapper
sys.stdout = TextIOWrapper(
    sys.stdout.buffer, encoding='UTF-8', errors='replace')

club = u"club -> \u2663"
diamond = u"diamond -> \u2666"
heart = u"hearts -> \u2665"
spade = u"spade -> \u2660"

suits = [r"\u2663'", r"\u2666'", r"\u2665'", r"\u2660'"]

print(heart)
print(spade)
print(diamond)
print(club)

f = open("card_dict.txt", "w+")
i = 0
while (i < 13):
    for j in range(2, 15):

        for suit in suits:
            i += 1
            f.write("{} : {} {},\n".format(i, "'" + str(j), suit))
f.close()
