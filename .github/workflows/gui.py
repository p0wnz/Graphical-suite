import pygame;import functions
class Label:
    text=""
    image=None
    fontt=None
    font=""
    color=(0,0,0)
    size=00
    pos=(0,0)
    centered=False
    posc=(0,0)
    surface=None
    def __init__(self,surface,font,size,text,color,pos):
        self.fontt =functions.font_chooser(font,size)
        self.font = font
        self.size = size
        self.surface = surface
        self.color=color
        self.text = text
        self.pos = pos
        
        self.calculate(text,color)
        self.center()
    def calculate(self,text,color):
        self.image =self.fontt.render(text,True,color)
    def update(self):
        if self.centered ==True:
            self.surface.blit(self.image,self.posc)
        else:
            self.surface.blit(self.image,self.pos)
    def recalc(self):
        self.center()    
        self.fontt =functions.font_chooser(self.font,self.size)
        self.calculate(self.text,self.color)
    def center(self):
        posc=functions.get_center(self.image.get_rect().size)
        newL =list(self.pos)
        newL[0] -= posc[0]
        newL[1] -= posc[1]
        self.posc = tuple(newL)
class Button:
    color=None
    color_bottom=()
    calculate=0
    size=None
    text_color=(255,255,255)
    text=None
    font="Fonts/Raleway-ExtraLight.ttf"
    posc=None
    pos=None
    yscale=0
    on_state=False
    surface=None
    def __init__(self,surface,size,pos,color,text):
        self.surface = surface
        self.color=color
        self.text =Label(self.surface,self.font,16,text,self.text_color,pos)
        self.pos = pos
        self.size=size
        self.center()
    def update(self):
        if self.calculate==0:
            self.calculate_now()
        pygame.draw.rect(self.surface,(self.color_bottom),[(self.pos[0],self.pos[1]),(self.size[0],self.size[1]+self.yscale)])
        if self.on_state==False:
            pygame.draw.rect(self.surface,self.color,[self.pos,self.size])
        
        self.text.update()
        pos=pygame.mouse.get_pos()
        self.on_state=False
        if pos[0] >= self.pos[0] and pos[0]<= self.pos[0]+self.size[0]:
            if pos[1] >= self.pos[1] and pos[1]<= self.pos[1]+self.size[1]:
                self.on_state=True
    def calculate_now(self):
        altercolor=[0,0,0]
        self.yscale =round(self.size[1]/10)
        for i in range(0,3):
            if self.color[i] >= 50:
                altercolor[i]+= (self.color[i]-50)
        self.color_bottom = tuple(altercolor)
    def calctext(self):
        self.center()
        self.text.posc = self.posc
        self.text.recalc()
    def center(self):
        posc=functions.get_center(self.size)
        newL =list(self.pos)
        newL[0] += posc[0]
        newL[1] += posc[1]
        self.posc = tuple(newL)
        self.text.pos = self.posc
        self.text.centered=True
        self.text.center()
    def clicked(self):
        if self.on_state:
            return True
class ListBox:
    surface = None
    images=[]
    color=None
    color_H=None
    color_selected=None
    size=(0,0)
    font="Fonts/Raleway-ExtraLight.ttf"
    bcolor=(255,255,255)
    fcolor=(0,0,0)
    fsize=12
    post=[]
    pos=(0,0)
    listt=[]
    posc=(0,0)
    width=1
    certin=0
    selected=False
    selected_index=0
    selected_item=""
    calculate=True
    on_state=False
    def __init__(self,surface,listt,color,size,pos):
        self.surface = surface
        self.color=color
        self.listt=listt
        self.size = size
        self.pos =pos
    def update(self):
        if self.calculate==True:
            self.calc()
            self.calculate=False
        pygame.draw.rect(self.surface,self.color,[self.pos,self.size],self.width)
        pygame.draw.rect(self.surface,self.bcolor,[self.pos[0]+self.width,self.pos[1]+self.width,self.size[0]-self.width-1,self.size[1]-self.width-1])
        y=0
        if self.selected==True:
            pygame.draw.rect(self.surface,self.color_selected,[self.pos[0]+self.width+1,self.pos[1]+self.post[self.selected_index]-7,self.size[0]-self.width-3,self.post[0]])
        self.on_state=False
        pos = pygame.mouse.get_pos()
        if pos[0] >= self.pos[0] and pos[0]<= self.pos[0]+self.size[0]:
            if pos[1] >= self.pos[1] and pos[1]<= self.pos[1]+self.size[1]:
                self.on_state=True
                self.certin=None
                for i in range(0,len(self.post)):
                    if (pos[1] > self.pos[1]+self.post[i]-7) and (pos[1] < self.pos[1]+self.post[i]-7+self.post[0]):
                        pygame.draw.rect(self.surface,self.color_H,[self.pos[0]+self.width+1,self.pos[1]+self.post[i]-7,self.size[0]-self.width-3,self.post[0]],1)
                        self.certin=i
        
        for item in self.images:
            self.surface.blit(item,(self.pos[0]+12,self.pos[1]+self.post[y]-7))
            y+=1
    def calc(self):
        fonter =functions.font_chooser(self.font,self.fsize)
        y=0
        x=0
        if len(self.images)>0:
            self.images=[]
            self.post=[]
        for item in self.listt:
            self.images.append(functions.write_text(fonter,item,self.fcolor))
            if y>0:
                self.post.append(self.images[y].get_rect().size[1]+1+(y*(self.images[y-1].get_rect().size[1])))
            else:
                self.post.append(self.images[y].get_rect().size[1]+1)
            y+=1
        altercolor=[0,0,0]
        for i in range(0,3):
            if self.color[i] >=200:
                altercolor[i]= (self.color[i]-100)
            elif self.color[i] >= 100:
                altercolor[i]= (self.color[i]-50)
        self.color_H=tuple(altercolor)
        altercolor=[0,0,0]
        for i in range(0,3):
            if self.color[i]==0:
                altercolor[i]= 30
            elif self.color[i] <60:
                altercolor[i]= (self.color[i]+100)
            elif self.color[i] >= 60 and self.color[i] <150:
                altercolor[i]= (self.color[i]+50)
            elif self.color[i]>=150:
                altercolor[i]= self.color[i]
        self.color_selected=tuple(altercolor)
    def clicked(self):
        if self.on_state==True:
            if self.certin!=None:
                self.selected=True
                self.selected_index=self.certin
                self.selected_item = self.listt[self.selected_index]
    def refresh_list(self):
        self.calc()
