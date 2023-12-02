def on_button_pressed_a():
    global bullet
    bullet = game.create_sprite(space_ship.get(LedSpriteProperty.X),
        space_ship.get(LedSpriteProperty.Y))
    bullet.turn(Direction.LEFT, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def hs():
    global shshs
    if bullet.is_touching(shshs):
        game.add_score(1)
        bullet.delete()
        shshs.delete()
        shshs = game.create_sprite(randint(0, 4), 0)
    elif bullet.get(LedSpriteProperty.Y) == 0:
        bullet.delete()
    else:
        pass
bullet: game.LedSprite = None
shshs: game.LedSprite = None
space_ship: game.LedSprite = None
space_ship = game.create_sprite(2, 4)
shshs = game.create_sprite(randint(0, 4), 0)
game.start_countdown(10000)

def on_forever():
    space_ship.move(1)
    space_ship.if_on_edge_bounce()
    if bullet:
        bullet.move(1)
        hs()
    basic.pause(200)
basic.forever(on_forever)
