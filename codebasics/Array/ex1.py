

heros: list[str] = ['spider man','thor','hulk','iron man','captain america']


# Length of the list
print(F"Length of list is: {len(heros)}")

# Add 'black panther' at the end of this list
heros.append("black panther")
print(f"Added another hero: {heros}")

# You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(3, "black panther")
print(f"Added the new hero after Hulk: {heros}")

# Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.

heros[1:3] = ["doctor strange"]
print(F"Replaced Thor & Hulk: {heros}")

# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(F"Sorted heros list: {heros}")