with open("list_gift.txt", "r", encoding="utf-8") as f:
    data = [line.strip() for line in f if line.strip()]

print(data)

list_ = []
l = 0

for i in data:
    l += 1
    list_.append(
        {"id": l, "text": i, "color": "#92E3A9", "use": False, "special": False}
    )
print(list_)
