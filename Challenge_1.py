s = str(input("Please enter your string: "))

lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
odddigits = ['1','3','5','7','9']
evendigits = ['0','2','4','6','8']

lower = ""
upper = ""
odd = ""
even = ""

for i in range(len(s)):
    if s[i] in lowercase:
        lower = lower + str(s[i]) + " "
    elif s[i] in uppercase:
        upper = upper + str(s[i]) + " "
    elif s[i] in odddigits:
        odd = odd + str(s[i]) + " "
    elif s[i] in evendigits:
        even = even + str(s[i]) + " "

    

lower = lower.split()
for i in range(len(lower)):
    for j in range(len(lower)-1):
        if lowercase.index(lower[j]) > lowercase.index(lower[j+1]):
            temp = lower[j]
            lower[j] = lower[j + 1]
            lower[j + 1] = temp

sortedlower = ""
for i in range(len(lower)):
    sortedlower = sortedlower + lower[i]



upper = upper.split()
for i in range(len(upper)):
    for j in range(len(upper)-1):
        if uppercase.index(upper[j]) > uppercase.index(upper[j+1]):
            temp = upper[j]
            upper[j] = upper[j + 1]
            upper[j + 1] = temp

sortedupper = ""
for i in range(len(upper)):
    sortedupper = sortedupper + upper[i]



odd = odd.split()
for i in range(len(odd)):
    for j in range(len(odd)-1):
        if odddigits.index(odd[j]) > odddigits.index(odd[j+1]):
            temp = odd[j]
            odd[j] = odd[j + 1]
            odd[j + 1] = temp

sortedodd = ""
for i in range(len(odd)):
    sortedodd = sortedodd + odd[i]

even = even.split()
for i in range(len(even)):
    for j in range(len(even)-1):
        if evendigits.index(even[j]) > evendigits.index(even[j+1]):
            temp = even[j]
            even[j] = even[j + 1]
            even[j + 1] = temp

sortedeven = ""
for i in range(len(even)):
    sortedeven = sortedeven + even[i]

print(sortedlower + sortedupper + sortedodd + sortedeven)
