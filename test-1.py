
m = open("file.txt", "r", encoding="utf-8").read()

from pprint import pprint

def nth_level_markov(inp, gn):
    d = {}
    inp = list(map(lambda x: str(x), inp))
    for word in range(0, len(inp)):
        try:
            g = " ".join(inp[word:word+gn])
            
            if g in d.keys():
                d[g] += [inp[word+gn]]
            else:
                d[g] = [inp[word+gn]]
        except:
            # TODO: don't pass, figure out 
            pass
    def gen(n):
        import random
        end = []
        last = random.choice(list(d.keys()))
        while len(end) < n:
            if last in d.keys():
                tmp = random.choice(d[last])
                end.append(tmp)
                next = " ".join(last.split(" ")[1:]) + " " + tmp
                last = next
            else:
                print("Done")
                break
        return " ".join(end)
    return gen


def makeproper(s):
    import re
    return re.findall(r"[\w']+|[.,!?;]", s)

gen = nth_level_markov(
    makeproper(m),
    4
)
print(gen(10000))

# one two three four
# one two: three
# two three: four