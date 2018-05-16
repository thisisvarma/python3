print("--------------- print different vowels from given string -----------")
word=input("Enter some word or string : ")
vowels={'a','e','i','o','u'}
difference=vowels.intersection(word)
print("vowels from given word are : ", difference)
print("number of vowels from given word : ",len(difference))
