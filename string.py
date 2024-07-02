a = "hello world"
print(a)
# ''도 가능하다. '' 안에 들어가는 것은 숫자여도 문자형태
name = "강수경"
age = '25'
print("-"*40)
c = name + '님 반갑습니다. ' + '나이는 ' + age + '살 이시군요. '
print(c)
print("-"*40)

print(len(c)) #len은 글자수세기, 화면에 출력하려면 print도 같이 써야 함.

# 파이썬 문자열의 인덱싱 및 슬라이싱
str = "smart안전학과 강사 7월 강의 현황"
print(str[0:5])
smart = str[0:5]
print(smart)
print(str[-1])