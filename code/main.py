from setting import*

class Main:
    def __init__(self):
        
        # general
        pygame.init()
        self.screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        
            self.screen.fill(LIGHT_GREEN)
            pygame.display.update()
                
        
main=Main()
main.run()
