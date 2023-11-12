import re
from colorama import Fore, Style, Back
import builtins

class SetPattern:
    def __init__(self, pattern, color=None, back=None, style=None, underline=False, strikethrough=False):
        # Compile the regular expression pattern
        self.pattern = re.compile(pattern)
        # Set default values for color, background, style, and underline
        self.color = color if color is not None else Fore.RESET
        self.back = back if back is not None else Back.RESET
        self.style = style if style is not None else Style.RESET_ALL
        self.underline = underline
        self.strikethrough = strikethrough

    def colorize_text(self, text, stop=None):
        # Apply color, background, style, underline, and strikethrough to matched text
        if self.underline and self.strikethrough:
            return self.pattern.sub(lambda match: f"{self.style}{self.color}{self.back}\033[4m\033[9m{match.group()}\033[0m{Style.RESET_ALL}", text)
        elif self.underline:
            return self.pattern.sub(lambda match: f"{self.style}{self.color}{self.back}\033[4m{match.group()}\033[0m{Style.RESET_ALL}", text)
        elif self.strikethrough:
            return self.pattern.sub(lambda match: f"{self.style}{self.color}{self.back}\033[9m{match.group()}\033[0m{Style.RESET_ALL}", text)
        else:
            return self.pattern.sub(lambda match: f"{self.style}{self.color}{self.back}{match.group()}{Style.RESET_ALL}", text)


# Function to initialize colorization
def start_color(patterns):
    def custom_print(*args, **kwargs):
        # Convert print arguments to a string
        text = " ".join(map(str, args))

        # Apply colorization to the text
        for pattern in patterns:
            text = pattern.colorize_text(text)

        # Print the colorized text
        original_print(text, **kwargs)

    # Replace the print function with the custom version
    original_print = builtins.print
    builtins.print = custom_print

    return original_print  # Return the original print function


# Function to end colorization and restore the original print function
def end_color():
    # Restore the original print function
    builtins.print = builtins.__original_print__

# Save the original print function
builtins.__original_print__ = builtins.print
