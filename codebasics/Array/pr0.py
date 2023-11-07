
jan: int = 0
feb: int = 1
mar: int = 2
apr: int = 3
may: int = 4

monthly_expenses: list[int] = [2200, 2350, 2600, 2130, 2190]

# In Feb, how many nairas you spent extra compare to January?
feb_extra_expense: int = monthly_expenses[feb] - monthly_expenses[jan]
print(F"[+] In february i spent NGN{feb_extra_expense:.2f} more than January last month")

# Find out your total expense in first quarter (first three months) of the year.
first_quarter_expense: float = sum(monthly_expenses[:3])
print(F"[+] 1st quarter total expense: NGN{first_quarter_expense:.2f}")

# Find out if you spent exactly 2000 nairas in any month
spent_2000: bool = 2000 in monthly_expenses

# for _ in monthly_expenses:
#     if _ == 2000:
#         spent_2000 = True

print(f"[+] Did i spend exectly NGN2000 in any month? {spent_2000}")

# June month just finished and your expense is 1980 naira. Add this item to our monthly expense list
monthly_expenses.append(1980)
print(F"[+] Updated monthly expenses: {monthly_expenses}")

# You returned an item that you bought in a month of April and
# got a refund of NGN200. Make a correction to your monthly expense list
# based on this
monthly_expenses[apr] = monthly_expenses[apr] - 200
print(F"[+] Updated monthly expenses: {monthly_expenses}")
