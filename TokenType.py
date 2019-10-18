from enum import Enum


class TokenType(Enum):

    FUNCTION = "function"
    PRINT = "print"
    EQUALS = "="
    ID = "id"
    INTEGER = "digits"
    LEFTPAREN = "("
    RIGHTPAREN = ")"
    END = "end"
    EOP = "end of program"
    IF = "if"
    ELSE = "else"
    WHILE = "while"
    FOR = "for"
    ITER = (":")
    LE = ("<=", True, False)
    LESSTHAN = ("<", True, False)
    GE = (">=", True, False)
    GREATERTHAN = (">", True, False)
    ISEQUALTO = ("==", True, False)
    NOTEQUAL = ("!=", True, False)
    ADD = ("+", False, True)
    SUB = ("-", False, True)
    MUL = ("*", False, True)
    DIV = ("/", False, True)
    MOD = ("%", False, True)
    REV_DIV = ("\\", False, True)
    EXP = ("^", False, True)
    STRING = True
    
    def __init__(self, readable_name, relative_op = False, arithmetic_op = False):
        self.readable_name = readable_name
        self.relative_op = relative_op
        self.arithmetic_op = arithmetic_op
