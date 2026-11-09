def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # checking for input more than 2 letters upto 6
    if len(s) < 2 or len(s) > 6:
        return False
    #  checking for input to not have letters in last two places
    for char in s [:2]:
        if not char.isalpha():
            return False
    # it has not digits yet
    has_digit = False
    for char in s:
        if char.isdigit():
            # if it's digit it shouldn't started with 0
            if not has_digit and char == "0":
                return False
            has_digit = True
        #if it had a digit yet and it's not a digit then invalid  
        elif has_digit and not char.isdigit():
            return False

    for char in s:
        is_puntuation = not char.isalnum() and not char.isspace()
        #checking for puncuation, space or period
        if char.isspace() or char == "." or is_puntuation:
            return False
# if it pass everything then it's valid
    return True
main() 