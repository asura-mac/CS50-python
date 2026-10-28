input_from_user = input("Input : ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
filtered_intput = [char for char in input_from_user if char not in vowels]
output = "".join(filtered_intput)
print("Output :", output)