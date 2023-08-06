from .lexer import BaseLexer, FileLexer, StringLexer
from .parser import Parser
from .version import __version__, version_info

a = "test\
    123"

__all__ = [
    "BaseLexer", 
    "FileLexer",
    "StringLexer"
]