# find max len of str in a list

# 1 way
data = ['amar', 'vicky', 'amardip']
print (reduce(lambda x, y : x if len(x) > len(y) else y, data))

#2 way
print (max(data, key=len))