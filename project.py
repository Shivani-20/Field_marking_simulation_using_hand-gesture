import cv2
import numpy as np
from tkinter import *
from functools import partial
import math
import tkinter as tk
import winsound
import time
import random

frequency = 400
duration = 1000
f=0
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
main_list = []
t=0
delay = 400
ci = 5
sin = lambda degs: math.sin(math.radians(degs))
cos = lambda degs: math.cos(math.radians(degs))
c=0
inc=5
st=355

class Robot(object):
    COS_0, COS_180 = cos(0), cos(180)
    SIN_90, SIN_270 = sin(90), sin(270)

    def __init__(self, x, y, radius):
        self.x, self.y = x, y
        self.radius = radius
    def bounds(self):
        return (self.x + self.radius * self.COS_0, self.y + self.radius * self.SIN_270,
                self.x + self.radius * self.COS_180, self.y + self.radius * self.SIN_90)

class Robot1:
    def move_robot_horizontal_path1(self,canvas,robot,u,u1,u0,v,x,x11,x0,y,line,m1,m2,m3,m4,n1,n2,n3,n4):
        u=u+1
        if(u==v):
            line1=canvas.create_line(x11,x0,x11,x0+5, dash=(5, 2))
            self.move_robot_vertical_path1(canvas,robot,x,x11,x0,y,line1,m1,m2,m3,m4,n1,n2,n3,n4)
            return
        canvas.move(robot, 1, 0)
        canvas.delete(line)
        line=canvas.create_line(u0, u1, u, u1, dash=(5, 2))
        canvas.after(20,self.move_robot_horizontal_path1,canvas,robot,u,u1,u0,v,x,x11,x0,y,line,m1,m2,m3,m4,n1,n2,n3,n4)

    def move_robot_vertical_path1(self,canvas,robot,x,x11,x0,y,line1,m1,m2,m3,m4,n1,n2,n3,n4):
        x=x+1
        if(x==y):
            line2=canvas.create_line(m3-5, m2, m3, m2, dash=(5, 2))
            self.move_robot_horizontal_path2(canvas,robot,line2,m1,m2,m3,m4,n1,n2,n3,n4)
            return
        canvas.move(robot,0,1)
        canvas.delete(line1)
        line1 = canvas.create_line(x11, x0, x11,x, dash=(5, 2))
        canvas.after(20, self.move_robot_vertical_path1, canvas, robot, x, x11, x0, y,line1,m1,m2,m3,m4,n1,n2,n3,n4)

    def move_robot_horizontal_path2(self,canvas,robot,line2,m1,m2,m3,m4,n1,n2,n3,n4):
        m1=m1-1
        if(m1==m4):
            line3=canvas.create_line(n2,n3,n2,n3-5,dash=(5,2))
            self.move_robot_vertical_path2(canvas,robot,line3,n1,n2,n3,n4)
            return
        canvas.move(robot,-1,0)
        canvas.delete(line2)
        line2 = canvas.create_line(m3, m2, m1, m2, dash=(5, 2))
        canvas.after(20,self.move_robot_horizontal_path2,canvas,robot,line2,m1,m2,m3,m4,n1,n2,n3,n4)

    def move_robot_vertical_path2(self,canvas,robot,line3,n1,n2,n3,n4):
        n1=n1-1
        if(n1==n4):
            print("parking completed")
            exit(1)
        canvas.move(robot,0,-1)
        canvas.delete(line3)
        line3=canvas.create_line(n2,n3,n2,n1,dash=(5,2))
        canvas.after(20,self.move_robot_vertical_path2,canvas,robot,line3,n1,n2,n3,n4)


