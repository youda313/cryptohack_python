# Given the string "label", XOR each character with the integer 13. 
# Convert these integers back to a string and submit the flag as crypto{new_string}.

first_s = "label"
second_s = 13
int_list = []

unicode_first_s = [ord(b) for b in first_s]

for i in unicode_first_s:
    int_list.append(i ^ second_s)

for j in int_list:
    print(chr(j))