import sys
import pyperclip

keyword1 = input("Enter first Major Keyword: ")
keyword2 = input("Enter second Major Keyword: ")
if keyword1 == "" or keyword2 == "":
    messagebox.showinfo("Error", "Please enter two Major keywords")
    sys.exit()
keyword1_1 = ('"' + keyword1 + '"')
keyword2_2 = ('"' + keyword2 + '"')
major_string = (keyword1_1 + ' OR ' + keyword2_2)
with open('keywords.txt') as f:
    keywords = f.read().splitlines()
    keywords = ['"' + keyword + '"' for keyword in keywords]
    keywords = ' AND '.join(keywords)
search_term = (major_string + ' AND ' + keywords)
print("")
print(search_term)
print("")
print("New Query Added To Clipboard")
pyperclip.copy(search_term)
