f = open("../../problems/1/input.txt", "r")
data = f.read()
data = data.split("\n")
data = list(map(lambda x: int(x) if x != "" else 0, data))

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
