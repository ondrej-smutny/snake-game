from turtle import Turtle, Screen
import time #musíme importovat, aby python rozuměl času
import random

# Proměnné
score = 0
highest_score = 0

screen = Screen()
screen.bgcolor("green") # barva pozadí
screen.title("Vítejte ve Snage game") # titulek okna
screen.setup(width=600, height=600) # šířka výška okna
screen.tracer(False) # zapnutí manuální aktualizace / vypnutí automatické aktualizace (musíme dobu aktualizace nastavit dále v kódu)

# Hadí hlava, jablko a skóre
head = Turtle("square") # typ objektu hlava
head.color("black") # barva želvy / čtverce
head.speed(0) #rychlost
head.penup() # zvedne pero, aby za sebou nezanechával stopu (barvu)
head.goto(0, 0) # začíná v souřadnici 0, 0
head.direction = "right"

apple = Turtle("circle") # potrava
apple.color("red")
apple.penup()
apple.goto(100, 100) # výchozí bod jablka

score_sign = Turtle("square") # nová želva, která bude reprezentovat skóre
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write("Skóre: 0   Nejvyšší skóre: 0", align="center", font=("Arial", 18))

body_parts = [] # prázdný list, do kterého se bude plnit tělo hada

def move():
    if head.direction == "up":
        y = head.ycor() # vrátí aktuální pozici v ose Y
        head.sety(y + 20) # k aktuální ose Y přičte 20
    elif head.direction == "down":
         y = head.ycor()
         head.sety(y - 20)
    elif head.direction == "left":
         x = head.xcor()
         head.setx(x - 20)
    elif head.direction == "right":
         x = head.xcor()
         head.setx(x + 20)

# Nastavení pohybu
def move_up():
     if head.direction != "down": # pokud směr hada není dolů, tak můžu jet nahoru (aby nenaboural sám do sebe)
          head.direction = "up" # když je proměnná head.direction "up", tak had se pohybuje nahoru

def move_left():
     if head.direction != "right":
          head.direction = "left"

def move_right():
     if head.direction != "left":
          head.direction = "right"

def move_down():
     if head.direction != "up":
          head.direction = "down"

# Stisknutí klávesy
screen.listen() # zapnutí čtení / sledování programu, co stiskneme
screen.onkeypress(move_up, "w") # stisknutí klávesy "w" znamená spuštění funkce move_forward()
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# Opakující se cyklus
while True:
    screen.update() # pokyn k aktualizaci okna

    # Kontrola kolize s hranou plátna
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290: # pokud nastane jednaz těchto podmínek
         time.sleep(2)
         head.goto(0, 0)
         head.direction = "stop"

         # Skryjeme všechny části těla (čtverečky)
         for one_body_part in body_parts:
              one_body_part.goto(1500, 1500)

        # Vyprázdníme list s částmi těla (čtverečky)
         body_parts.clear()

         # Resetování score
         score = 0
         score_sign.clear() # vyčistíme aktuální score_sign
         score_sign.write(f"Skóre: {score}   Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18)) # dynamické skóre

    # Kolize hlavy s jablkem
    if head.distance(apple) < 20: # jestliže je hlava na potravě (méně něž 20 bodů), tak ...
         x = random.randint(-280, 280) # vygeneruj novou sořadnici pro potravu v ose x
         y = random.randint(-280, 280) # vygeneruj novou sořadnici pro potravu v ose y
         apple.goto(x, y) # přesuň potravu na nové souřadnice

         # Přidání části těla
         new_body_part = Turtle("square") # nový čtverec, který bude znázorňovat tělo hada
         new_body_part.speed(0)
         new_body_part.color("grey")
         new_body_part.penup()
         body_parts.append(new_body_part) # přidá do listu body_part (nyní prázdný) nový čtverec new_body_part

         # Zvýšení skóre
         score += 1

         if score > highest_score:
              highest_score = score

         score_sign.clear() # vyčistíme aktuální score_sign
         score_sign.write(f"Skóre: {score}   Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18)) # dynamické skóre

    for index in range(len(body_parts)-1, 0, -1):
         x = body_parts[index-1].xcor()
         y = body_parts[index-1].ycor()
         body_parts[index].goto(x, y)

# Nultý čtvereček (přilepí se hned za hlavu)
    if len(body_parts) > 0: # jestliže je list větší než 0 / má alespoň jedno tělo
        x = head.xcor() # uloží aktuální souřadnici hlavy v ose x
        y = head.ycor()
        body_parts[0].goto(x, y) # vloží nultý čtverec na pozici aktuální hlavy

# První čtvereček (přilepí se za nultý čtvereček)

    move() # spustíme funkci s pohybem. Nyní přesunu to za IF

    # Hlava narazila do těla
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"

            # Resetování score
            score = 0
            score_sign.clear() # vyčistíme aktuální score_sign
            score_sign.write(f"Skóre: {score}   Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 18)) # dynamické skóre

            # Skryjeme všechny části těla (čtverečky)
            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500)

            # Vyprázdníme list s částmi těla (čtverečky)
            body_parts.clear()
            
    time.sleep(0.1) # doba aktualizace okna
    
screen.exitonclick()
