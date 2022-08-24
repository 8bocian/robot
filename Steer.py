#  Copyright (c) 2022. Oskar "Bocian" Możdżeń
#  All rights reserved.

from Utilities import *
from keyboard import is_pressed

WIDTH, HEIGHT = 800, 800
FPS = 60

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
run = True
t = 0
dt = 0.01
rotate_angle = 0
current_angle_1, current_angle_2 = 0, 0

trans = Translator(WIDTH // 2, HEIGHT // 2)
leg = Leg(100, 0, 100, 0, 30, 0, trans, screen)

while run:
    t += dt
    screen.fill(BLACK)
    clock.tick(FPS)

    desired_angle_1, desired_angle_2, desired_angle_3 = leg.move(rotate_angle)
    print(np.rad2deg(desired_angle_1), np.rad2deg(desired_angle_2), np.rad2deg(desired_angle_3))
    leg.show()

    pg.display.flip()
    if is_pressed("["):
        rotate_angle -= 0.1
    if is_pressed("]"):
        rotate_angle += 0.1
    rotate_angle = np.clip(rotate_angle, -np.pi / 2, np.pi / 2)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            break
