import re

# Open the input file
with open(r"C:\Users\Family\Desktop\paragrafizace\genesis.txt", "r", encoding='utf-8') as f:
    text = f.read()

# Define the string to be added
addedtext = "</p> <p>"

# Iterate over matches of superscript digits and insert the added text
modified_text = text
num = 0
for m in re.finditer(r"[¹²³⁴⁵⁶⁷⁸⁹]+", text):
    modified_text = modified_text[:m.start() + num] + addedtext + modified_text[m.start() + num:m.end() + num] + modified_text[m.end() + num:]
    num += len(addedtext)

# Write the modified text to the output file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(modified_text)