import pygame

pygame.init()
pygame.mixer.init()


APP_DATA = {
    "SIZE": (800, 600),
    "TITLE": 'Simple Piano',
    "ICO": 'assets\\icon.png'
}





def main():
    
    logo = pygame.image.load(APP_DATA['ICO'], 'png')

    display = pygame.display.set_mode(APP_DATA["SIZE"])

    pygame.display.set_caption(APP_DATA["TITLE"])
    pygame.display.set_icon(logo)
    
    running = True
    while running:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        
        display.fill((0, 0, 0))


        pygame.display.flip()

    pygame.mixer.stop()
    pygame.mixer.quit()
    pygame.quit()


if __name__ == "__main__":
    main()