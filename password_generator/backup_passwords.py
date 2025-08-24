"""A simple script to back up the generated_passwords.txt file."""

with open('generated_passwords.txt', 'r') as file:
    original = file.read()
    print('File opened.')

with open('generated_passwords.txt.bak', 'w') as file:
    file.write(original)
    print('file saved.')