class robot2:
    def movee_horizontal1(self,robot,canvas,len1,wid1,marking,markingx1,markingy1,markingy2,obstacle,ox1,oy1,ox2,oy2,f,t,marking1,c,choice,center):
        x0, y0, x1, y1 = canvas.coords(robot)
        if((ox1+5)-(x1-5)<20) and ((ox1+5)-(x1-5)>=1):
            if(c==0):
                winsound.Beep(frequency,duration)
                c=c+1
            canvas.move(robot, 1, 1)
            x0, y0, x1, y1 = canvas.coords(robot)

        elif((x1-5)-(ox1+5)>=0) and((x0+5)-(ox2-5)<=18):
            canvas.move(robot,1,-1)
            x0, y0, x1, y1 = canvas.coords(robot)


        elif((x0+5)-(ox2-5)==19):
            f=1
            t=x0+5
            canvas.move(robot,1,0)
            x0, y0, x1, y1 = canvas.coords(robot)


        elif(x1==len1-10):
            self.movee_vertical(robot,canvas,len1,wid1,choice,center)
            return

        else:
            canvas.move(robot, 1, 0)
            x0, y0, x1, y1 = canvas.coords(robot)
            if(f==0):
                canvas.delete(marking)
                marking = canvas.create_line(markingx1, markingy1, x1 - 5, markingy2, fill="yellow", width="3")
            else:
                canvas.delete(marking1)
                marking1 = canvas.create_line(t,markingy1,x1-5,markingy2,fill="yellow", width="3")

        canvas.after(20,self.movee_horizontal1,robot,canvas,len1,wid1,marking,markingx1,markingy1,markingy2,obstacle,ox1,oy1,ox2,oy2,f,t,marking1,c,choice,center)

    def movee_vertical(self,robot,canvas,len1,wid1,choice,center):
        canvas.move(robot, 0, 1)
        x0, y0, x1, y1 = canvas.coords(robot)
        if(y1==wid1):
            mark=canvas.create_line(x0+5,y0+5,x1,y0+5,fill="yellow",width="3")
            mx1,my1,mx2,my2=canvas.coords(mark)
            self.movee_horizontal2(robot,canvas,len1,wid1,mark,mx1,my1,mx2,my2,choice,center)
            return
        canvas.after(20, self.movee_vertical, robot, canvas,len1, wid1,choice,center)

    def movee_horizontal2(self,robot,canvas,len1,wid1,mark,mx1,my1,mx2,my2,choice,center):
        canvas.move(robot,-1,0)
        x0, y0, x1, y1 = canvas.coords(robot)
        canvas.delete(mark)
        mark = canvas.create_line(x0+5, my1, mx1, my1,fill="yellow",width="3")
        if(x0==50) and (choice==2):
            exit(1)
        if(x0==50) and (choice==1):
            marking3=canvas.create_line(0,0,0,0)
            self.reach_center(robot,canvas,len1,wid1,center,marking3)
            return
        canvas.after(20, self.movee_horizontal2, robot, canvas, len1, wid1,mark,mx1,my1,mx2,my2,choice,center)

    def reach_center(self,robot,canvas,len1,wid1,center,marking3):

        x0, y0, x1, y1 = canvas.coords(robot)
        if(x1 == len1 - 10):
            exit(1)
        elif(y0+5==center):
            canvas.delete(marking3)
            marking3=canvas.create_line(55,center,x1-5,center,width="3",fill="white")
            canvas.move(robot,1,0)
        else:
            canvas.move(robot, 0, -1)

        canvas.after(20, self.reach_center, robot, canvas, len1, wid1,center,marking3)


def validateLogin(username, password):
    a=username.get()
    b=password.get()
    if(a=="root") and (b=="123"):
        tkWindow.destroy()
        hand_gesture()
    else:
        tkWindow.destroy()
        print("Username or password incorrect")
        time.sleep(3)
        exit(1)

def circular_path(x, y, radius, delta_ang):
    ang = 0
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360

def update_position(canvas, id, obj, path_iter,c,new1,new2,inc,st,new_posx1,new_posy1,new_posx2,new_posy2):
    obj.x, obj.y = next(path_iter)
    x0, y0, x1, y1 = canvas.coords(id)
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2
    dx, dy = obj.x - oldx, obj.y - oldy
    canvas.move(id, dx, dy)
    if(c!=0):
        canvas.create_arc(new_posx1,new_posy1,new_posx2,new_posy2,start=st,extent=inc,style='arc',dash=(3,1),fill="white",width="2")
        st = st-inc
    if (obj.x == new1) and (obj.y == new2):
        c = c + 1
    if (c == 2):
        exit(1)
    canvas.after(delay, update_position, canvas, id, obj, path_iter,c,new1,new2,inc,st,new_posx1,new_posy1,new_posx2,new_posy2)

def input_function():
    print("x1,y1 (------)")
    print("     (        )")
    print("      ---C---")
    print("      <--dia->")
    print("C is the centre of the circle")
    print("maximum length can be 600")
    print("maximum breadth can be 600")
    print("consider circle is inscribed in a square/rect so the coordinates are actually given for the square, after entering the coords, circular plot is drawn inside the square")
    x1 = int(input("x1 Coordinate"))
    y1 = int(input("y1 Coordinates"))
    dia = int(input("diameter of the plot"))
    return (x1, y1, dia)

def input_function1():
    print("x1,y1-------")
    print("     |     |")
    print("     |     |")
    print("     -------x2,y2")
    print("maximum length can be 600")
    print("maximum breadth can be 600")
    x1=int(input("x1 Coordinate"))
    y1=int(input("y1 Coordinates"))
    x2=int(input("x2 Coordinates"))
    y2=int(input("y2 Coordinates"))
    return(x1,y1,x2,y2)

