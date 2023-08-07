import re

# task 1

# try:
#
#     with open("input_text.txt", "r") as input_text:
#         content_text = input_text.read()
#
#     text_filter = re.findall(r'\b[a-zA-Z]{7,}\b', content_text)
#
#     with open("output_text.txt", "w") as output_text:
#         output_text.write(' '.join(text_filter))
#
#     print("Successfully created a new file 'output_text.txt' with matching words")
#
# except IOError:
#     print("Unable to read or write files!")

# task 2

# try:
#
#     with open("input_text.txt", "r") as input_text:
#         content_text = input_text.read()
#         amount_text = len(re.findall(r'\b[a-zA-Z]+\b', content_text))
#
#         print(f"Number of words {amount_text}")
#
# except IOError:
#     print(f"Unable to read file!")