class CheckBox:
    surface=None
    images=[]
    color=(0,0,0)
    fcolor=(0,0,0)
    bcolor=(255,255,255)
    hcolor=(0,0,0)
    font="Fonts/Raleway-ExtraLight.ttf"
    scolor=(0,0,0)
    listt=None
    width=1
    fsize=12
    sizeyy=0
    sizexx=0
    xoffset=0
    post=[]
    size=(8,8)
    inv=0
    pos=(0,0)
    selected=False
    on_state=False
    selected_index=[]
    selectedICONS=[]
    curtains=-1
    selected_item=[]
    def __init__(self,surface,color,listt,pos):
        self.surface= surface
        self.color=color
        self.listt = listt
        self.pos = pos
    def update(self):
        if self.inv ==0:
            self.calc()
            self.inv+=1
        if self.selected:
            for i in self.selected_index:
                pygame.draw.rect(self.surface,self.scolor,[(self.pos[0]+self.xoffset+(2*self.size[0]),self.pos[1]+self.post[i]-7),self.size])
        y=0
        for item in self.images:
            pygame.draw.rect(self.surface,self.color,[(self.pos[0]+self.xoffset+(2*self.size[0])+1,self.pos[1]+self.post[y]-7+1),(self.size[0]-1,self.size[1]-1)],self.width)
            self.surface.blit(item,(self.pos[0]+3,self.pos[1]+self.post[y]-7))
            y+=1
        pos = pygame.mouse.get_pos()
        self.on_state=False
        if pos[0] >= self.pos[0] and pos[0]<= self.sizexx+self.size[0]+self.pos[0]:
            if pos[1] >= self.pos[1] and pos[1]<= self.pos[1]+self.sizeyy:
                self.on_state=True
                for i in range(0,len(self.post)):
                    if (pos[1] > self.pos[1]+self.post[i]-7) and (pos[1] < self.pos[1]+self.post[i]-7+self.post[0]):
                        pygame.draw.rect(self.surface,self.hcolor,[self.pos[0]+self.width+1,self.pos[1]+self.post[i]-7,self.sizexx+self.size[0],self.post[0]],1)
                        self.curtains=i
    def calc(self):
        fonter =functions.font_chooser(self.font,self.fsize)
        y=0
        x=0
        if len(self.images)>0:
            self.images=[]
            self.post=[]
        for item in self.listt:
            self.images.append(functions.write_text(fonter,item,self.fcolor))
            if y>0:
                self.post.append(self.images[y].get_rect().size[1]+1+(y*(self.images[y-1].get_rect().size[1])))
            else:
                self.post.append(self.images[y].get_rect().size[1]+1)
            y+=1
        altercolor=[0,0,0]
        for i in range(0,3):
            if self.color[i] >=200:
                altercolor[i]= (self.color[i]-100)
            elif self.color[i] >= 100:
                altercolor[i]= (self.color[i]-50)
        self.hcolor=tuple(altercolor)
        altercolor=[0,0,0]
        for i in range(0,3):
            if self.color[i]==0:
                altercolor[i]= 30
            elif self.color[i] <60:
                altercolor[i]= (self.color[i]+100)
            elif self.color[i] >= 60 and self.color[i] <150:
                altercolor[i]= (self.color[i]+50)
            elif self.color[i]>=150:
                altercolor[i]= self.color[i] 
        self.scolor=tuple(altercolor)
        self.xffset()
    def xffset(self):
        maxoffset=0
        for image in self.images:
            if image.get_rect().size[0] > maxoffset:
                maxoffset=image.get_rect().size[0]
        self.xoffset = maxoffset
        self.sizexx = (2*self.size[0])+maxoffset
        self.sizeyy = (len(self.listt) * self.images[0].get_rect().size[1])
    def clicked(self):
         if self.on_state:
            if self.curtains!=-1:
                if len(self.selected_index)!=0:
                    if not(self.curtains in self.selected_index):
                        self.selected_index.append(self.curtains)
                        self.selected=True
                        self.selected_item.append(self.listt[self.curtains])
                        self.curtains=-1
                    else:
                        self.selected_index.remove(self.curtains)
                        if len(self.selected_index)!=0:
                            self.selected=True
                        else:self.selected=False
                        self.selected_item.remove(self.listt[self.curtains])
                        self.curtains=-1
                else:
                    self.selected_index.append(self.curtains)
                    self.selected=True  
                    self.selected_item.append(self.listt[self.curtains])
                    self.curtains=-1

