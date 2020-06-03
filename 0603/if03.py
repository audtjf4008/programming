# file name : if03.py
# if(조건문)에서 조건문이 True이면 if 아레에 있는 명령들이 실행
# 그렇지 않고 elif 조건문이 True이면 elif 아래에 있는 명령들이 실행
# 그렇지 않고 elif 조건문이 True이면 elif 아래에 있는 명령들이 실행
# ...
#그렇지 않으면(위에 조건들이 True가 아니면) else 아래에 있는 명령들이 실행

a = int(input("점수 입력 : "))

if a >= 90:
   print("당신의 학점은 A 입니다.")
elif a >= 80:
   print("당신의 학점은 B 입니다.")
elif a >= 70:
   print("당신의 학점은 C 입니다.")
elif a >= 60:   
   print("당신의 학점은 D 입니다.")
else:
   print("당신의 학점은 F 입니다.")
   
print("수고하셨습니다.")
