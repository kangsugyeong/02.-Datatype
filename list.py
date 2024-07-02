sugyeong = ["강수경", '25', '1117']
print(type(sugyeong))
name = sugyeong[0]
age = sugyeong[1]
birth = sugyeong[2]
print(name, age, birth)

names = [['강수경', '강혜나', '김민석'],['20','21','22']]
print(names[0][0:2])

sugyeong = ["현대건설", "안전관리"]
print(sugyeong)

numbers = [1,2,3,4,5]
result = numbers[2] + numbers[-1]
print(result)

print(len(names[0]))

# 리스트에 요소 추가하기
last = [1,2,3]
last.append(30)
print(last)
last.remove(3)
print(last)