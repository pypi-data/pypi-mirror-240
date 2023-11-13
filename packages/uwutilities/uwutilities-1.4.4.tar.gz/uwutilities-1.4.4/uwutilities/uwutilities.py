# --- progress bar ---
from time import time as now
from datetime import timedelta
import curses


class Bar:
    """progress bar"""

    def __init__(self, steps: int, text: str = "", pattern_bar: str = "█", pattern_space: str = " ", lenght: int = 25,
                 show_steps: bool = True, show_time: bool = False, show_time_left: bool = True) -> None:
        """initialize the progress bar

        Args:
            steps (int): number of steps
            text (str): message to show in the progress bar
            pattern_bar (str): pattern of the progress bar
            pattern_space (str): pattern of the space
            lenght (int): lenght of the progress bar
        """
        self._steps = steps
        self._text = text

        self._current = 0
        self._time = now()
        self._init = now()
        self._total = 0
        self._mean = 0

        self._show_time = show_time
        self._show_steps = show_steps
        self._show_time_left = show_time_left
        self._pattern_bar = pattern_bar
        self._pattern_space = pattern_space
        self._lenght = lenght

        self._console = curses.initscr()
        self._console.clear()

    def next(self):
        """increment the progress bar"""

        self._current += 1
        self._mean += now() - self._time
        self._time = now()
        self._total = self._mean / self._current * self._steps

        self._console.addstr(0, 0,
                            f"{self._text} | {self._pattern_bar * (self._current * self._lenght // self._steps)}{self._pattern_space * (self._lenght - (self._current * self._lenght // self._steps))}| {self._current * 100 // self._steps}%{' [' if self._show_time or self._show_steps else ''}{f' steps:  {self._current} / {self._steps} ' if self._show_steps else ''}{'|' if self._show_time and self._show_steps else ''}{f' time: {str(timedelta(seconds=self._time - self._init))[:-7]} / {str(timedelta(seconds=self._total))[:-7]} ' if self._show_time else ''}{f'| finished in: {str(timedelta(seconds=self._total - (self._time - self._init)))[:-7]} ' if self._show_time_left else ''}{']' if self._show_time or self._show_steps or self._show_time_left else ''}")
        self._console.refresh()

        if self._current == self._steps:
            curses.endwin()

    def __str_round(self, num: int) -> str:
        """round a number to 2 decimal"""

        tmp = str(round(num, 2)).split(".")
        avant = tmp[0]
        apres = tmp[1]

        avant = "0" * (3 - len(avant)) + avant
        apres += "0" * (3 - len(apres))

        return f"{avant}.{apres}"

    def stop(self):
        """stop the progress bar"""

        curses.endwin()


# --- replace characters in a string ---
class String_tools:

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

class Import:

    def __init__(self, file: str):
        self.file = file
        self.dictionary = {}

    def get_all(self):
        vari = {}
        lines = open(self.file, "r").readlines()

        if len(lines) == 1:
            return

        for line in lines:
            if line == "" or line == "\n":
                continue

            line = line.split("=")
            line[0], line[1] = line[0].strip(), line[1].strip()

            if line[0] in vari:
                raise Exception(f"{line[0]} est plusieurs fois dans le fichier")
            
            
            vari[line[0]] = line[1][:-1] if line[1].endswith("\n") else line[1]
 
        self.dictionary = vari


    def save_all(self):
        string = ""
        for key, value in self.dictionary.items():
            string += f"{key}={value}\n"
        
        open(self.file, "w").write(string)


    def save(self, *variables: str):
        lines = open(self.file, "r").readlines()

        variables_of_lines = []
        for line in lines:
            if line.strip() != "" or line != "\n":
                variables_of_lines.append(line.split("=")[0].strip())

        for variable in variables:

            if variable not in variables_of_lines:
                lines.append(f"{variable}={self.dictionary[variable]}")

            else:
                for i in range(len(lines)):
                    if lines[i].startswith(variables):
                        lines[i] = f"{variable}={self.dictionary[variable]}"

        line = [line for line in lines if line != [] and line != []]        
        open(self.file, "w").writelines(line)
