import turtle              # 터틀 불러오기
t = turtle.Turtle()        # t에 터틀 설정 
t.shape("turtle")          # 터틀 모양 거북이로 설정  
t.speed(0)                 # 터틀의 속도 설정

def hexagon():             # 육각형을 만든는 함수 생성
    for i in range(6):
        turtle.forward(100)
        turtle.left(360/6)

for i in range (6):        # 육각형을 만드는 함수 반복생성
    hexagon()
    turtle.forward(100)
    turtle.right(60)
