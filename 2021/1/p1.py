from pprint import pprint

f = open("../../problems/1/input.txt", "r")
data = f.read()
data = data.split("\n")
data = list(map(lambda x: int(x) if x != "" else 0, data))

def p1():
    last = 0
    inc = 0
    dec = 0
    for i,d in enumerate(data):
        if i==0:
            last = d
            continue

        print([d, last])
        if d > last:
            inc += 1
        else:
            dec += 1
        last = d
    print(data[1:10])
    print([inc, dec])

# p1()
def p2():
    last = 0
    inc = 0 
    dec = 0
    xs = []
    for i,d in enumerate(data):
        if i==0:
            last = data[i] + data[i+1] + data[i+2]
            xs.append([last, last])
            continue
        
        if i >= len(data)-1:
            cur = data[i-2] + data[i-1] + data[i]
            last = cur
            break

        cur = data[i-1] + data[i] + data[i+1]
        x = 0
        if cur > last:
            inc += 1
        else:
            dec += 1
        xs.append([last, cur])
        last = cur

#        if(i == 30):
#            break
#    pprint(xs)
    print([inc, dec])

p2()
