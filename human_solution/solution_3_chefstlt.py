t = eval(input())
i = 0

while i != t:
    str1 = ""
    str2 = ""
    str1 = input()
    str2 = input()
    len_string = len(str1)
    j = 0
    min = 0
    max = 0

    while j < len_string:
        if str1[j] != str2[j] or str1[j] == '?' or str2[j] == '?':
            if str1[j] == '?' or str2[j] == '?':
                max += 1
            else:
                min += 1
                max += 1
        j += 1
    print(min," ",max)
    i += 1