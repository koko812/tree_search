import pygame as pg

def get_all_events(max=2000):
    for i in range(pg.NUMEVENTS):
        if pg.event.event_name(i) != "Unknown":
            print(i, pg.event.event_name(i))
        if(i>max):
            break

WIDTH=500
HEIGHT=500
GLID_RECT_SIZE=100
GLID_SIZE=4
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))

x = 100

font = pg.font.Font(None,100)
fonts = [font.render(str(i),0,(200,200,200)) for i in range(20)]
fonts[0]=font.render(" ",0,(200,200,200))

def draw_pannel(x,y,num,edge_color=(0,0,0),color=(100,100,100)):
    pg.draw.rect(screen, color, (x,y,GLID_RECT_SIZE,GLID_RECT_SIZE), 0)
    pg.draw.rect(screen, edge_color, (x,y,GLID_RECT_SIZE,GLID_RECT_SIZE), width=3)
    g_font = fonts[num]
    font_rect = g_font.get_rect()
    ofsets = (GLID_SIZE-font_rect[2], GLID_SIZE-font_rect[3])
    screen.blit(g_font,(x+ofsets[0]/2,y+ofsets[1]/2))

def draw_grid(tx=50,ty=50):
    for i in range(GLID_SIZE):
        for j in range(GLID_SIZE):
            dx= tx+j*GLID_RECT_SIZE
            dy= ty+i*GLID_RECT_SIZE
            draw_pannel(dx,dy,i*GLID_SIZE+j) 

while True:
    events = pg.event.get()
    x += 0.1

    screen.fill((0,0,0))
    draw_grids()
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
