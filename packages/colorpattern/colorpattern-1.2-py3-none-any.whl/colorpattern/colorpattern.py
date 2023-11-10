"""
This file is (or part of) COLORPATTERN v1.2
Copyright 2023- Croketillo <croketillo@gmail.com> https://github.com/croketillo

DESCIPTION:
COLORPATTERN - Effortless console text colorization based on user-defined patterns 
in Python.

                        LICENSE -   GNU GPL-3

This software is protected by the GNU General Public License version 3 (GNU GPL-3).
You are free to use, modify, and redistribute this software in accordance with the
terms of the GNU GPL-3. You can find a copy of the license at the following link:
https://www.gnu.org/licenses/gpl-3.0.html.

This software is provided as-is, without any warranties, whether express or implied.
Under no circumstances shall the authors or copyright holders be liable for any claims,
damages, or liabilities arising in connection with the use of this software.
If you make modifications to this software and redistribute it, you must comply with
the terms of the GNU GPL-3, which includes the obligation to provide the source code
for your modifications. Additionally, any derived software must also be under the
GNU GPL-3.

For more information about the GNU GPL-3 and its terms, please carefully read the full
license or visit https://www.gnu.org/licenses/gpl-3.0.html


"""

import re
from colorama import Fore, Style, Back
import builtins

class SetPattern:
    def __init__(self, pattern, color=None, back=None, style=None, underline=False):
        # Compile the regular expression pattern
        self.pattern = re.compile(pattern)
        # Set default values for color, background, style, and underline
        self.color = color if color is not None else Fore.RESET
        self.back = back if back is not None else Back.RESET
        self.style = style if style is not None else Style.RESET_ALL
        self.underline = underline

    def colorize_text(self, text):
        # Apply color, background, style, and underline to matched text
        if self.underline:
            return self.pattern.sub(lambda match: f"{self.style}{self.color}{self.back}\033[4m{match.group()}\033[0m{Style.RESET_ALL}", text)
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
