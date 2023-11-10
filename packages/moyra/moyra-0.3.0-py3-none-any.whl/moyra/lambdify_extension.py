from sympy.utilities.iterables import (iterable)
from sympy import Symbol
class SymbolInterator:
    def __init__(self):
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.num = self.num + 1
        return Symbol(f'rep_{self.num}')

    
def doprint(self, funcname, args, expr):
        """Returns the function definition code as a string."""
        from sympy import Dummy,cse,Symbol

        funcbody = []

        if not iterable(args):
            args = [args]

        argstrs, expr = self._preprocess(args, expr)

        ## --------------- Addition -----------------
        replacments, exprs = cse(expr,symbols=SymbolInterator())
        if isinstance(expr,tuple):
            expr = tuple(exprs)
        elif isinstance(expr,list):
            expr = exprs
        else:
            expr = exprs[0]
        ## --------------- Addition -----------------

        # Generate argument unpacking and final argument list
        funcargs = []
        unpackings = []

        for argstr in argstrs:
            if iterable(argstr):
                funcargs.append(self._argrepr(Dummy()))
                unpackings.extend(self._print_unpacking(argstr, funcargs[-1]))
            else:
                funcargs.append(argstr)
        arg_vars = ', '.join(funcargs)
        funcsig = f'def {funcname}({arg_vars}):'

        # Wrap input arguments before unpacking
        funcbody.extend(self._print_funcargwrapping(funcargs))

        funcbody.extend(unpackings)

        ## --------------- Addition -----------------
        for variable, expression in replacments:
            funcbody.append(f'{variable} = {self._exprrepr(expression)}')
        ## --------------- Addition -----------------

        funcbody.append('return ({})'.format(self._exprrepr(expr)))

        funclines = [funcsig]
        funclines.extend('    ' + line for line in funcbody)

        return '\n'.join(funclines) + '\n'