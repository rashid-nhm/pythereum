##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
"""RestrictedPython package."""

# flake8: NOQA: E401

# This is a file to define public API in the base namespace of the package.
# use: isort:skip to supress all isort related warnings / errors,
# as this file should be logically grouped imports

# compile_restricted methods:
from pythereum.restricted_python.compile import compile_restricted  # isort:skip
from pythereum.restricted_python.compile import compile_restricted_eval  # isort:skip
from pythereum.restricted_python.compile import compile_restricted_exec  # isort:skip
from pythereum.restricted_python.compile import compile_restricted_function  # isort:skip
from pythereum.restricted_python.compile import compile_restricted_single  # isort:skip

# predefined builtins
from pythereum.restricted_python.Guards import safe_builtins  # isort:skip
from pythereum.restricted_python.Guards import safe_globals  # isort:skip
from pythereum.restricted_python.Limits import limited_builtins  # isort:skip
from pythereum.restricted_python.Utilities import utility_builtins  # isort:skip

# Helper Methods
from pythereum.restricted_python.PrintCollector import PrintCollector  # isort:skip
from pythereum.restricted_python.compile import CompileResult  # isort:skip

# Policy
from pythereum.restricted_python.transformer import RestrictingNodeTransformer  # isort:skip


from pythereum.restricted_python.Eval import RestrictionCapableEval
