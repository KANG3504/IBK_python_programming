def fahrenheit(a):
    return "{}의 화씨는 {:.2f} 입니다".format(a, ((9/5)*a)+32)

print(fahrenheit(float(input("섭씨를 입력하세요 : "))))

print("섭씹 : ")
user_input = input()

print(f"섭씨온도 : {user_input}")
