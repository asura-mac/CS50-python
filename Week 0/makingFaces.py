def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")

def main():
    s = input()
    print(convert(s))

main()