class textBox:
    surface=None
    list_text=[]
    string=""
    string_toDisplay=""
    surface=None
    color=None
    hcolor=None
    ffont=None
    font="Fonts/Raleway-ExtraLight.ttf"
    fsize=24
    evk=True
    width=1
    fcolor=(0,0,0)
    on_state=False
    imagetxt=pygame.Surface((1,1))
    clicked=False
    bcolor=(255,255,255)
    size=();evk=True
    caps=False
    cap2=False
    pos=()
    blink=0
    def __init__(self,surface,color,hcolor,pos,size):
        self.surface =surface
        self.color=color
        self.pos=pos
        self.size=size
        self.hcolor = hcolor
    def update(self):
        if self.evk:
            self.calc();self.evk=False
        color = self.color
        if self.on_state:
            color=self.hcolor
        if self.clicked:
            self.blink+=1
            if self.blink>22:
                pygame.draw.rect(self.surface,(0,0,0),[self.imagetxt.get_rect()[0]+self.imagetxt.get_rect()[2]+2,self.pos[1]+4,1,self.fsize])
                
            if self.blink>45:self.blink=1
        pygame.draw.rect(self.surface,color,[self.pos,self.size],self.width)
        if self.string != "":
            self.surface.blit(self.imagetxt,(self.pos[0]+4,self.pos[1]+4))
        pos = pygame.mouse.get_pos()
        self.on_state=False
        if pos[0] >= self.pos[0]-2 and pos[0]<= self.size[0]+self.pos[0]:
            if pos[1] >= self.pos[1]-2 and pos[1]<= self.pos[1]+self.size[1]:
                self.on_state=True
		
    def calc(self):
        self.ffont =functions.font_chooser(self.font,self.fsize)
        self.size=(self.size[0],functions.write_text(self.ffont,"hello",self.fcolor).get_rect().size[1]+4)
    def Click(self):
        if self.on_state:
            self.clicked=True
        else: self.clicked=False
    def press(self,event):
        if self.clicked:
            self.type_(event)
    def type_(self,event):
        string= pygame.key.name(event.key)
        
        if string.lower()=='space':
            string=' '
            self.string+=string
            self.list_text.append(string)
            self.string_toDisplay =self.string
            i=1
            while functions.write_text(self.ffont,self.string_toDisplay,self.fcolor).get_rect().size[0]+4 > self.size[0]:
                self.string_toDisplay = self.string[i:]
                i+=1
            self.imagetxt=(functions.write_text(self.ffont,self.string_toDisplay,self.fcolor))
            return
        elif string.lower() == "right shift" or string.lower() == "left shift":
            self.caps=True
        elif string.lower() == "return":
            self.clicked=False
        elif string.lower() == "caps lock":
            print( self.cap2)
            if self.cap2:
                self.cap2=False
            else:
                self.cap2=True
        elif string.lower()=='backspace':
            string=''
            self.string+=string
            self.string = self.string[:-1]
            self.string_toDisplay =self.string
            i=1
            while functions.write_text(self.ffont,self.string_toDisplay,self.fcolor).get_rect().size[0]+4 > self.size[0]:
                self.string_toDisplay = self.string[i:]
                i+=1
            self.imagetxt=(functions.write_text(self.ffont,self.string_toDisplay,self.fcolor))
            return
        else:
            if self.caps or self.cap2==True:
                string =string.upper()
            self.string+=string
            self.list_text.append(string)
            self.string_toDisplay =self.string
            i=1
            while functions.write_text(self.ffont,self.string_toDisplay,self.fcolor).get_rect().size[0]+4 > self.size[0]:
                self.string_toDisplay = self.string[i:]
                i+=1
            self.imagetxt=(functions.write_text(self.ffont,self.string_toDisplay,self.fcolor))
            return
    def event2(self,event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                self.caps=False
