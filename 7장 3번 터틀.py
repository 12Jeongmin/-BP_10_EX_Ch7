import turtle           # 터틀 불러오기 
t = turtle.Turtle()     # t에 터틀 변수 설정 
t.shape("turtle")       # 터틀의 거북이 모양 불러오기
t.speed(0)              # 터틀의 속도 설정 

def f(x):               # 함수 f(x)=X2+1을 계산 하는함수 작성 
    return x**2+1


t.goto(200, 0)
t.goto(0, 0)
t.goto(0, 200)
t.goto(0, 0)

for x in range(150):
    t.goto(x, int(0.01*f(x)))
