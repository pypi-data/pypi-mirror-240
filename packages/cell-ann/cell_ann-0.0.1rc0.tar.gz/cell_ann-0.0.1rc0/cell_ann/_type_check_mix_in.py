import inspect

from typing import Any, Dict

from . import __logger__


class TypeCheckMixIn(object):
    _enabled = True
    
    def __init__(self, *args, **kwargs):
        
        """enabled by default"""
        
        __logger__.info(msg=f"{self._cls_name}:TypeChecker ENABLED")
        
    @property
    def _cls_name(self):
        return self.__class__.__name__
    
    def _disable_type_check(self):
        self._enabled = False
        __logger__.info(msg=f"{self._cls_name}:TypeChecker DISABLED.")
        
    def _enable_type_check(self):
        self._enabled = True
        __logger__.info(msg=f"{self._cls_name}:TypeChecker DISABLED.")
    
    @property
    def _TYPECHECK_IGNORE(self):
        return ["self", "args", "kwargs"]

    @property
    def _SIGNATURE(self):
        return inspect.signature(self._func).parameters.items()

    def __check_types__(self, func: Any, passed: Dict):
        """
        func
        passed
        """

        if self._enabled:
            self._func = func

            for key, val in self._SIGNATURE:
                if not key in self._TYPECHECK_IGNORE:
                    assert isinstance(passed[key], val.annotation), TypeError(
                        f"arg: {key} is not of correct type: {val}"
                    )
