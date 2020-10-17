from graphics import *

def getInputs():
    
    prefferedSize = [5,7,9,11]
    
    while True:
        try:
            patchWorkSize = int(input("Please enter the prefferred patchwork size 5,7,9 or 11: "))
            if patchWorkSize not in prefferedSize:
                print("Please enter a valid size!")
                continue
        except ValueError:
            print("Your input is invalid, Please enter a valid number.")
            continue
        else:
            break

    listOfColours = ["red","green","blue","magenta","cyan","orange","brown","pink"]       
    coloursUsed = []
    while len(coloursUsed) < 3:
        colour = input("Please enter a colour: ")        
        if validateColours(listOfColours, coloursUsed,colour):
            coloursUsed.append(colour)
        
    return patchWorkSize, coloursUsed
    
    
def validateColours(listOfColours, coloursUsed,colour):
    if colour in listOfColours and colour not in coloursUsed:
        return True
    elif colour not in listOfColours:
        print("Not a colour or invalid. Please try again\nPlease enter a different colour")
        return False
    elif colour in coloursUsed:
        print("Colour has already been used, Please use a different colour")
        return False
    
def fifthDigit(win,x,y,colour):
        
    x1 = 0
    for i in range(4):
        
        rectangleLeft = Rectangle(Point(x + x1,90-x1 + y),Point(x + x1 + 10,x1 + y))
        rectangleLeft.draw(win)
        rectangleLeft.setFill(colour)
        
        rectangleTop = Rectangle(Point(x + 100 - x1 ,x1 +10 + y),Point(x + x1 +10,x1 + y))
        rectangleTop.draw(win)
        rectangleTop.setFill(colour)
        
        rectangleRight = Rectangle(Point(x + 100 - x1,100 - x1 + y),Point(x +90 - x1,x1 + 10 + y))
        rectangleRight.draw(win)
        rectangleRight.setFill(colour)
        
        rectangleBottom = Rectangle(Point(x + x1,90 - x1 + y),Point(x + 90 - x1,100 - x1 + y))
        rectangleBottom.draw(win)
        rectangleBottom.setFill(colour)
        x1 = x1 + 10
        #y1 = y1 + 10
        
    
def lastDigit(win,x,y,colour):
    y1 = 95 + y
    a = 5
    for i in range(10):
        circle = Circle(Point(50+x,y1),a)
        circle.setOutline(colour)
        circle.draw(win)
        y1 = y1 - 5
        a = a + 5
        
def main():
    size,colours = getInputs()
    win = GraphWin("Patchwork Sampler",100 * size,size * 100)
    count = 0
    for y in range(0,size * 100,100): 
        for x in range(0,size * 100,100):
            if y == 0 or x <= 100 :
                lastDigit(win,x,y,colours[count%3])
            else:
                fifthDigit(win,x,y,colours[count%3])
            count = count + 1
    
