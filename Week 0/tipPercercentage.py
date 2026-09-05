def main():
    dollars = float(input("Dollars bill: "))
    percent = int(input("Percentage: "))
    tip = dollars * (percent / 100)
    print(f"{tip:.2f}")

main()