# take input
input_from_user = input("Input : ")
# make a list of vowels
vowels = ['a','e','i','o','u','A','E','I','O','U']
#check  and store words without vowels
filtered_intput = [char for char in input_from_user if char not in vowels]
# join the word without vowels
output = "".join(filtered_intput)
# show the output
print("Output :", output)