import turtle
import time
import random
import winsound  # Works on Windows only; comment out if on Mac/Linux

delay = 0.1
score = 0
high_score = 0

# 🎨 Set up the screen
wn = turtle.Screen()
wn.title("🐍 Snake Game by Salma")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

# 🐍 Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 🍎 Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(random.choice(["red", "yellow", "orange", "pink", "cyan"]))
food.penup()
food.goto(0, 100)

segments = []

# 🧾 Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "bold"))

# 🎮 Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# ⌨️ Keyboard controls
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# 🎯 Main Game Loop
while True:
    wn.update()

    # 💥 Collision with wall
    if abs(head.xcor()) > 340 or abs(head.ycor()) > 340:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Reset segments
        for seg in segments:
            seg.goto(1000, 1000)
        segments.clear()

        # Reset score and delay
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "bold"))
        winsound.Beep(200, 200)

    # 🍏 Collision with food
    if head.distance(food) < 20:
        winsound.Beep(600, 150)
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        food.goto(x, y)
        food.color(random.choice(["red", "yellow", "orange", "pink", "cyan", "lightgreen"]))

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        delay = max(0.05, delay - 0.002)  # Increase speed gradually
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "bold"))

    # 🐍 Move the body
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # 💀 Collision with itself
    for segment in segments:
        if segment.distance(head) < 20:
            winsound.Beep(200, 200)
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "bold"))
    time.sleep(delay)
