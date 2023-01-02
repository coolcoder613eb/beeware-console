"""
A console in beeware
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT, RIGHT, CENTER, ROW, Pack, TOP, BOTTOM


class Console(toga.App):
    def ok(self,button):
        print(self.input.value)
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        self.text = ''#(('█'*80)+'\n')*25
        self.main_box = toga.Box()
        self.main_box.style.update(direction=COLUMN, padding=0)
        self.word = toga.Label("\n".join("".join(x) for x in self.text))
        self.word_box = toga.Box()
        self.main_box.style.update(direction=ROW, padding=0)
        self.main_box.add(self.word)
        self.main_box.add(self.word_box)
        self.input = toga.TextInput()
        self.word_box.add(self.input)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()


def main():
    return Console()
