# Name: Janae Dorsey
# File: vigenere.py
#
# Purpose: This program will implement the Vigenere cipher by using an inputted keyword to encode an inputted message.

# Certification of Authenticity:
# I certify that this lab is entirely my own work.

from graphics import *
from time import sleep

#Function for entire program
def main():

    width = 500
    height = 500

    anchor_pt = Point(width/2, height-10)

    #draws grapic window
    win = GraphWin("Vigenere", width, height)

    #draws input messages
    msg_text = Text(Point(150, height - 400), "Message to code: ")
    kw_text = Text(Point(140, height - 350), "Enter keyword: ")

    msg_text.draw(win)
    kw_text.draw(win)

    #draws text(input) boxes
    msg = Entry(Point(350, height - 400), 25)
    kw = Entry(Point(284, height - 350), 10)
    msg.draw(win)
    kw.draw(win)

    #draws encode button
    button_text = Text(Point(width / 2, height / 2), "Encode")
    button_outline = Rectangle(Point(210, 220), Point(290, 280))
    button_text.draw(win)
    button_outline.draw(win)

    #gets text from text(input) boxes
    win.getMouse()
    message = msg.getText()
    keyword = kw.getText()

    #undraws encode button
    button_text.undraw()
    button_outline.undraw()

    #function for encoding message
    def encode(message, keyword):

        msg_ns = message.replace(" ", "")
        msg_cap = msg_ns.upper()
        keyword_cap = keyword.upper()
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        keyword_dict = []
        msg_dict = []
        cipher_text = ""

        #finds index of characters in message in alphabet
        for ch in msg_cap:
            msg_cap_pos = alphabet.find(ch)
            msg_dict.append(msg_cap_pos)

        #finds index of characters in key in alphabet
        for letter in keyword_cap:
            keyword_cap_pos = alphabet.find(letter)
            keyword_dict.append(keyword_cap_pos)

        #adds a key index to every message index in a circular fashion
        for i in range(len(msg_dict)):
            value = (msg_dict[i] + keyword_dict[i % len(keyword)]) % 26
            cipher_text += alphabet[value % len(alphabet)]
        return cipher_text

    #draws "resulting message"
    results_text = Text(Point(width / 2, 250), "Resulting Message:")
    results_text.draw(win)

    #draws encoded message
    results = Text(Point(width / 2, 275), encode(message, keyword))
    results.draw(win)

    #draws exit instructions
    sleep(1)
    close_text = Text(anchor_pt, "Click anywhere to close window.")
    close_text.draw(win)

    #closes window
    win.getMouse()
    win.close()

main()