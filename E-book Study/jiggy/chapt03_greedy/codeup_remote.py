a, b = map(int, input().split())

dif = abs(a - b)
button_clicked = 0

if dif % 10 > 7:
    button_clicked += (dif // 10) + 1
    dif -= 10 * ((dif // 10) + 1)
    if abs(dif) % 5 >= 3:
        dif = abs(dif) - 5
        button_clicked += 1 + abs(dif)
    else:
        button_clicked += abs(dif)
else:
    button_clicked += dif // 10
    dif -= 10 * (dif // 10)
    if dif >= 3:
        dif = abs(dif) - 5
        button_clicked += 1 + abs(dif)
    else:
        button_clicked += abs(dif)

print(button_clicked)
