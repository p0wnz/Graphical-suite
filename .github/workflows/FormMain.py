import pygame,functions,gui
def run(surface):
    running = True
    clock = pygame.time.Clock()
    cursor = pygame.transform.scale(pygame.image.load("images/cursor.png") ,(16,28))
    def_pos=500
    button = gui.Button(surface,(100,30),(300,def_pos),(210,0,125),"Button")
    title = gui.Label(surface,"Fonts/JosefinSans-Bold.ttf",24,"GUI Graphical user interface",(0,0,0),(100,0))
    lstbox = gui.ListBox(surface,["list item one","list item two","list item three","item four","item five"],(255,0,0),(200,200),(100,200))
    rlstbox = gui.ListBox(surface,["listr item one","listr item two","listr item three","item four","item five"],(0,0,255),(200,200),(400,200))
    ckbox = gui.CheckBox(surface,(255,0,0),['hello','aref','Jaffar'],(100,40))
    txtbox = gui.textBox(surface,(255,0,0),(255,50,0),(0,100),(200,24))

    def update():
        button.update()
        title.update()
        lstbox.update()
        txtbox.update();
        ckbox.update()
        rlstbox.update()
    while running:
        for event in pygame.event.get():
            txtbox.event2(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                
                txtbox.press(event)
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP:
                    button.text.color=(255,0,0)
                    button.text.recalc()
            if event.type == pygame.MOUSEBUTTONDOWN:
                txtbox.Click()
                lstbox.clicked()
                rlstbox.clicked()
                ckbox.clicked()
                if button.clicked():
                    lstbox.listt.pop()
                    lstbox.listt.append("hello")
                    lstbox.calc()
                    
                        
        ckbox.scolor=(0,0,255)
        surface.fill((255,255,255))
        update()
        functions.set_cursor(surface,cursor)
        functions.update(clock,60)    
    pygame.quit()
