#Counting Vowels and Consonants in a String
# vowels are a,e,i,o,u
# eg 
# input:hello world

# output: 
# vowels 3 (e,o,o)
#non-vowels: 7 (h,l,l,w,r,l,d)

s = str(input("enter a string: ").lower().replace(" ",""))
no_of_vowels = 0
no_of_non_vowels = 0
list_vowels= []
list_non_vowels = []
for i in s:
    if (i=='a') or (i=='e') or (i=='i') or (i=='o') or (i=='u'):
        list_vowels.append(i) #for the end output (['e','o','o'])
        no_of_vowels+=1 
    else:
        list_non_vowels.append(i)
        no_of_non_vowels+=1


print(f"vowels: {no_of_vowels} ({list_vowels})")
print(f"non-vowels: {no_of_non_vowels} ({list_non_vowels})")


#list comprehensions 
# string = str(input("enter a string: "))
# string.lower().replace(" ","")
# vowels = "aeiou"

# vowels = sum(string.count(vowel) for vowel in vowels)
# print(f"vowels: {vowels}")