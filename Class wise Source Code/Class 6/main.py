# Adding Whitespace to Strings with Tabs or Newlines


# print("""data\nclass_06\n\tHello world\tPakistan""")


result = "python    "
result1 = "     Hello world"
print((f"{result.rstrip()} {result1.lstrip()}"))
# abc = result, result1
# print(abc.rstrip())



abc = "   python  "
print(abc.strip())