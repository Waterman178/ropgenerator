# -*- coding: utf-8 -*- 
# Main module:  semantic-mode 

from prompt_toolkit import PromptSession, ANSI

from ropgenerator.IO import string_semantic, string_bold, string_special, banner
from ropgenerator.semantic.Find import find

import sys

# Definitions of commands 
CMD_HELP = "help"
CMD_ASSERT = "assert"
CMD_FIND = "find"
CMD_MAIN = "main"
CMD_EXIT = "exit"


helpStr = banner([string_bold('Semantic-Mode Commands'),
    string_special('(For more info about a command type <cmd -h>)')])
helpStr += '\n\t' + string_bold(CMD_FIND) + ': \t\tfind gadgets/ropchains'
helpStr += '\n\n\t' + string_bold(CMD_HELP) + ': \t\tshow this help'
helpStr += '\n\t' + string_bold(CMD_MAIN) + ': \t\treturn to the main menu'
helpStr += '\n\t' + string_bold(CMD_EXIT) + ': \t\texit ROPGenerator'

promptSession = PromptSession(ANSI(u"("+ string_semantic(u'semantic') +u")> "))

def semantic_mode():
    """
    Returns
    -------
    True if ROPGenerator must continue
    False if ROPGenerator must be closed 
    """
    
    finish = False
    while( not finish ):
        try:
            user_input = promptSession.prompt()
            args = user_input.split()
            argslen = len(args)
            if( argslen > 0 ):
                command = args[0]
            else:
                command = None

            if( command == CMD_FIND ):
                find(args[1:])
            elif( command == CMD_EXIT ):
                return False
            elif( command == CMD_HELP ):
                print(helpStr)
            elif( command == CMD_MAIN ):
                finish = True
            if( command != None ):
                print('')
        except KeyboardInterrupt:
            pass
    return True












