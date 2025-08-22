from setting import*

class Main:
    def __init__(self):
        
        # general
        pygame.init()
        self.screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        
        # game object
        self.bg_rect=[pygame.Rect(COL*CELL_SIZE,0,CELL_SIZE,CELL_SIZE) for COL in range(0,COLN,2)]
        
    def draw_bg(self):
        for rect in self.bg_rect:
            pygame.draw.rect(self.screen, 'red', rect)
            
                
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            # drawing code should be outside the event loop
            self.screen.fill(LIGHT_GREEN)
            self.draw_bg()
            pygame.display.update()


              
main=Main()
main.run()

