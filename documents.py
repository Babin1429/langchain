with open("data.txt", "rb") as f:
    raw = f.read()
print(repr(raw))

with open("data.txt", "r", encoding='utf-8') as f:
    content = f.read()
print(repr(content))

with open("data.txt", "r", encoding='utf-8-sig') as f:
    content_sig = f.read()
print(repr(content_sig))