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
GLID_OFFSET=10

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
        if self.num==0:
            return
        x = BOARD_OFFSET+GLID_OFFSET+self.pos%GLID_SIZE*GLID_RECT_SIZE
        y = BOARD_OFFSET+GLID_OFFSET+self.pos//GLID_SIZE*GLID_RECT_SIZE
        pg.draw.rect(screen, self.color, (x, y,GLID_RECT_SIZE,GLID_RECT_SIZE), 0)
        pg.draw.rect(screen, self.eg_color, (x,y ,GLID_RECT_SIZE,GLID_RECT_SIZE), 3)
        g_font = fonts[self.num]
        font_rect = g_font.get_rect()
        ofsets = (GLID_SIZE-font_rect[2], GLID_SIZE-font_rect[3])
        screen.blit(g_font,(x+ofsets[0]/2+GLID_RECT_SIZE/2,y+ofsets[1]/2+GLID_RECT_SIZE/2))
        
    def move(self, dist):
        self.pos = dist


pannels = [Pannel(i,i) for i in range(16)]
zero_pos = 0

def draw_pannel(x,y,num,edge_color=(0,0,0),color=(100,100,100)):
    pg.draw.rect(screen, color, (x,y,GLID_RECT_SIZE,GLID_RECT_SIZE), 0)
    pg.draw.rect(screen, edge_color, (x,y,GLID_RECT_SIZE,GLID_RECT_SIZE), width=3)
    g_font = fonts[num]
    font_rect = g_font.get_rect()
    ofsets = (GLID_SIZE-font_rect[2], GLID_SIZE-font_rect[3])
    screen.blit(g_font,(x+ofsets[0]/2+GLID_RECT_SIZE/2,y+ofsets[1]/2+GLID_RECT_SIZE/2))

def draw_grid():
    pg.draw.rect(screen, (50,50,50), (BOARD_OFFSET,BOARD_OFFSET ,board_size,board_size), 0)
    for p in pannels:
        p.draw()

cnt = 0
mode = 0
while True:
    events = pg.event.get()
    cnt += 1

    screen.fill((0,0,0))
    #draw_board()
    #draw_grid()
    draw_grid()
    pg.display.flip()

    if cnt%1000==0:
        pannels[0].move(mode%2)
        mode+=1

    flag=0

    for event in events:
        if event.type == pg.KEYDOWN:
            print(event)
            pg.quit()
            flag=1
            break

    if flag:
        break
