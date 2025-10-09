import pygame as pg

WIDTH=500
HEIGHT=500
pg.init()
pg.display.set_mode((WIDTH, HEIGHT))

print(pg.KEYDOWN)
cnt=0

def get_all_events(max=2000):
    for i in range(pg.NUMEVENTS):
        if pg.event.event_name(i) != "Unknown":
            print(i, pg.event.event_name(i))
        if(i>max):
            break

get_all_events()

max_cnt = 10000
while max_cnt>cnt:
    cnt+=1
    events = pg.event.get()
    pg.display.flip()
    if len(events):
        event=events[0]
        if event.type == pg.KEYDOWN:
            print(event)
            pg.quit()
            break
