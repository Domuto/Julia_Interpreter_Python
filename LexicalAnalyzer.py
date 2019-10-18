from Exceptions import LexicalAnalyzerException
import sys
from TokenType import TokenType
from Token import Token
from ErrorMessages import ErrorMessages
from os.path import abspath, dirname



class LexicalAnalyzer:

    def __init__(self,path):
        self.path=path
        f=open(dirname(abspath(__file__))+"/"+self.path, "r")
        lines=f.readlines()
        #print(type(lines))
        for line in lines:
            #print(type(line))
            line= line.strip('\n')
            self.tokenize(line)


        self.tokens = []
        self.index = 0


    def tokenize(self, program):
        self.tokens = []
        self.index = 0
        tokens = program.split(" ")
        for token in tokens:
            if len(token) > 0:
                self.save_token(token)
        self.tokens.append(Token(TokenType.EOP, ""))

    def save_token(self, token):
        sys.stdout = open("output.txt", "a")
        if token == "end":
            self.tokens.append(Token(TokenType.PRINT, token))
        elif token == "function":
            print(token + " is a function\n")
            self.tokens.append(Token(TokenType.FUNCTION, token))
        elif token == "println":
            print(token + " is a print\n")
            self.tokens.append(Token(TokenType.PRINT, token))
        elif token == "=":
            print(token+"         Token Keyword ID:33  ASSIGN\n")
            self.tokens.append(Token(TokenType.EQUALS, token))
        elif len(token) == 1 and token[0].isalpha():
            print(token + " is a ID\n")
            self.tokens.append(Token(TokenType.ID, token))
        elif self.is_integer(token):
            print(token + " Lexime Value NUMBER " + token + "\n")
            self.tokens.append(Token(TokenType.INTEGER, token))
        elif token == "(":
            print(token+" is Left Paratheses\n")
            self.tokens.append(Token(TokenType.LEFTPAREN, token))
        elif token == ")":
            self.tokens.append(Token(TokenType.RIGHTPAREN, token))
        elif token == "if":
            print(token + " is an If\n")
            self.tokens.append(Token(TokenType.IF, token))
        elif token == "else":
            self.tokens.append(Token(TokenType.ELSE, token))
        elif token == "<=":
            self.tokens.append(Token(TokenType.LE, token))
        elif token == "<":
            self.tokens.append(Token(TokenType.LESSTHAN, token))
        elif token == "":
            self.tokens.append(Token(TokenType.STRING, token))
            print(token + " string\n")
        elif token == ">":
            self.tokens.append(Token(TokenType.GREATERTHAN, token))
        elif token == "==":
            self.tokens.append(Token(TokenType.ISEQUALTO, token))
        elif token == "!=":
            self.tokens.append(Token(TokenType.NOTEQUAL, token))
        elif token == "+":
            print(token + " plus\n")
            self.tokens.append(Token(TokenType.ADD, token))
        elif token == "-":
            self.tokens.append(Token(TokenType.SUB, token))
        elif token == "*":
            self.tokens.append(Token(TokenType.MUL, token))
        elif token == "/":
            self.tokens.append(Token(TokenType.DIV, token))
        elif token == "%":
            self.tokens.append(Token(TokenType.MOD, token))
        elif token == "\\":
            self.tokens.append(Token(TokenType.REV_DIV, token))
        elif token == "^":
            self.tokens.append(Token(TokenType.EXP, token))
        elif token == "while":
            self.tokens.append(Token(TokenType.WHILE, token))
        elif token == "for":
            self.tokens.append(Token(TokenType.FOR, token))
        elif token == ":":
            self.tokens.append(Token(TokenType.ITER, token))
        elif token.startswith('"') or token.endswith('"'):
            token = token.replace('"', '')
            self.tokens.append(Token(TokenType.STRING, token))
            print(token + " is a \n")
#            raise LexicalAnalyzerException(ErrorMessages.ERROR_UNKNOWN_TOKEN_BADTOKEN % token)

    def is_integer(self, token):
        for c in token:
            if not c.isdigit():
                return False
        return True

    def next_token(self):
        token = self.tokens[self.index]
        self.index += 1
        return token

    def peek_token(self):
        return self.tokens[self.index]
