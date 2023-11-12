# table_printer/printer.py

def print_table(number, limit=10):
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} * {i} = {result}")

def main():
    number = int(input("Enter a number between 1 and 100: "))
    print_table(number)
