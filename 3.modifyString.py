print("\n")

#Upper Case

txt = "hello world"

print(f"Upper case: {txt.upper()}")

print("\n")

#Lower Case

txt = "hElLo WOrLd"

print(f"Lower case: {txt.lower()}")

print("\n")

#Remove Whitespace from the beginning or the end

txt = "  Harvard, Roosevelt  "

print(f"Remove Whitespace: {txt.strip()}")

print("\n")

#Replace String

txt = "Josh Hard"

print(txt)
print(f"Replace word J->H : {txt.replace('J', 'H')}")

print("\n")

#Split String, returns a list where the text between the specified separator becomes the list items

txt = "Banana, Apple, Orange, Mango"

print(f"List items: {txt.split(",")} ")