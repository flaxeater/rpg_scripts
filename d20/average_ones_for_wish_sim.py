from random import choice

d20=lambda:choice(range(1,21))

runs = 30000

def test(runs, mythic_points = 9):
    stats=[]
    for x in range(runs):
        tests = 0
        ones = 0
        while ones < mythic_points:
            tests += 1
            if d20() == 1:
                ones += 1
        stats.append(tests);
    result = float(sum(stats))/len(stats)
    print result
    return result

#test(runs)

tests = []

for x in range(4):
    tests.append(test(runs))
print tests
