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

directions = parse("day2-input.txt")
p0 = Point()
for dir, amt in directions:
    p0 = p0.move(dir, int(amt))
assert(p0.x * p0.y == 1989265)

directions2 = parse("day2-input-twitter.txt")
p0 = Point()
for dir, amt in directions2:
    p0 = p0.move(dir, int(amt))
assert(p0.x * p0.y == 1250395)

## Part 2 ##

# aim, horiztonal, depth
# down increases aim
# up decreases aim
# forward increases horizontal, increases depth by aim * X

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2

# output: horizontal 15, depth 60, mult = 900

class Point2:
    def __init__(self, x=0, y=0, aim=0):
        self.x = x
        self.y = y
        self.aim = aim
    
    def move(self, dir, amt):
        new_x, new_y = self.x, self.y
        if dir == "forward":
            new_x += amt
            new_y += self.aim * amt
        elif dir == "down":
            self.aim += amt
        elif dir == "up":
            self.aim -= amt
        return Point2(new_x, new_y, self.aim)

aim_point = Point2()
for dir, amt in directions:
    aim_point = aim_point.move(dir, int(amt))
assert(aim_point.x * aim_point.y == 2089174012)

aim_point = Point2()
for dir, amt in directions2:
    aim_point = aim_point.move(dir, int(amt))
assert(aim_point.x * aim_point.y == 1451210346)