"""
A console in beeware
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, LEFT, RIGHT, CENTER, ROW, Pack, TOP, BOTTOM


class Console(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        text = [[' ' for y in range(80)] for x in range(25)]
        main_box = toga.Box()
        main_box.style.update(direction=COLUMN, padding=0)
        self.word = toga.Label("\n".join("".join(x) for x in text))
        word_box = toga.Box()
        main_box.add(self.word)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Console()
