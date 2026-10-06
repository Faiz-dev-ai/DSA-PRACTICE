def NonRepeatingCharacter(string):
    #Store it in hashmap
    dictionary={}
    for i in string:
        dictionary[i]  = dictionary.get(i,0)+1
    print(dictionary)
    #Give me first letter i got in the string that is non repeating 
    for ch in string:
        if dictionary[ch] == 1:
            return ch
string = input("Enter the String:")
print(NonRepeatingCharacter(string))
