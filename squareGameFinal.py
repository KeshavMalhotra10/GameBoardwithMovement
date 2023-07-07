import tkinter as tk
import random

#####################################
# Global Variables
#####################################
button_height = 50
window_height = 850 - button_height
window_width = 850
player1_x = 750
player1_y = 700
player2_x = 770
player2_y = 700

#####################################
# Function Declaration
#####################################
endCounter = 0
endCounter2 = 0

def randomDiceButton():
    # Rolls a random number for the user to move
    global root
    global ranNum
    global endCounter
    ranNum = random.randint(1, 6)  # Generate random number
    popUp = tk.Toplevel(root)  # Making a pop-up occur when btn is pressed
    popUp.geometry("600x200")  # Pop-up canvas
    popUp.title("Number Rolled:")  # Title
    tk.Label(popUp, text="You rolled a " + str(ranNum), font=("Arial 18 bold")).place(x=150, y=80)  # Text and placement of the popup
    global player1_x
    global player1_y

    player1_x -= 85 * ranNum  # Update player1_x by multiplying ranNum with 85
    labelImage1.place(x=player1_x, y=player1_y)  # Update the player1 image position

    if player1_x < -25:  # If the piece leaves the canvas board, then go back up
        endCounter += 1
        player1_x = 750 + player1_x + 108 - (0.6 * endCounter)
        player1_y = 700 - endCounter * 85 + (15 * 0.2 * endCounter)
        labelImage1.place(x=player1_x, y=player1_y)
    
    # Check for teleportation from square 4 to square 14
    if player1_x == 480 and player1_y == 600:
        player1_x = 770
        player1_y = 500
        labelImage1.place(x=player1_x, y=player1_y)
    
    if player1_x > 725:
         print("Congratulations player1, you have reached square 100 first!")


def randomDiceButton2():
    # Rolls a random number for the user to move
    global root
    global ranNum
    global endCounter2
    ranNum = random.randint(1, 6)  # Generate random number
    popUp = tk.Toplevel(root)  # Making a pop-up occur when btn is pressed
    popUp.geometry("600x200")  # Pop-up canvas
    popUp.title("Number Rolled:")  # Title
    tk.Label(popUp, text="You rolled a " + str(ranNum), font=("Arial 18 bold")).place(x=150, y=80)  # Text and placement of the popup
    global player2_x
    global player2_y
    player2_x -= 85 * ranNum  # Update player1_x by multiplying ranNum with 85
    labelImage2.place(x=player2_x, y=player2_y)  # Update the player1 image position

    if player2_x < -25:  # If the piece leaves the canvas board, then go back up
        endCounter2 += 1
        player2_x = 750 + player2_x + 108 - (0.6 * endCounter2)
        player2_y = 700 - endCounter2 * 85 + (15 * 0.4 * endCounter2)
        labelImage2.place(x=player2_x, y=player2_y)

    if player2_x > 725:
         print("Congratulations player2, you have reached square 100 first!")


def setup():
    global root
    root = tk.Tk()
    root.title("Snakes & Ladders Keshav")
    root.geometry("850x850")
    myCanvas = tk.Canvas(
        root,
        bg="white",
        height=window_height,
        width=window_width)

    return root, myCanvas


def makeSquares(canvas):
    # Create 100 squares
    counter = 0
    colorList = ["#9381FF", "#B8B8FF", "#F8F7FF", "#FFEEDD"]

    for row in range(10):
        for column in range(10):

            # create coordinates
            x1 = 0 + (window_width / 10) * column
            x2 = x1 + (window_width / 10)
            y1 = button_height + 15 + (window_height / 10) * row
            y2 = y1 + (window_height / 10)

            # update counter
            counter += 1

            canvas.create_rectangle(
                x1,
                y1 - 90,
                x2,
                y2 - 90,
                outline="black",
                fill=colorList[counter % 4],
                width=2)


def makeLabels():
    # go through each square
    # Number through in reverse(100 TOWARDS 1)
    counter = 101

    for row in range(10):
        for column in range(10):

            # create coordinates
            x1 = 0 + (window_width / 10) * column
            x2 = x1 + (window_width / 10)
            y1 = button_height - 90 + (window_height / 10) * row
            y2 = y1 + (window_height / 10)

            # update counter
            counter -= 1

            tk.Label(
                root,
                text=counter,
                font=("Arial 18 bold")
            ).place(x=(x1 + x2) / 2, y=(y1 + y2) / 2)


#####################################
# Function Calls
#####################################

root, myCanvas = setup()

rollBtn = tk.Button(root, text="PLAYER 1 ROLL! ", command=randomDiceButton)  # Links button to function
rollBtn.place(x=450, y=760)

rollBtn2 = tk.Button(root, text="PlAYER 2 ROLL!", command=randomDiceButton2)  # Links button to function
rollBtn2.place(x=300, y=760)

# Making player images
photo_image1 = tk.PhotoImage(file="/Users/keshavmalhotra/Desktop/Players/player1.png")
labelImage1 = tk.Label(root, image=photo_image1, bd=0, relief='flat', highlightthickness=0, bg=root['bg'])
labelImage1.place(x=player1_x, y=player1_y)

photo_image2 = tk.PhotoImage(file="/Users/keshavmalhotra/Desktop/Players/player2.png")
labelImage2 = tk.Label(root, image=photo_image2, bd=0, relief='flat', highlightthickness=0, bg=root['bg'])
labelImage2.place(x=player2_x, y=player2_y)

makeSquares(myCanvas)
makeLabels()
myCanvas.pack()
root.mainloop()
