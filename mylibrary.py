""" this is my personnal library with useful functions
    - bar -> progress bar
    - string -> string manipulation
"""

# --- progress bar ---

from time import time as now
import curses

class bar:

    """progress bar"""

    def __init__(self, steps: int, text: str = "", pattern_bar: str = "█", pattern_space: str = " ", lenght: int = 10, show_time: bool = True) -> None:
        """initialize the progress bar

        Args:
            steps (int): number of steps
            text (str): message to show in the progress bar
            pattern_bar (str): pattern of the progress bar
            pattern_space (str): pattern of the space
            lenght (int): lenght of the progress bar
        """

        self.steps = steps
        self.text = text
        self.pattern_bar = pattern_bar
        self.pattern_space = pattern_space
        self.lenght = lenght
        self.current = 0
        self.time = now()
        self.init = now()
        self.total = 0
        self.mean = 0
        self.show_time = show_time

        self.console = curses.initscr()


    def next(self):
        """increment the progress bar"""

        self.current += 1
        self.mean += now() - self.time
        self.time = now()
        self.total = self.mean / self.current * self.steps
        
        self.console.addstr(0, 0, f"{self.text} |{self.pattern_bar * (self.current * self.lenght // self.steps)}{self.pattern_space * (self.lenght - (self.current * self.lenght // self.steps))}| {self.current * 100 // self.steps}% {f'[{self.__str_round(self.time - self.init)} s / {self.__str_round(self.total)} s]' if self.show_time else ''}")
        self.console.refresh()
        
        if self.current == self.steps:
            curses.endwin()
        
    
    def __str_round(self, num: int) -> str:
        """round a number to 2 decimal"""
        
        tmp = str(round(num, 2)).split(".")
        avant = tmp[0]
        apres = tmp[1]

        avant = "0" * (3 - len(avant)) + avant
        apres += "0" * (3 - len(apres))

        return avant + "." + apres



# --- replace characters in a string ---
class string:

    def replace(string: str, index: int, char: str) -> str:
        """replace a character in a string with index

        Args:
            string (str): the string to modify
            index (int): the index of the character to replace
            char (str): the character to replace

        Returns:
            str: the modified string
        """
        return string[:index] + char + string[index + 1:]

    
    def replaces(string, *args) -> str:
        """multiple replaces in a string
        ---
        
        *args need to be per pair\n
        example:\n
        a = "Hello World"\n
        a = string.replaces(a, "Hello", "Hi", "World", "Earth")\n
        print(a) -> "Hi Earth"\n
        


        Args:
            string (str): the string to modify
            *args (str): pair of characters to replace

        Returns:
            str: the modified string
        """
        for i in range(0, len(args), 2):
            string = string.replace(args[i], args[i + 1])
        return string

# --- 
