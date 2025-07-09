items = ["apple","banana","orange" ,"mango"]
unique_item = set()
for c in items:
    if c in unique_item:
        print("Duplicate item:",c)
        break
    unique_item.add(c)


