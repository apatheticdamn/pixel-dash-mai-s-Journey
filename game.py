import pygame
import sys
import random

pygame.init()

start_time = int(pygame.time.get_ticks()/1000)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(car_surf_resized, obstacle_rect)
            else:
                screen.blit(bird_resized, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player_rect.colliderect(obstacle_rect): return False 
    return True 

def display_score():
    if game_active:
        global current_time
        current_time = int(pygame.time.get_ticks()/1000) - start_time
    return current_time

fps = 60

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

bird_surf = pygame.image.load("graphics/bird/bird_flying1.png")
bird_resized = pygame.transform.scale(bird_surf, (40, 30))
bird_rect = bird_resized.get_rect(midright = (600, 130))



obstacle_rect_list = []

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
instruction_rect = instruction_render.get_rect(midtop = (400, 330))

score = 0
end_score = 0

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

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
        if game_active and event.type == obstacle_timer:
            if random.randint(0,2):
                obstacle_rect_list.append(car_surf_resized.get_rect(midbottom = (random.randint(900,1100), 300)))
            else:     
                obstacle_rect_list.append(bird_resized.get_rect(midbottom = (random.randint(900,1100), 130)))

                
    screen.blit(sky_surf_resized, sky_rect)
    screen.blit(ground_resized, ground_rect)
    screen.blit(game_header_surf_render, game_header_rect)
        
       
    if game_active:
        score = display_score()
        game_score_font = pygame.font.Font("font/Pixeltype.ttf", 40)
        game_score_text = game_score_font.render(f"Score: {score}", False, "Black")
        game_score_rect = game_score_text.get_rect(midright = (760, 50))
        screen.blit(game_score_text, game_score_rect)
       
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300: player_rect.bottom = 300 
        screen.blit(player_surf, player_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        car_rect.x -= 6
        if car_rect.right < 0: car_rect.left = 800
        
        game_active = collision(player_rect, obstacle_rect_list) 
        

        
    else:
        screen.fill(dodger_blue)
        screen.blit(player_stand_resized2, player_stand_rect2)
        screen.blit(instruction_render, instruction_rect)
        screen.blit(player_stand_resized, player_stand_rect)
        screen.blit(game_footer_render, game_footer_rect)
        end_score_font = pygame.font.Font("font/Pixeltype.ttf", 36,)
        end_score_render = end_score_font.render(f"Your Score: {end_score}", False, (64, 64, 64))
        end_score_rect = end_score_render.get_rect(midtop = (400, 300))
        screen.blit(end_score_render, end_score_rect)
        end_score = display_score()

        player_rect.midbottom = (90, 300)
        player_gravity = 0

        obstacle_rect_list.clear()
    pygame.display.update()
    clock.tick(fps)








