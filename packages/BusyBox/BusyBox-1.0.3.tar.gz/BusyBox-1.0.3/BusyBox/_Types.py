# -*- coding: utf-8 -*-
from typing import Tuple, Any, Dict


def _f(args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> Any: pass


FunctionType = type(_f)