def circle_plot():
    x1, y1, dia = input_function()
    if(x1>=600) or (y1>=600) or (x1<=10) or (y1<=10):
        print("out of range")
        time.sleep(2)
        exit(1)
    x2 = x1 + dia
    y2 = y1 + dia
    if(x2>=600) or (y2>=600):
        print("diameter is out of range")
        time.sleep(2)
        exit(1)

    new_posx1 = x1 + 15
    new_posy1 = y1 + 15
    new_posx2 = x2 - 15
    new_posy2 = y2 - 15
    new_diam = dia - 30
    new_rad = new_diam / 2
    mid_pointx = (new_posx2 + new_posx1) / 2
    mid_pointy = (new_posy1 + new_posy2) / 2
    top = tk.Tk()
    top.after(1000)
    top.title('Circular Plot marking')
    canvas = tk.Canvas(top, height=600, width=600)
    canvas.create_oval(x1, y1, x2, y2, fill="light green", outline="black")

    robot = Robot(new_posx2, mid_pointy, 8)
    robot1 = canvas.create_rectangle(robot.bounds(), fill='blue')
    canvas.pack()
    path_iter = circular_path(mid_pointx, mid_pointy, new_rad, ci)
    top.after(delay,update_position(canvas, robot1, robot, path_iter,c,new_posx2,mid_pointy,inc,st,new_posx1,new_posy1,new_posx2,new_posy2))
    top.mainloop()

def square():
    x1,y1,x2,y2=input_function1()
    if(x2-x1>600) or (y2-y1>600) or (x2-x1<0) or (y2-y1<0) or (x1<0) or (y1<0) or (x2<0) or (y2<0):
        print("out of range values")
        time.sleep(2)
        exit(1)
    if(x1==x2) or (y2==y1):
        print("plot can't be a straight line")
        time.sleep(2)
        exit(1)

    print("Marking will be drawn at:")
    print(x1+15,y1+15,x2-15,y2-15)
    new_pos1=x1+15
    new_pos2=y1+15
    new_pos3=x2-15
    new_pos4=y2-15
    master = Tk()
    master.geometry("600x600")
    master.title("square plot marking")
    canvas = Canvas(master)
    canvas.create_rectangle(x1,y1,x2,y2,fill="#90EE90",outline="black")

    canvas.pack(fill=BOTH, expand=True)
    u = new_pos1
    u1 = new_pos2
    u0 = new_pos1
    v = new_pos3

    x = new_pos2
    x11 = new_pos3
    x0 = new_pos2
    y = new_pos4

    m1 = new_pos3
    m2 = new_pos4
    m3 = new_pos3
    m4 = new_pos1

    n1 = new_pos4
    n2 = new_pos1
    n3 = new_pos4
    n4 = new_pos2

    robot = canvas.create_rectangle(new_pos1 - 4, new_pos2 - 4, new_pos1 + 4, new_pos2 + 4, fill="blue")
    line = canvas.create_line(u0, u1, u0+5, u1, dash=(5, 2))
    rr=Robot1()
    rr.move_robot_horizontal_path1(canvas, robot, u, u1, u0, v, x, x11 , x0, y,line,m1,m2,m3,m4,n1,n2,n3,n4)
    mainloop()

def road():
    wid = int(input("enter width of road can be 200 to 500"))
    len = int(input("enter length of road, can be between 300 to 1500"))
    if(len>1500) or (len<300):
        print("distance not identified")
        time.sleep(2)
        exit(1)
    if(wid<200) or (wid>500):
        print("distance not identified")
        time.sleep(2)
        exit(1)
    len1 = 50 + len
    wid1 = 150 + wid - 10
    choice = int(input("do you want a centre white line? Type '1' if yes else Type '2':"))
    obs = random.randint(80, len - 30)
    print("obstacle chosen randomly between x=80 to x=len1-30 has position:")
    print("x0:", obs, "y0:", 160, "x1:", obs + 10, "y1:", 170)

    master = Tk()
    master.geometry("2500x700")
    canvas = Canvas(master)
    canvas.configure(bg="light green")
    canvas.create_line(50, 150, 50 + len, 150)
    canvas.create_line(50, 150 + wid, 50 + len, 150 + wid)
    canvas.create_rectangle(50, 150, 50 + len, 150 + wid, fill="grey", outline="light green")
    center_point = (150 + (150 + wid)) / 2

    robot = canvas.create_rectangle(50, 160, 60, 170, fill="blue")
    obstacle = canvas.create_oval(obs, 160, obs + 10, 170, fill="red")

    marking1 = canvas.create_line(0, 0, 0, 0)
    ox1, oy1, ox2, oy2 = canvas.coords(obstacle)
    marking = canvas.create_line(50, 165, 60, 165, fill="yellow", width="3")
    markingx1 = 55
    markingy1 = 165
    markingx2 = 60
    markingy2 = 165
    canvas.pack(fill=BOTH, expand=True)
    pp = robot2()
    pp.movee_horizontal1(robot, canvas, len1, wid1, marking, markingx1, markingy1, markingy2, obstacle, ox1, oy1, ox2,
                         oy2, f, t, marking1, c, choice, center_point)
    master.mainloop()

