import pygame as pg

def get_all_events(max=2000):
    for i in range(pg.NUMEVENTS):
        if pg.event.event_name(i) != "Unknown":
            print(i, pg.event.event_name(i))
        if(i>max):
            break

WIDTH=800
HEIGHT=800
GLID_RECT_SIZE=100
GLID_SIZE=4
BOARD_OFFSET=50

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))

board_size = GLID_RECT_SIZE*GLID_SIZE+20
def draw_board(x=40,y=40,edge_color=(0,0,0),color=(50,50,50)):
    pg.draw.rect(screen, color, (x,y,board_size,board_size), 0)

font = pg.font.Font(None,100)
fonts = [font.render(str(i),0,(200,200,200)) for i in range(20)]
fonts[0]=font.render(" ",0,(200,200,200))

class Pannel:
    def __init__(self,pos,num):
        self.pos = pos
        self.num = num
        self.color = (100,100,100)
        self.eg_color = (0,0,0)

    def draw(self):
        x = BOARD_OFFSET+self.pos%GLID_SIZE*GLID_RECT_SIZE
        y = BOARD_OFFSET+self.pos//GLID_SIZE*GLID_RECT_SIZE
        pg.draw.rect(screen, self.color, (x, y,GLID_RECT_SIZE,GLID_RECT_SIZE), 0)
        pg.draw.rect(screen, self.eg_color, (x,y ,GLID_RECT_SIZE,GLID_RECT_SIZE), 3)
        g_font = fonts[self.num]
        font_rect = g_font.get_rect()
        ofsets = (GLID_SIZE-font_rect[2], GLID_SIZE-font_rect[3])
        screen.blit(g_font,(x+ofsets[0]/2+GLID_RECT_SIZE/2,y+ofsets[1]/2+GLID_RECT_SIZE/2))

def draw_pannel(x,y,num,edge_color=(0,0,0),color=(100,100,100)):
    pg.draw.rect(screen, color, (x,y,GLID_RECT_SIZE,GLID_RECT_SIZE), 0)
    pg.draw.rect(screen, edge_color, (x,y,GLID_RECT_SIZE,GLID_RECT_SIZE), width=3)
    g_font = fonts[num]
    font_rect = g_font.get_rect()
    ofsets = (GLID_SIZE-font_rect[2], GLID_SIZE-font_rect[3])
    screen.blit(g_font,(x+ofsets[0]/2+GLID_RECT_SIZE/2,y+ofsets[1]/2+GLID_RECT_SIZE/2))

def draw_grid(tx=50,ty=50):
    for i in range(GLID_SIZE):
        for j in range(GLID_SIZE):
            if i+j == 0:
                continue
            dx= tx+j*GLID_RECT_SIZE
            dy= ty+i*GLID_RECT_SIZE
            num=i*GLID_SIZE+j
            draw_pannel(dx,dy,num) 

while True:
    events = pg.event.get()

    screen.fill((0,0,0))
    #draw_board()
    #draw_grid()
    pannel = Pannel(1,1)
    pannel.draw()
    pg.display.flip()

    flag=0

    for event in events:
        if event.type == pg.KEYDOWN:
            print(event)
            pg.quit()
            flag=1
            break

    if flag:
        break
