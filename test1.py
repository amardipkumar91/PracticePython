import re
string = 'h8i rajes34singh h4ow a23re yo76u abc67x'
split_string = string.split()
all_int = []
for i in split_string:
    num = int(re.search(r'\d+', i).group())
    all_int.append(num)
all_int.sort()

final_list = []
for nn in all_int:
    # dd = [s for s in split_string if str(nn) in s and len(re.search(r'\d+', i).group()) == len(str(nn))]
    for st in split_string:
        if str(nn) in st and len(re.search(r'\d+', st).group()) == len(str(nn)):
            final_list.append("".join(sorted(st)))
result = " ".join(final_list)
print "final result is :",result