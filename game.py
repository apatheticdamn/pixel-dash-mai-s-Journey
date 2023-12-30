import pygame
import sys

pygame.init()

start_time = int(pygame.time.get_ticks()/1000)

def display_score():
    global current_time
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    return current_time

fps = 30

rose = (225, 29, 72) 
dodger_blue = '#9ecfff'

screen_width, screen_height = 800, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Dash: Mai's Journey")
icon = pygame.image.load("graphics/appicon/mai_san_app_icon.jpg")
pygame.display.set_icon(icon)

sky_surf = pygame.image.load("graphics/Sky.png").convert()
sky_surf_resized = pygame.transform.scale(sky_surf, (800, 300))
sky_rect = sky_surf_resized.get_rect(midtop = (400, 0))

ground_surf = pygame.image.load("graphics/ground.jpg").convert_alpha()
ground_resized = pygame.transform.scale(ground_surf, (800, 100))
ground_rect = ground_resized.get_rect(midtop = (400, 300))

clock = pygame.time.Clock()

game_header_surf = pygame.font.Font("font/Pixeltype.ttf", 50)
game_header_surf_render = game_header_surf.render("Pixel Dash:  Mai's Journey", False, "Black")
game_header_rect = game_header_surf_render.get_rect(center = (400, 50))

game_footer_surf = pygame.font.Font("font/Pixeltype.ttf", 20)
game_footer_render = game_footer_surf.render("Created by: Apathetic", True, (64,64,64))
game_footer_rect = game_footer_render.get_rect(midleft = (10, 380))

car_surf = pygame.image.load("graphics/car/car.png").convert_alpha()
car_surf_resized = pygame.transform.scale(car_surf, (60, 30))
car_rect = car_surf_resized.get_rect(midbottom = (50, 300))
car_rect.right = 600

player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (90, 300))
player_gravity = 0

player_stand_surf = pygame.image.load("graphics/Player/mai_san_stand3.png").convert_alpha()
player_stand_resized = pygame.transform.scale(player_stand_surf, (300, 300))
player_stand_rect = player_stand_resized.get_rect(midtop = (400, 0))

player_stand_surf2 = pygame.image.load("graphics/Player/mai_san_stand2.png").convert_alpha()
player_stand_resized2 = pygame.transform.scale(player_stand_surf2, (100, 100))
player_stand_rect2 = player_stand_resized2.get_rect(midright = (829, 356))


instruction = pygame.font.Font("font/Pixeltype.ttf", 50)
instruction_render = instruction.render("Press Space to play again!", False, (64, 64, 64))
instruction_rect = instruction_render.get_rect(midtop = (400, 350))

score = 0


game_active = True

while True:
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    mouse_left_click = (True, False, False)
    mouse_button_press = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                car_rect.x = 800
                score = 0
                start_time = int(pygame.time.get_ticks()/1000)
                
                
           
       # if event.type == pygame.MOUSEBUTTONUP:
       #     print("Mouse button up")
       # if event.type == pygame.MOUSEBUTTONDOWN:
       #     print("Mouse button down")
       # if event.type == pygame.MOUSEMOTION:
       #     if player_rect.collidepoint(event.pos): print("Collision")
      
    screen.blit(sky_surf_resized, sky_rect)
    screen.blit(ground_resized, ground_rect)
    screen.blit(game_header_surf_render, game_header_rect)
        
    #pygame.draw.line(screen, "Gold", (0,0), pygame.mouse.get_pos(), width = 10)
    #pygame.draw.rect(screen, sky_grey_c, game_header_rect, width = 0, border_radius=10)

    
    if game_active:
        score = display_score()
        score_text = pygame.font.Font("font/Pixeltype.ttf", 40)
        score_text_render = score_text.render(f"Score: {score}", False, "Black")
        score_text_rect = score_text_render.get_rect(midright = (760, 50))
        screen.blit(score_text_render, score_text_rect)
       
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300: player_rect.bottom = 300 
        screen.blit(player_surf, player_rect)

        car_rect.x -= 5
        if car_rect.right < 0: car_rect.left = 800
        screen.blit(car_surf_resized, car_rect)

        if player_rect.colliderect(car_rect):
            game_active = False
            score = 0

        #    if player_rect.collidepoint(mouse_pos):
    #       print(pygame.mouse.get_pressed())
        
        #if player_rect.collidepoint(mouse_pos):
        #    if pygame.mouse.get_pressed() == (True, False, False):
        #        player_gravity = -20
             
        
        
        #key = pygame.key.get_pressed() 
        #if key[pygame.K_SPACE]:
        #    print("Jump")
    else:
        screen.fill(dodger_blue)
        screen.blit(player_stand_resized2, player_stand_rect2)
        screen.blit(instruction_render, instruction_rect)
        screen.blit(player_stand_resized, player_stand_rect)
        screen.blit(game_footer_render, game_footer_rect)

        
    pygame.display.update()
    clock.tick(fps)









