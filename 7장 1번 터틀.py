import turtle              # 터틀 불러오기 
t = turtle.Turtle()        # t에 터틀 변수 설정
t.shape("turtle")          # 터틀 모양 지정 
t.color("black", "white")  # 터틀의 색상 지정 검정색과 하얀색

s = turtle.Screen(); s.bgcolor('skyblue');   # 터틀의 배경색 지정 하늘색

def draw_snowman(x, y):                     # 함수 생성 눈사람만들기
    t.up()                 
    t.goto(x, y) 
    t.down()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.goto(x, y-25)
    t.setheading(135)
    t.forward(50)
    t.backward(50)

    t.setheading(30)
    t.forward(50)
    t.backward(50)
    t.setheading(0)

    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.goto(x, y-70)
    t.begin_fill()
    t.circle(30)
    t.end_fill()

draw_snowman(0, 0)        # 1번 눈사람의 위치 설정
draw_snowman(100, 0)      # 2번 눈사람의 위치 설정
draw_snowman(200, 0)      # 3번 눈사람의 위치 설정
