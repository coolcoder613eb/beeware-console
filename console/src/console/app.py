"""
A console in beeware
"""
import toga
import threading
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT, RIGHT, CENTER, ROW, Pack, TOP, BOTTOM


class Console(toga.App):
    def input(self,text=None):
        if text:
            self.word.text += text
        while not self.is_enter:
            pass
        self.is_enter = False
        rtn = self.text_input.value
        self.text_input.clear()
        return rtn
    def print(self,*args):
        self.word.text += ' '.join([str(x) for x in args]) + '\n'
    def ok(self,button):
        #print(self.text_input.value)
        self.is_enter = True

    def ch(self):
        self.word.text = 'Chometz Hunt' + '\n'
        print = self.print
        input = self.input
        #----------code-----------#
        place = 2
        numcol = ch1 = ch2 = ch3 = ch4 = ch5 = ch6 = ch7 = ch8 = ch9 = ch10 = found = 0
        savelist = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        def makesave():
            print(place, ' ', numcol, ' ', ch1, ' ', ch2, ' ', ch3, ' ', ch4, ' ', ch5, ' ', ch6, ' ', ch7, ' ', ch8,
                  ' ', ch9, ' ', ch10, ' ', found, '\n\n')

        def getsave():
            i = input('\nenter your savecode ')
            savelist = i.split()
            savelist[0] = int(savelist[0])
            savelist[1] = int(savelist[1])
            savelist[2] = int(savelist[2])
            savelist[3] = int(savelist[3])
            savelist[4] = int(savelist[4])
            savelist[5] = int(savelist[5])
            savelist[6] = int(savelist[6])
            savelist[7] = int(savelist[7])
            savelist[8] = int(savelist[8])
            savelist[9] = int(savelist[9])
            savelist[10] = int(savelist[10])
            savelist[11] = int(savelist[11])
            savelist[12] = int(savelist[12])
            place = savelist[0]
            numcol = savelist[1]
            ch1 = savelist[2]
            ch2 = savelist[3]
            ch3 = savelist[4]
            ch4 = savelist[5]
            ch5 = savelist[6]
            ch6 = savelist[7]
            ch7 = savelist[8]
            ch8 = savelist[9]
            ch9 = savelist[10]
            ch10 = savelist[11]
            found = savelist[12]

        while 1 == 1:
            if numcol == 10:
                if found == 0:
                    print('\n\nYOU FOUND ALL THE CHAMETZ!!!!\n\n')
                    found = 1
            if place == 2:
                i = input(
                    '\ntype "1" for the kitchen, type "2" for the dining room, \ntype "3" for the parents bedroom, type "4" for the kids bedroom.\nType "save" to save and "load" to load a savecode.')
                if i == '1':
                    place = 1
                if i == '2':
                    place = 3
                if i == '3':
                    place = 4
                if i == '4':
                    place = 5
                if i == 'save':
                    print('This number is your savecode.\n')
                    makesave()
                if i == 'load':
                    i = input('\nenter your savecode ')
                    savelist = i.split()
                    place, numcol, ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, found = int(savelist[0]), int(
                        savelist[1]), int(savelist[2]), int(savelist[3]), int(savelist[4]), int(savelist[5]), int(
                        savelist[6]), int(savelist[7]), int(savelist[8]), int(savelist[9]), int(savelist[10]), int(
                        savelist[11]), int(savelist[12])
            if place == 1:
                print('\nYou look around the kitchen.\nYou see 1.a cupboard 2.the oven and 3.the freezer')
                i = input('type "back" to go back or type "1", "2" or "3" to look more closely')
                if i == 'back':
                    place = 2
                if i == '1':
                    place = 11
                if i == '2':
                    place = 12
                if i == '3':
                    place = 13
            if place == 11:
                print('\nInside the cupboard you see \n1.a box of cornflakes and 2.a box of rice bubbles.')
                i = input('type "back" to go back or type "1" or "2" to look more closely')
                if i == '1':
                    print('\nYou look behind the cornflakes.')
                    place = 11
                if i == 'back':
                    place = 1
                if i == '2':
                    if ch1 == 0:
                        print('\nBehind the rice bubbles you see... \n1.a piece of bread in a plastic bag')
                        i = input('type "back" to go back or type "1" to look more closely')
                        ch1 = 1
                    else:
                        print('\nYou look behind the rice bubbles.')
                        place = 11
                    if i == '1':
                        numcol += 1
                        print('\nYou pick up the bread.\nYou have ', numcol, ' pieces of chametz')
                        place = 11
                    if i == 'back':
                        place = 11
            if place == 12:
                print('\nThe oven is very clean.')
                place = 1
            if place == 13:
                if ch2 == 0:
                    print(
                        '\nAs you open the freezer, \n1.a piece of bread in a plastic bag tumbles down from where it was hidden on the freezer door.')
                    i = input('type "back" to go back or type "1" to look more closely')
                    if i == '1':
                        numcol += 1
                        print('\nYou pick up the bread.\nYou have ', numcol, 'pieces of chametz.')
                        ch2 = 1
                        place = 1
                    if i == 'back':
                        place = 1
                else:
                    print('\nYou open the freezer')
                    place = 1
            if place == 3:
                print('\nYou look around the dining room. \nYou see 1.the table, 2.the couch and 3.a bookshelf.')
                i = input('type "back" to go back or type "1", "2" or "3" to look more closely')
                if i == 'back':
                    place = 2
                if i == '1':
                    place = 31
                if i == '2':
                    place = 32
                if i == '3':
                    place = 33
            if place == 31:
                print('\nThe table is empty.')
                place = 3
            if place == 32:
                if ch3 == 0:
                    print('\nAs you look behind the couch cushions, you see...\n1.a piece of bread in a plastic bag')
                    i = input('type "back" to go back or type "1" to look more closely')
                    if i == '1':
                        numcol += 1
                        print('\nYou pick up the bread.\nYou have ', numcol, 'pieces of chametz.')
                        ch3 = 1
                        place = 3
                    if i == 'back':
                        place = 3
                else:
                    print('\nYou look behind the couch cushions.')
                    place = 3
            if place == 33:
                if ch4 == 0:
                    print('\nAs you look behind the books, you see...\n1.a piece of bread in a plastic bag')
                    i = input('type "back" to go back or type "1" to look more closely')
                    if i == '1':
                        numcol += 1
                        print('\nYou pick up the bread.\nYou have ', numcol, 'pieces of chametz.')
                        ch4 = 1
                        place = 3
                    if i == 'back':
                        place = 3
                else:
                    print('\nYou look behind the books.')
                    place = 3
            if place == 4:
                print(
                    '\nAs you look around the bedroom you see \n1.a queen bed and 2.a king bed with \n3.a bedside table between them.')
                i = input('type "back" to go back or type "1", "2" or "3" to look more closely')
                if i == 'back':
                    place = 2
                if i == '1':
                    place = 41
                if i == '2':
                    place = 42
                if i == '3':
                    place = 43
            if place == 41:
                if ch5 == 0:
                    print(
                        '\nYou look under the blanket. \nAs you look under the pillow you see \n1.a piece of bread in a plastic bag.')
                    i = input('type "back" to go back or type "1" to look more closely')
                    if i == '1':
                        numcol += 1
                        print('\nYou pick up the bread.\nYou have ', numcol, 'pieces of chametz.')
                        ch5 = 1
                        place = 4
                    if i == 'back':
                        place = 4
                else:
                    print('\nYou look under the blanket and pillow.')
                    place = 4
            if place == 42:
                if ch6 == 0:
                    print(
                        '\nAs you look under the blanket and pillow, you see \n1.a piece of bread in a plastic bag \nbetween the headboard and the mattress.')
                    i = input('type "back" to go back or type "1" to look more closely')
                    if i == '1':
                        numcol += 1
                        print('\nYou pick up the bread.\nYou have ', numcol, 'pieces of chametz.')
                        ch6 = 1
                        place = 4
                    if i == 'back':
                        place = 4
                else:
                    print('\nYou look under the blanket and pillow.')
                    place = 4
            if place == 43:
                print('\nAs you look at the bedside table you see \n1.a lamp and 2.a drawer.')
                i = input('type "back" to go back or type "1" or "2" to look more closely')
                if i == '1':
                    if ch7 == 0:
                        print(
                            '\nAs you move the lamp you see \n1.the piece of bread in a plastic bag that was hidden under it.')
                        i = input('type "back" to go back or type "1" to look more closely')
                        if i == '1':
                            numcol += 1
                            print('\nYou pick up the bread.\nYou have ', numcol, 'pieces of chametz.')
                            ch7 = 1
                        place = 43
                        if i == 'back':
                            place = 43
                    else:
                        print('\nYou move the lamp.')
                        place = 43
                if i == 'back':
                    place = 4
                if i == '2':

                    if ch8 == 0:
                        print(
                            '\nAs you open the drawer you see \n1.the piece of bread in a plastic bag that was hidden inside it.')
                        i = input('type "back" to go back or type "1" to look more closely')
                        if i == '1':
                            numcol += 1
                            print('\nYou pick up the bread.\nYou have ', numcol, 'pieces of chametz.')
                            ch8 = 1
                        place = 43
                        if i == 'back':
                            place = 43
                    else:
                        print('\nYou open the drawer.')
                        place = 43
            if place == 5:
                print('\nAs you look around the bedroom \nyou see 1.a pink bunkbed and 2.a blue bunkbed.')
                i = input('type "back" to go back or type "1" or "2" to look more closely')
                if i == 'back':
                    place = 2
                if i == '1':
                    place = 51
                if i == '2':
                    place = 52
            if place == 51:
                if ch9 == 0:
                    print(
                        '\nAs you look under the bed you see \n1.a piece of bread in a plastic bag that was hidden there.')
                    i = input('type "back" to go back or type "1" to look more closely')
                    if i == '1':
                        numcol += 1
                        print('\nYou pick up the bread.\nYou have ', numcol, 'pieces of chametz.')
                        ch9 = 1
                        place = 5
                    if i == 'back':
                        place = 5
                else:
                    print('\nYou look under the bed.')
                    place = 5
            if place == 52:
                print('\nAs you look under the bed you see \na black left shoe and 1.a shoebox.')
                i = input('type "back" to go back or type "1" to look more closely')
                if i == '1':
                    if ch10 == 0:
                        print(
                            '\nAs you look inside the shoebox you see a black right shoe and 1.a piece of bread in a plastic bag.')
                        i = input('type "back" to go back or type "1" to look more closely')
                        if i == '1':
                            numcol += 1
                            print('\nYou pick up the bread.\nYou have ', numcol, 'pieces of chametz.')
                            ch10 = 1
                            place = 52
                        if i == 'back':
                            place = 52
                    else:
                        print('\nAs you look inside the shoebox you see a black right shoe.')
                        place = 52
                if i == 'back':
                    place = 5

        #--------end code---------#

    def startch(self,button):
        ch_thread = threading.Thread(target=self.ch, daemon=True)
        ch_thread.start()

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.is_enter = False
        self.text = 'Mobile Console\n'#(('█'*80)+'\n')*25
        self.main_box = toga.Box()
        self.main_box.style.update(direction=COLUMN, padding=0)
        self.word = toga.Label(self.text)
        self.word_box = toga.Box()
        self.word_box.style.update(direction=ROW, padding=0)
        self.main_box.add(self.word)
        self.main_box.add(self.word_box)
        self.text_input = toga.TextInput()
        self.ok_button = toga.Button('Ok',on_press=self.ok)
        self.word_box.add(self.text_input)
        self.word_box.add(self.ok_button)
        self.ch_button = toga.Button('Chometz Hunt', on_press=self.startch)
        self.main_box.add(self.ch_button)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()


def main():
    return Console()
