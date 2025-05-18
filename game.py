from objects import*
from levels import*

pygame.init()

level1_objects, key, chest = draw_level(level1)
player = Player(50, H - 90, 40, 50, 10, player_images)
portal = MapObject(-300, -300, 80, 80, portal_image)

level1_objects.add(portal)
level1_objects.add(player)

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

            camera.update(player)

            player.update(platforms)

            if pygame.sprite.spritecollide(player, coins, True):
                coints_count += 1

            window.blit(pygame.transform.scale(coin_image, (40, 40)), (10, 10))
            coins_txt = font1.render(f": {coints_count}", True, (255, 255, 255))
            window.blit(coins_txt, (55, 10))

            if portal:
                if coints_count > 1:
                    portal.rect.x = 1300
                    portal.rect.y = 600

                if pygame.sprite.collide_rect(player, portal):
                    for obj in level1_objects:
                        obj.kill()

                    for platform in platforms:
                        platform.kill()

                    del portal

                    portal = None

                    level1_objects, key, chest = draw_level(level2)

                    player.rect.x = 50
                    player.rect.y = H - 90
                    level1_objects.add(player)

            if player.rect.y > 650:
                finish = True


    pygame.display.update()
    clock.tick(FPS)
