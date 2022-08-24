from sys import stdin

# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5, 3, 2, 7, 5]
survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]


def solution(survey, choices):
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    answer = ''

    for i in range(len(survey)):
        left = survey[i][0]
        right = survey[i][1]

        if choices[i] > 4:
            dic[right] += choices[i] - 4
        elif choices[i] < 4:
            dic[left] += 4 - choices[i]

    if dic["R"] >= dic["T"]:
        answer += "R"
    else:
        answer += "T"

    if dic["C"] >= dic["F"]:
        answer += "C"
    else:
        answer += "F"

    if dic["J"] >= dic["M"]:
        answer += "J"
    else:
        answer += "M"

    if dic["A"] >= dic["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer


print(solution(survey, choices))