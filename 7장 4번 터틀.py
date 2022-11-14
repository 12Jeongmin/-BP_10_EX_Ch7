import turtle             # 터틀 불러오기
t = turtle.Turtle()       # t에 터틀 변수 설정
t.shape("turtle")         # 터틀모양 거북이로 설정
t.speed(0)                # 터틀의 속도 설정

def draw_line():          # 라인 그리는 함수 만들기
    t.forward(100)
    t.backward(100)

for x in range(12):       # 함수 반복 설정
    t.right(30)
    draw_line()
