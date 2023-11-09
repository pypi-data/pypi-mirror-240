# the spirit of Cleword lives on.

import re
import sys
import json
from .ast import AtomicValue, SimpleValue, Block

__REGEX_BOOLEAN = re.compile(r'\s*(#(?:true|false))')
__REGEX_NUMBER = re.compile(r'^\s*((?:0(?:x[0-9a-fA-F]+|b[01]+|o[0-7]+))|-?(?:(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?))(?:\s|:|=|$)')
__REGEX_QUOTED_STRING = re.compile(r'^\s*((?:"(?:[^"\\\x00-\x1f\x7f]|\\["\\/bfnrt]|\\u[0-9a-fA-F]{4})*"))(?:\s|:|=|$)')
__REGEX_SIMPLE_STRING = re.compile(r'^\s*((?:[^:\\\s=]|\\.|\\=)+)(?:\s|:|=|$)')

def __assert(x, msg: str):
    if not bool(x):
        raise Exception(f'assert failed: {msg}')

__REGEX_ESCAPE = re.compile(r'\\(.)')
def __replace_escape(x: str) -> str:
    return __REGEX_ESCAPE.sub(lambda x: x.groups()[0], x)
    
def __take_atomic_value(x: str, line: int = -1) -> tuple[AtomicValue|None, str]:
    matchres = __REGEX_NUMBER.match(x)
    if matchres:
        resgroups = matchres.groups()
        rest = x[len(resgroups[0]):]
        val = (
            int(resgroups[0][2:], 16) if resgroups[0].startswith('0x')
            else int(resgroups[0][2:], 2) if resgroups[0].startswith('0b')
            else int(resgroups[0][2:], 8) if resgroups[0].startswith('0o')
            else float(resgroups[0]) if '.' in resgroups[0] or 'e' in resgroups[0] or 'E' in resgroups[0]
            else int(resgroups[0], 10)
        )
        return (val, rest)
    matchres = __REGEX_QUOTED_STRING.match(x)
    if matchres:
        resgroups = matchres.groups()
        return (json.loads(resgroups[0]), x[len(resgroups[0]):])
    matchres = __REGEX_BOOLEAN.match(x)
    if matchres:
        resgroups = matchres.groups()
        return (
            True if resgroups[0] == '#true' else False if resgroups[0] == '#false' else False,
            x[len(resgroups[0]):],
        )
    matchres = __REGEX_SIMPLE_STRING.match(x)
    if matchres:
        s : str = matchres.groups()[0]
        if s[0] == '"' and s[-1] == '"':
            print(f'Line {line}: Possible quote string treated as simple string; may contian invalid escape sequence?', file=sys.stderr)
        return (__replace_escape(s), x[len(s):])
    return (None, x)

def __take_simple_value(x: str, line: int = -1) -> tuple[SimpleValue|None, str]:
    first, rest = __take_atomic_value(x, line)
    if first is None: return (None, x)
    if not rest.startswith('='): return (first, rest)
    second, rest = __take_atomic_value(rest[1:], line)
    if second is None: return (first, rest)
    return ((first, second), rest)
            
            
__REGEX_INDENT = re.compile(r'^( *)(.*)?$')
def __parse_head(required_indent: int, current_line: int, x: str) -> Block:
    __assert(x.strip() and not x.strip().startswith('//'), 'comment and empty line should not reach __parse_head')
    res = Block(A=[], B=None, C=None)
    matchres = __REGEX_INDENT.match(x)
    if not matchres: raise Exception(f'Line {current_line+1}: assert failed. ')
    matchres = matchres.groups()
    if len(matchres[0]) != required_indent: raise Exception(f'Line {current_line+1}: invalid indent')
    command = []
    subj = matchres[1]
    while subj:
        val = __take_simple_value(subj, current_line)
        if val[0] is not None:
            command.append(val[0])
            subj = val[1].strip()
            continue
        subj = subj.strip()
        if not subj:
            res.B = None
            break
        __assert(subj[0] and subj[0] == ':', 'non separator should already be parsed as simple value')
        if subj[0] and subj[0] == ':':
            res.B = subj[1:].strip()
            break
    res.A = command
    return res

def __parse_blocks(required_indent: int, current_line: int, lines: list[str]) -> tuple[list[Block], int]:
    res = []
    i = current_line
    lines_length = len(lines)
    while i < lines_length:
        while i < lines_length and ((not lines[i].strip()) or lines[i].strip().startswith('//')): i += 1
        if i >= lines_length: break
        line = lines[i]
        matchres = __REGEX_INDENT.match(line)
        if not matchres or len(matchres.groups()[0]) < required_indent: break
        head = __parse_head(required_indent, current_line, line)
        if head.B is None:
            res.append(head); i += 1
            continue
        j = i + 1
        while j < lines_length and ((not lines[j].strip()) or lines[j].strip().startswith('//')): j += 1
        if j >= lines_length:
            res.append(head); i = j
            break
        nextline = lines[j]
        matchres = __REGEX_INDENT.match(nextline)
        if not matchres or len(matchres.groups()[0]) <= required_indent:
            res.append(head); i = j
            break
        matchres = matchres.groups()
        children = __parse_blocks(len(matchres[0]), j, lines)
        head.C = children[0] or None
        res.append(head)
        i = children[1]
    return (res, i)

def parse(x: str) -> list[Block]:
    return __parse_blocks(0, 0, x.splitlines())[0]

