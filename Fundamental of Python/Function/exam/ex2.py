def avarageOfList(li):
    result = 0
    for i in li:
        result += i

    li_length = len(li)
    avarage = result / li_length

    return avarage

answer = avarageOfList([1,2,3,4])
print(answer)
