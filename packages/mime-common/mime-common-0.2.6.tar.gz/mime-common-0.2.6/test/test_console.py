import logging
import unittest
import io
import sys
import pytest

sys.path.append("../src")
sys.path.append("src")
from console import Console, color_numbers

class ConsoleTest(unittest.TestCase):
    TEST_MESSAGE = 'TEST MESSAGE'
    def test_error_nocolor(self):
        capture_output = io.StringIO()
        cons = Console(use_colors=False) 
        cons.set_colors(False)    
        cons.set_logglevel(logging.DEBUG)   
        sys.stdout = capture_output
        cons.error(self.TEST_MESSAGE)
        sys.stdout = sys.__stdout__
        print(f"Error NOcolor - Compare to: {capture_output.getvalue()}")
        assert f"{self.TEST_MESSAGE}\n" == capture_output.getvalue()

    def test_error_color(self):
        capture_output = io.StringIO()
        cons = Console(use_colors=True)        
        cons.set_colors(True)    
        cons.set_logglevel(logging.DEBUG)   
        sys.stdout = capture_output
        cons.error(self.TEST_MESSAGE)
        sys.stdout = sys.__stdout__
        print(f"Error color - Compare to: {capture_output.getvalue()}")
        assert f"\x1b[1;31m{self.TEST_MESSAGE}\x1b[0m\n" == capture_output.getvalue()

    def test_critical_color(self):
        capture_output = io.StringIO()
        cons = Console(use_colors=True)        
        cons.set_colors(True)    
        cons.set_logglevel(logging.DEBUG)   
        sys.stdout = capture_output
        cons.critical(self.TEST_MESSAGE)
        sys.stdout = sys.__stdout__
        print(f"Critical color - Compare to: {capture_output.getvalue()}")
        assert f"\x1b[1;37;41m{self.TEST_MESSAGE}\x1b[0m\n" == capture_output.getvalue()

    def test_print(self) -> None:
        capture_output = io.StringIO()
        cons = Console(use_colors=False)
        cons.set_colors(False)    
        cons.set_logglevel(logging.DEBUG)   
        sys.stdout = capture_output
        cons.print(self.TEST_MESSAGE)
        sys.stdout = sys.__stdout__
        print(f"Print - Compare to: {capture_output.getvalue()}")
        assert f"{self.TEST_MESSAGE}\n" == capture_output.getvalue()

    def test_logglevel(self) -> None:
        capture_output = io.StringIO()
        cons = Console(use_colors=False)
        cons.set_colors(False)    
        cons.set_logglevel(logging.DEBUG)
        debg: bool = logging.DEBUG == cons.get_logglevel()
        cons.set_logglevel(logging.INFO)
        info: bool = logging.INFO == cons.get_logglevel()
        cons.set_logglevel(logging.WARNING)
        warn: bool = logging.WARNING == cons.get_logglevel()
        cons.set_logglevel(logging.ERROR)
        erro: bool = logging.ERROR == cons.get_logglevel()
        cons.set_logglevel(logging.CRITICAL)
        crit: bool = logging.CRITICAL == cons.get_logglevel()
        assert debg and info and warn and erro and crit    
    
    def test_all_colors_dummy(self):
        cons = Console(use_colors=True)
        cons.set_colors(True)    
        cons.set_logglevel(logging.DEBUG)   
        cons.red("red")
        cons.black_on_red("black")
        cons.yellow("yellow")
        cons.green("green")
        cons.blue("blue")
        cons.print(f"{self.TEST_MESSAGE}", underline=True)
        assert True

    def test_rest_dummy(self):
        cons = Console()
        cons.set_colors(False)    
        cons.set_logglevel(logging.DEBUG)   
        cons.debug("debug")
        cons.info("info")
        cons.warning("warning")
        assert True

    def test_destructor(self) -> None:
        cons:Console = Console(use_colors=False)
        cons.set_colors(False)    
        cons.set_logglevel(logging.DEBUG)
        del cons
        cons_exist: bool = not ("cons" in locals() or "cons" in globals())
        assert cons_exist


class color_numbersTest(unittest.TestCase):
     def test_some_values(self):
        if color_numbers.RESET == 0 and \
            color_numbers.BOLD == 1 and \
            color_numbers.UNDERLINE == 4 and \
            color_numbers.BLACK == 30 and \
            color_numbers.RED == 31 and \
            color_numbers.GREEN == 32 and \
            color_numbers.YELLOW == 33 and \
            color_numbers.BLUE == 34 and \
            color_numbers.MAGENTA == 35  and \
            color_numbers.CYAN == 36 and \
            color_numbers.WHITE == 37 and \
            color_numbers.BGBLACK == 40 and \
            color_numbers.BGRED == 41 and \
            color_numbers.BGGREEN == 42 and \
            color_numbers.BGYELLOW == 43 and \
            color_numbers.BGBLUE == 44 and \
            color_numbers.BGMAGENTA == 45  and \
            color_numbers.BGCYAN == 46 and \
            color_numbers.BGWHITE == 47:
            assert True

if __name__=='__main__':
	unittest.main()     # pragma: no cover