def hand_gesture():
    while (cap.isOpened()):

        try:  # an error comes if it does not find anything in window as it cannot find contour of max area
            # therefore this try error statement

            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            kernel = np.ones((3, 3), np.uint8)

            # define region of interest
            roi = frame[100:300, 100:300]

            cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
            hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

            # define range of skin color in HSV
            lower_skin = np.array([0, 20, 70], dtype=np.uint8)
            upper_skin = np.array([20, 255, 255], dtype=np.uint8)

            # extract skin colur imagw
            mask = cv2.inRange(hsv, lower_skin, upper_skin)

            # extrapolate the hand to fill dark spots within
            mask = cv2.dilate(mask, kernel, iterations=4)

            # blur the image
            mask = cv2.GaussianBlur(mask, (5, 5), 100)

            # find contours
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # find contour of max area(hand)
            cnt = max(contours, key=lambda x: cv2.contourArea(x))

            # approx the contour a little
            epsilon = 0.0005 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            # make convex hull around hand
            hull = cv2.convexHull(cnt)

            # define area of hull and area of hand
            areahull = cv2.contourArea(hull)
            areacnt = cv2.contourArea(cnt)

            # find the percentage of area not covered by hand in convex hull
            arearatio = ((areahull - areacnt) / areacnt) * 100

            # find the defects in convex hull with respect to hand
            hull = cv2.convexHull(approx, returnPoints=False)
            defects = cv2.convexityDefects(approx, hull)

            # l = no. of defects
            l = 0

            # code for finding no. of defects due to fingers
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(approx[s][0])
                end = tuple(approx[e][0])
                far = tuple(approx[f][0])
                pt = (100, 180)

                # find length of all sides of triangle
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                s = (a + b + c) / 2
                ar = math.sqrt(s * (s - a) * (s - b) * (s - c))

                # distance between point and convex hull
                d = (2 * ar) / a

                # apply cosine rule here
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

                # ignore angles > 90 and ignore points very close to convex hull(they generally come due to noise)
                if angle <= 90 and d > 30:
                    l += 1
                    cv2.circle(roi, far, 3, [255, 0, 0], -1)

                # draw lines around hand
                cv2.line(roi, start, end, [0, 255, 0], 2)

            l += 1

            # print corresponding gestures which are in their ranges
            font = cv2.FONT_HERSHEY_SIMPLEX
            if l == 1:
                if areacnt < 2000:
                    cv2.putText(frame, 'Put hand in the box', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                else:
                    if arearatio < 12:
                        cv2.putText(frame, '0', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

                    elif arearatio < 17.5:
                        cv2.putText(frame, 'Best of luck', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

                    else:
                        cv2.putText(frame, '1', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                        t=1
            elif l == 2:
                cv2.putText(frame, '2', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                t=2

            elif l == 3:

                if arearatio < 27:
                    cv2.putText(frame, '3', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                    t=3
                else:
                    cv2.putText(frame, 'ok', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

            else:
                cv2.putText(frame, 'reposition', (10, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                t=0

            # show the windows
            cv2.imshow('mask', mask)
            cv2.imshow('frame', frame)
        except:
            ret, frame = cap.read()
            if ret == True:

                # Display the resulting frame
                cv2.imshow('Frame', frame)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow("gray", gray)

                # Press Q on keyboard to  exit
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    if(t==1):
        square()
    elif(t==2):
        circle_plot()
    elif(t==3):
        road()
    else:
        print("hand gesture not valid")
        time.sleep(2)
        exit(1)

tkWindow = Tk()
tkWindow.configure(background="light blue")
tkWindow.geometry('200x100')
tkWindow.title('Login Form')
usernameLabel = Label(tkWindow, text="User Name",bg="light blue").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

passwordLabel = Label(tkWindow,text="Password",bg="light blue").grid(row=3, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=3, column=1)

validateLogin = partial(validateLogin, username, password)
loginButton = Button(tkWindow, text="Login", command=validateLogin,bg="yellow").grid(row=4, column=0)

tkWindow.mainloop()