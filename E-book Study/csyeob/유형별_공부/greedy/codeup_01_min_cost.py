# 3종류의 파스타와 2종류의 생과일 주스에서 하나씩 선택
# 파스타와 생과일 쥬스의 가격의 합계에서 10퍼센트를 더한 금액이 대금

#첫번째 틀렸을때 걍 바보임
pasta = []
drink = []

for i in range(3):
    a = input()
    pasta.append(a)
for i in range(2):
    b = input()
    drink.append(b)

pasta.sort()
drink.sort()
minimum = float(pasta[0])*1.1 + float(drink[0])*1.1
print(round(minimum,1))

# 2번째로 리스트 컴프렉션과 간단하게 생각해봄 맞음 얏호
pasta = [float(input()) for _ in range(3)]
drink = [float(input()) for _ in range(2)]

print(round((min(pasta) + min(drink)) * 1.1, 1))
