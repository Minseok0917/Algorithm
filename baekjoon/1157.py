area = {}
s = input().upper()
for i in s:
    area[i] = area[i]+1 if i in area else 1

key = s[0]
max = max(area.values())
for i in area:
    if area[key] < area[i] or key == i:
        key = i
    elif area[key] == area[i] and area[key] == max:
        key = '?'
        break

print(key)
