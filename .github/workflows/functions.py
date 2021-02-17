import pygame,os
pygame.font.init()
def set_screen(screen_resolution,caption,icon,centered,custom_cursor):
    pygame.init()
    if (centered):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode(screen_resolution)
    pygame.display.set_caption(caption)
    pygame.display.set_icon(pygame.image.load(icon))
    if custom_cursor==True:
        pygame.mouse.set_visible(False)
    return screen
def update(clock,tick):
    pygame.display.update()
    if clock != "":
        clock.tick(60)
def set_cursor(screen,image):
    screen.blit(image,pygame.mouse.get_pos())
def font_chooser(font,size):
    fontt=pygame.font.Font(font,size)
    return fontt
def write_text(font,text,color):
    return (font.render(text,True,color))
def get_center(size):
    posxc=size[0]/2
    posyc=size[1]/2
    return (posxc,posyc)
