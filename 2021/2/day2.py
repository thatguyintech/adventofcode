# commands: forward 1, down 2, up 3
# forward X increases horizontal by X
# down X increases depth by X
# up X decreases depth by X

# example:
# (start at 0, 0)
# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2

# (end at 15, 10) -> product is 150

def parse(filename):
    directions = []
    with open(filename) as f:
        for line in f:
            directions.append(line.split())
    return directions 

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move(self, dir, amt):
        new_x, new_y = self.x, self.y
        if dir == "forward":
            new_x += amt
        elif dir == "down":
            new_y += amt
        elif dir == "up":
            new_y -= amt
        return Point(new_x, new_y)

p0 = Point(0,0)
p1 = p0.move("forward", 2)
assert(p1.x == 2 and p1.y == 0)
p2 = p1.move("down", 2)
assert(p2.x == 2 and p2.y == 2)
p3 = p2.move("up", 2)
assert(p3.x == 2 and p3.y == 0)

directions = parse("day2-input.txt")
for dir, amt in directions:
    p0 = p0.move(dir, int(amt))
print(p0.x, p0.y)
assert(p0.x == 2083 and p0.y == 955)
print(p0.x * p0.y)
