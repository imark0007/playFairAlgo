# Remove spaces and make all characters uppercase for simplicity
P = input("Enter plaintext (P): ").replace(" ", "").upper()
K = input("Enter key (K): ").replace(" ", "").upper()
C = input("Do you want to Encrypt or Decrypt (E/D)? ").upper()

# Prepare 5x5 matrix
matrix = []
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is typically combined with I in Playfair cipher

# Remove duplicates from the key and build the matrix
used = []
for char in K:
    if char not in used and char in alphabet:
        used.append(char)

# Add remaining letters of the alphabet to the matrix
for char in alphabet:
    if char not in used:
        used.append(char)

# Fill the matrix row by row
for i in range(0, 25, 5):
    matrix.append(used[i:i + 5])

# Print the matrix (for reference)
for row in matrix:
    print(" ".join(row))

# Prepare the plaintext (or ciphertext) for processing by breaking it into digraphs
if C == "E":  # Encrypt
    # If two letters in the digraph are the same, insert an 'X' between them
    plaintext = ""
    i = 0
    while i < len(P):
        if i + 1 < len(P) and P[i] == P[i + 1]:
            plaintext += P[i] + "X"
            i += 1
        else:
            plaintext += P[i]
            i += 1
    if len(plaintext) % 2 != 0:  # If there's an odd number of characters, append an 'X'
        plaintext += "X"

    # Now encrypt the digraphs
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        # Find the position of each letter in the matrix
        for row in range(5):
            if a in matrix[row]:
                a_row, a_col = row, matrix[row].index(a)
            if b in matrix[row]:
                b_row, b_col = row, matrix[row].index(b)

        # Encrypt according to Playfair rules
        if a_row == b_row:
            ciphertext += matrix[a_row][(a_col + 1) % 5] + matrix[b_row][(b_col + 1) % 5]
        elif a_col == b_col:
            ciphertext += matrix[(a_row + 1) % 5][a_col] + matrix[(b_row + 1) % 5][b_col]
        else:
            ciphertext += matrix[a_row][b_col] + matrix[b_row][a_col]

    print("Ciphertext:", ciphertext)

elif C == "D":  # Decrypt
    plaintext = ""
    for i in range(0, len(P), 2):
        a, b = P[i], P[i + 1]
        # Find the position of each letter in the matrix
        for row in range(5):
            if a in matrix[row]:
                a_row, a_col = row, matrix[row].index(a)
            if b in matrix[row]:
                b_row, b_col = row, matrix[row].index(b)

        # Decrypt according to Playfair rules
        if a_row == b_row:
            plaintext += matrix[a_row][(a_col - 1) % 5] + matrix[b_row][(b_col - 1) % 5]
        elif a_col == b_col:
            plaintext += matrix[(a_row - 1) % 5][a_col] + matrix[(b_row - 1) % 5][b_col]
        else:
            plaintext += matrix[a_row][b_col] + matrix[b_row][a_col]

    print("Plaintext:", plaintext)