# signal strength 0-50 stars
# get all fifty stars

# input: measurement of sea floor depth, outwards from submarine

# 199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263

# output: number of times depth increases

# 7 increases

def parse(filename):
    depths = []
    with open(filename) as f:
        for line in f:
            depths.append(int(line))
    return depths

def count_increases(depth_arr):
    if len(depth_arr) == 0 or len(depth_arr) == 1:
        return 0

    increases = 0
    prev_depth = depth_arr[0]
    for depth in depth_arr[1:]:
        if depth > prev_depth:
            increases += 1
        prev_depth = depth

    return increases

###########
## TESTS ##
###########
assert(count_increases(parse('example1.txt')) == 7)
assert(count_increases(parse('example2.txt')) == 0)
assert(count_increases(parse('example3.txt')) == 3)
assert(count_increases(parse('example4.txt')) == 0)

##################
## FINAL ANSWER ##
##################
assert(count_increases(parse('day1-input.txt')) == 1387)