# -*- coding: utf-8 -*-
import abc
from typing import Any, Union, Tuple, Dict

from BusyBox._Types import FunctionType


class BoxAPI(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def inject_lazy_factory(self, obj_fd: str, fac: FunctionType, **class_kwargs):
        raise NotImplementedError


class FactoryInjectAPI(metaclass=abc.ABCMeta):
    """
        抽象工厂
    """
    @abc.abstractmethod
    def construct(self, *args, **kwargs) -> Any:
        """
            构造实例的方法
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError