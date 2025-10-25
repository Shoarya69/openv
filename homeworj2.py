import cv2
import os

def rect(image):
    print("I am Rectangel function\n")
    h,w,c = image.shape
    print(f"Image size is h={h},w={w}\n")
    print("Give me points of digonal to draw an rectange\n ")
    x1 = int(input("X1 point = "))
    y1 = int(input("Y2 point = "))
    x2 = int(input("X2 point = "))
    y2 = int(input("Y2 point = "))
    rec = cv2.rectangle(image,(x1,y1),(x2,y2),(255,0,0),4)
    cv2.imwrite("rec.jpg",rec)

def cir(image):
    print("I am Circle Function\n")
    h,w,c = image.shape
    print(f"Image size is h={h},w={w}\n")
    print("Give me points of circle to draw an circle with radius\n")
    x1 = int(input("X1 = "))
    y1 = int(input("Y2 = "))
    r = int(input("Radius = "))
    cir = cv2.circle(image,(x1,y1),r,(225,0,0),4)
    cv2.imwrite("cir.jpg",cir)

def line(image):
    print("I am line Function \n")
    h,w,c = image.shape
    print(f"Image size is h={h},w={w}\n")
    print("Give me points of line to draw an line\n")
    x1 = int(input("X1 point = "))
    y1 = int(input("Y2 point = "))
    x2 = int(input("X2 point = "))
    y2 = int(input("Y2 point = "))
    lin = cv2.line(image,(x1,y1),(x2,y2),(255,0,0),4)
    cv2.imwrite("line.jpg",lin)

def text(image):
    print("I am Text add Function \n")
    h,w,c = image.shape
    print(f"Image size is h={h},w={w}\n")
    print("Give me points of line write text\n")
    x1 = int(input("X1 point = "))
    y1 = int(input("Y2 point = "))
    t = input("Enter your text = ")
    tex = cv2.putText(image,t,(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    cv2.imwrite("tex.jpg",tex)

def fun(image,l):
    match l:
        case 1:
            print("This is for creating rectangle on current image ")
            rect(image)
        case 2:
            print("This is for creating circle on current image ")
            cir(image)
        case 3:
            print("This is for creating line on current image  ")
            line(image)
        case 4:
            print("This is for creating text on current image  ")
            text(image)
        case _:
            print("Somthing Went wrong ,Sorrry for inconvinition")
            return
def imgop(image):
    if image is None:
        print("Somthing went Wrong plese try again later")
    else:
        print("Success fully loaded")
        print("Which operation You Want to perform:- \n")
        print("1. for Rectangele\t2. for circle\t3. for line\t4. for add text\tany other key for exit\n")
        try:
            l = int(input("Enter your inpur here:- "))
            if(l<5):
                print("We are processng further :- \n")
                fun(image,l)
            else:
                print("Exiting the code")
                return
        except:
            print("Exiting the code")
            exit()

base_dir = os.path.dirname(os.path.abspath(__file__))

files = [f for f in os.listdir(base_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
file = []

print("Those are the files in current dir:- \n")

i=1

for f in files:
    print(f"{i} {f}")
    i = i+1
    file.append(f)

try:
    cho = int(input("Which file you want to open for your photo editing (enter the Number):- "))
except Exception as e:
    print(e)
    exit()

if(cho<i):
    image = cv2.imread(file[cho-1])
    imgop(image)
else:
    print("There is no such type of file")




