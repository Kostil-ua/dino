from objects import*
from levels import*

pygame.init()

level1_objects, key, chest = draw_level(level1)
#player
#portal

""" Кнопки для меню """
btn_play = Button(465, 250, 350, 100, (170, 139, 231), "PLAY", 60, (255, 255, 255))
btn_instructions = Button(465, 400, 350, 100, (170, 139, 231), "INSTRUCTIONS", 60, (255, 255, 255))
btn_exit = Button(465, 550, 350, 100, (170, 139, 231), "EXIT", 60, (255, 255, 255))

mode = "menu"

game = True
finish = False
while game:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            if btn_play.rect.collidepoint(x, y):
                mode = "game"
            if btn_exit.rect.collidepoint(x, y):
                game = False


    if mode == "menu":
        window.blit(bg, (0, 0))
        window.blit(game_name, (200, 50))

        btn_play.draw(120, 30)
        btn_instructions.draw(15, 30) 
        btn_exit.draw(120, 30)

    if mode == "game":
        if not finish:
            window.blit(bg, (0, 0))

            for obj in level1_objects:
                window.blit(obj.image, camera.apply(obj))
            #camera.update(player)

            #camera.update(platforms)




        

    pygame.display.update()
    clock.tick(FPS)
















