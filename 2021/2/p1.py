from pprint import pprint

f = open("../../problems/2021/2/input.txt", "r")
data = f.read()
data = data.split("\n")
# data = list(map(lambda x: int(x) if x != "" else 0, data))

class Subm():
    x = 0
    y = 0
    aimx = 0
    
    aim = 0
    log = []

    def __init__(self):
        pass
    
    def fwd(self, x=1):
        self.x += x
        self.log.append(("fwd",x))

        return self
    
    def down(self, x=1):
        self.y -= x
        self.log.append(("down",x))

        return self

    def up(self, x=1):
        self.y += x
        self.log.append(("up",x))

        return self
    
    def aimfwd(self, x=1):
        aim = self.aimx if self.aimx > 0 else 1

        self.x += x
        self.y += aim * x

        self.log.append(("aimfwd",x))

        return self
    
    def aimdown(self, x=1):
        self.aimx += x
        self.log.append(("aimdown",x))

        return self

    def aimup(self, x=1):
        self.aimx -= x
        self.log.append(("aimup",x))

        return self
    
    def mulxy(self):
        return self.x * self.y

    def pos(self):
        return self.x, self.y

subm = Subm()

def parseCmd(str):
    cmds = str.split(" ")

    if(len(cmds) < 2):
        cmds = ["x", 0]

    return {
        "cmd": cmds[0],
        "arg": int(cmds[1]),
    }

def act(cmds):
    for st in cmds:
        parsed = parseCmd(st)
        print(parsed)
        cmd = parsed['cmd']
        v = parsed['arg']

        if cmd == "forward":
            subm.fwd(v)
        elif cmd == "up":
            subm.up(v)
        elif cmd == "down":
            subm.down(v)
        print(subm.pos())

def act2(cmds):
    for st in cmds:
        parsed = parseCmd(st)
        print(parsed)
        cmd = parsed['cmd']
        v = parsed['arg']

        if cmd == "forward":
            subm.aimfwd(v)
        elif cmd == "up":
            subm.aimup(v)
        elif cmd == "down":
            subm.aimdown(v)
        print(subm.pos())
    
def p1():
    # act(data)
    act2(data)
    print(subm)
    print(subm.__dict__)
    print(subm.pos())
    print(subm.mulxy())

# print(data)
p1()
