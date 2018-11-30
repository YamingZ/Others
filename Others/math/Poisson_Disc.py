import math
import time
import tkinter as tk
import random



def draw_point(point,color):
    x1, y1 = (point[0] - 1.5), (point[1] - 1.5)
    x2, y2 = (point[0] + 1.5), (point[1] + 1.5)
    canvas.create_oval(x1, y1, x2, y2, fill=color)
    canvas.update_idletasks()

def random_process():
    for i in range(1000):
        x = random.randint(0,400)
        y = random.randint(0,400)
        draw_point((x,y),"red")
        time.sleep(0.01)

def poisson_process():
    K = 1000
    r = 10
    width = 400
    height = 400
    grid = []
    active = []
    w = r/math.sqrt(2)
    found = False

#STEP 0
    cols = math.floor(width/w)
    rows = math.floor(height/w)
    for i in range(cols*rows):
        grid.append(False)

#STEP 1
    x,y = random.uniform(0,width),random.uniform(0,height)  #平面点集取点
    i,j = math.floor(x/w),math.floor(y/w)
    pos = (x,y)
    grid[i+j*cols] = pos
    active.append(pos)


    while len(active)>0 :
        index = math.floor(random.uniform(0,len(active)))
        apos = active[index]
        for i in range(K):
            a = random.uniform(0,6.28)
            m = random.uniform(r, 2 * r)
            offsetX,offsetY = m*math.cos(a),m*math.sin(a)
            sample = (offsetX + apos[0],offsetY + apos[1])

            col = math.floor(sample[0] / w)
            row = math.floor(sample[1] / w)

            if col > 0 and row > 0 and col < cols and row < rows and grid[col + row*cols] == False:
                ok = True
                for i in range(-1,2,1):
                    for j in range(-1,2,1):
                        if col + i >= 0 and row + j >=0 and col + i < cols and row + j < rows:
                            neighbor = grid[(col + i) + (row + j) * cols]
                            if neighbor:
                                d = math.sqrt((neighbor[0] - sample[0])**2 + (neighbor[1] - sample[1])**2)
                                if d < r:
                                    ok = False
                if ok:
                    found = True
                    grid[col + row * cols] = sample
                    active.append(sample)
                    draw_point(sample,"red")

        #k个都不满足要求，将该点作为稳定点，并从激活点集中删除
        if ~found:
            draw_point(active[index], "white")
            active.pop(index)

        # time.sleep(0.02)

    # last draw
    # for point in grid:
    #     if point:
    #         draw_point(point,"white")
    #
    # for point in active:
    #     if point:
    #         draw_point(point,"red")




root = tk.Tk()
canvas = tk.Canvas(root, width=400,
                        height=400, bg="black")
canvas.pack()
root.title("Tkinter MVC example")
root.resizable(width=False, height=False)

poisson_process()
# random_process()
root.mainloop()
