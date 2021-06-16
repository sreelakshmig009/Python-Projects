string1 = input()
string2 = input()
if(sorted(string1) == sorted(string2)):
    print("yes it is an anagram")
else:
    print("no it is not an anagram")