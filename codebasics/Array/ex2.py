
# Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

max_number: int = int(input("[+] Enter a number: "))

odd_numbers: list[int] = [num for num in filter(lambda x: x % 2 > 0, list(range(max_number + 1)))]

print(f"Odd numbers between 1 & {max_number} are: {odd_numbers}")