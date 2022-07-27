from pprint import pprint
from collections import Counter

data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

f = open("../../problems/2021/3/input.txt", "r")
data = f.read()
data = data.split("\n")
# data = list(map(lambda x: int(x) if x != "" else 0, data))

temp = []
digits = [
    [] for x in "100111011000"
]
cnts = []

def decompose(data, init="100111011000"):
    digits = [
        [] for x in init
    ]

    cnts = []

    for i,d in enumerate(data):
        for j, de in enumerate(d):
            digits[j].append(de)
    # act(data)
    # cnts = []
    for d in digits:
        cnts.append(dict(Counter(d)))
    return digits, cnts

def p1():
    for i,d in enumerate(data):
        for j, de in enumerate(d):
            digits[j].append(de)
    # act(data)
    # cnts = []
    for d in digits:
        cnts.append(dict(Counter(d)))
    # print(cnts)

def p1x():
    # cnts = [{'0': 506, '1': 494},
    #     {'0': 510, '1': 490},
    #     {'0': 494, '1': 506},
    #     {'0': 492, '1': 508},
    #     {'0': 501, '1': 499},
    #     {'0': 502, '1': 498},
    #     {'0': 506, '1': 494},
    #     {'0': 489, '1': 511},
    #     {'0': 505, '1': 495},
    #     {'0': 524, '1': 476},
    #     {'0': 515, '1': 485},
    #     {'0': 510, '1': 490}
    # ]

    msb = ''
    for c in cnts:
        if c['0'] > c['1']:
            msb += '0'
        else:
            msb += '1'

    print(msb)
    pprint(cnts)

def getOxy():
    temp = data
    print(temp)
    for i, d in enumerate(temp[0]):
        digits, cnts = decompose(temp, init=temp[0])
        c = cnts[i]
        di = digits[i]
        # print(digits)
        # print(digits[i])
        if c['0'] > c['1']:
            temp = [data for i,data in enumerate(temp) for j,de in enumerate(di) if i==j and de=='0']
        elif c['0'] < c['1']:
            temp = [data for i,data in enumerate(temp) for j,de in enumerate(di) if i==j and de=='1']
        else:
            temp = [data for i,data in enumerate(temp) for j,de in enumerate(di) if i==j and de=='1']
        print(c['0'], c['1'], temp)
        
        if len(temp) == 1:
             break
    return temp

def getCo2():
    temp = data
    print(temp)
    
    for i, d in enumerate(temp[0]):
        digits, cnts = decompose(temp, init=temp[0])
        c = cnts[i]
        di = digits[i]
        # print(digits)
        # print(digits[i])
        if c['0'] < c['1']:
            temp = [data for i,data in enumerate(temp) for j,de in enumerate(di) if i==j and de=='0']
        elif c['0'] > c['1']:
            temp = [data for i,data in enumerate(temp) for j,de in enumerate(di) if i==j and de=='1']
        else:
            temp = [data for i,data in enumerate(temp) for j,de in enumerate(di) if i==j and de=='0']
        print(c['0'], c['1'], temp)

        if len(temp) == 1:
             break
    return temp

# print(data)
# p1()
# p1x()
# print(digits)
print(cnts)
oxy = getOxy()
co2 = getCo2()

print([
    oxy[0],
    co2[0]
])

print(eval("0b"+oxy[0]) * eval("0b"+co2[0]))