rows = 5  

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end=' ')

    # Print numbers
    for j in range(1, i*2):
        print(j, end=' ')

    print()

for i in range(rows - 1, 0, -1):
# Print leading spaces
  for j in range(rows - i):
    print(" ", end=' ')

# Print numbers
  for k in range(1, i * 2):
    print(k, end=' ')

  print()