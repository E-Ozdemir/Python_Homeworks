from collections import Counter
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
cnt = Counter(numbers)
a = list(cnt.most_common())
print('the most frequent number is',a[0][0], 'and it was' ,a[0][1], 'times repeated')