import re
from colorama import Fore, Style, Back
import builtins


class SetPattern:
    def __init__(self, pattern, color=None, back=None, style=None, underline=False):
        self.pattern = re.compile(pattern)
        self.color = color if color is not None else Fore.RESET
        self.back = back if back is not None else Back.RESET
        self.style = style if style is not None else Style.RESET_ALL
        self.underline = underline

    def colorize_text(self, text):
        if self.underline:
            return self.pattern.sub(lambda match: f"{self.style}{self.color}{self.back}\033[4m{match.group()}\033[0m{Style.RESET_ALL}", text)
        else:
            return self.pattern.sub(lambda match: f"{self.style}{self.color}{self.back}{match.group()}{Style.RESET_ALL}", text)


# Función que inicializa el coloreado
def start_color(patterns):
    def custom_print(*args, **kwargs):
        # Convertir los argumentos de print a una cadena
        text = " ".join(map(str, args))
        
        # Aplicar el coloreado
        for pattern in patterns:
            text = pattern.colorize_text(text)

        # Imprimir el texto coloreado
        original_print(text, **kwargs)

    # Remplazar la función print por nuestra versión personalizada
    original_print = builtins.print
    builtins.print = custom_print
