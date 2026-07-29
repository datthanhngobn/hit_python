itemBought = list(input("Ten san pham da mua: ").replace(",", " ").split())

searchItem = input("Ten san pham kiem tra: ")
maxItem = []
countItem = 0


for i in range(len(itemBought)) :
    itemBought[i] = itemBought[i][:1].upper() + itemBought[i][1:].lower()
    if (itemBought[i] == "Sữa") :
        saveIndex = i

st = set(itemBought)

for i in st :
    if (countItem < itemBought.count(i)) :
        maxItem.clear()
        maxItem .append(i)
        countItem = itemBought.count(i)
    elif (countItem == itemBought.count(i)) :
        maxItem .append(i)

sorted(maxItem)

print(f"Tong so san pham da mua la {len(itemBought)}: {st}")

if (len(itemBought) % 2 == 1) :
    print(itemBought[int(len(itemBought) / 2) + 1])

print(f"San pham xuat hien nhieu nhat: {maxItem} xuat hien {countItem}", sep=' ')

if (itemBought.count(searchItem) > 0) :
    print(f"San pham {searchItem} xuat hien {itemBought.count(searchItem)}")
else :
    print(f"San pham {searchItem} khong xuat hien")

itemBought.insert(0, "Banh Nabati")

if (itemBought.count("Sữa") > 0) :
    itemBought.pop(saveIndex + 1)

print(itemBought)