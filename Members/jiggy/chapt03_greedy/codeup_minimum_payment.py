first_pasta = int(input())
second_pasta = int(input())
third_pasta = int(input())
first_juice = int(input())
second_juice = int(input())

past_list = [first_pasta, second_pasta, third_pasta]
juice_list = [first_juice, second_juice]

min_past = min(past_list)
min_juice = min(juice_list)

pay = min_past + min_juice

min_pay = pay + (pay * 1/10)

print(round(min_pay, 1))
