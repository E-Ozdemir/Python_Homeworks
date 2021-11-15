
ops =  ["5", "-2", "4", "C", "D", "9", "+", "+"]
result = []
for i in ops:
    if i == "D":
        result.append(2 * int(result[-1]))
    elif i == "C":
        result.pop()
    elif i == "+":
        result.append(int(result[-1]) + int(result[-2]))
    else:
        result.append(int(i))
print(sum(result))