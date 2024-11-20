
# debug.py

import pdb

# counter = 1
# pdb.set_trace()

# while counter <= 5:
#     print(counter)
#     pdb.set_trace()  # Add breakpoint
#     counter += 1

cats = []

for name in ('Powder', 'Sky', 'Cheddar', 'Cocao'):
    pdb.set_trace()
    cats + [name]

print(cats)
