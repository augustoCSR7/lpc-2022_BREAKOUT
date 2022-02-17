import pygame

# Initialize pygame for game machanics
pygame.init()
# Initialize pygame for game sounds
pygame.mixer.init()

s_width = 900
s_height = 1010
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("BREAKOUT")
clock = pygame.time.Clock()

def main_game():
    
    start_game = True
    while start_game:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_game = False
                
        screen.fill((0, 0, 0))

        pygame.display.update()
        clock.tick(60)
        
        
    pygame.quit()

main_game()