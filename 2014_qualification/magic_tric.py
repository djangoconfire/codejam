import fileinput

f = fileinput.input()

T = int(f.readline())
for case in range(1, T + 1):
    first = list()
    first_answer = int(f.readline())
    for i in range(4):
        first.append([int(x) for x in f.readline().split()])

    first_relevant = first[first_answer - 1]
    second = list()
    second_answer = int(f.readline())
    for i in range(4):
        second.append([int(x) for x in f.readline().split()])
    second_relevant = second[second_answer - 1]
    #
    possibles = [x for x in first_relevant if x in second_relevant]
    if len(possibles) > 1:
        answer = "Bad magician!"
    elif len(possibles) == 1:
        answer = possibles[0]
    else:
        answer = "Volunteer cheated!"

    print("Case #{0}: {1}".format(case, answer))