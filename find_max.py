
with open('data/numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]
    nejvetsicislo = max(numbers)

print(f"Největší číslo : {nejvetsicislo}")