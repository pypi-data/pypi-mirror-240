# -*- coding: utf-8 -*-
""" class实例化 延迟 """
import abc
import copy
import re
from typing import Tuple, Any, Dict, Union, List, Type
from types import FunctionType as F, MethodType
from functools import wraps
from inspect import signature, Parameter, getargs, getargspec, getfullargspec
from BusyBox.FactoryUtils import FactoryInjectAPI, BoxAPI
from BusyBox._Types import FunctionType


def camel_name_to(f_name: str):
    """
        生成实例化名 根据类的驼峰化转变成 a_b_c 形式
    :param f_name:
    :return:
    """
    pattern = "[A-Z]"
    return re.sub(pattern, lambda x: "_" + x.group(0).lower(), f_name).strip('_')


class Box(BoxAPI):

    def __init__(self):
        self.__payload = None
        # 存放类对应的实例 类 以及 其签名信息
        self.__objs_class_mappings = {}
        self.__fac_objs_class_mappings = {}

    def inject_factory(self, *fac_cls_args: Type[FactoryInjectAPI], **fac_cls_kwargs):
        _refer = fac_cls_kwargs.get('refer', None)

        for _fac in fac_cls_args:
            _sig = _fac.construct.__annotations__
            _cls_name = _sig['return'].__name__
            if _cls_name.endswith('API'):
                _cls_name = _cls_name[:-3]
            _cls_name = camel_name_to(_cls_name)
            self.__fac_objs_class_mappings.update({_cls_name: {'objs': [], }})
            if _refer:
                if isinstance(_refer, dict):
                    self.__fac_objs_class_mappings[_cls_name]['objs'].append(_fac().construct(**_refer))
                elif isinstance(_refer, tuple):
                    self.__fac_objs_class_mappings[_cls_name]['objs'].append(_fac().construct(*_refer))
                else:
                    self.__fac_objs_class_mappings[_cls_name]['objs'].append(_fac().construct(_refer))
            else:
                self.__fac_objs_class_mappings[_cls_name]['objs'].append(_fac().construct())

    def inject_lazy_factory(self, obj_fd: str, fac: FunctionType, **class_kwargs):
        # args_payload = class_kwargs.get('args_payload', None)
        kwargs_payload = class_kwargs.get('kwargs_payload', None)
        self.__objs_class_mappings.update({obj_fd: dict(_obj=None, _cls=fac, _payload=dict(
            # ___args=args_payload,
            ___kwargs=kwargs_payload
        ))})

    def inject(self, *class_args, **class_kwargs):

        _payload = class_kwargs.get('payload', None)

        if _payload is None:
            _payload = {}
        args_payload = class_kwargs.get('args_payload', None)
        kwargs_payload = class_kwargs.get('kwargs_payload', None)

        _dependency = class_kwargs.get('dependency', None)
        __class_args = list(class_args)
        if _dependency is not None:
            __class_args.append(_dependency)

        for _c in __class_args:
            # 生成实例化名 根据类的驼峰化转变成 a_b_c 形式
            # _cls 本质上是 生成具体对象的工厂方法
            __c_name = camel_name_to(_c.__name__)
            if args_payload and kwargs_payload:
                self.__objs_class_mappings.update({__c_name: dict(_obj=None, _cls=_c, _payload=dict(
                    ___args=args_payload,
                    ___kwargs=kwargs_payload
                ))})
                continue
            if isinstance(_payload, tuple):
                self.__objs_class_mappings.update({__c_name: dict(_obj=None, _cls=_c, _payload=dict(___args=_payload))})
                continue
            if isinstance(_payload, dict):
                self.__objs_class_mappings.update({__c_name: dict(_obj=None, _cls=_c, _payload=dict(___kwargs=_payload))})

    def reset(self, _c_name):
        """ 重置对象 """
        _maybe_ins_obj, is_ins = self.__get_probable_instance_or_class(_c_name)
        if is_ins:
            __get_payload = self.__get_payload(_c_name)
            if len(__get_payload):
                self.__set_val_into_class(__get_payload, _maybe_ins_obj.__init__)
            return _maybe_ins_obj

    def destroy(self, _c_name):
        """ 主动销毁对象 """
        del self.__objs_class_mappings[_c_name]

    def depend(self, *depend_args, **depend_kwargs):

        def decorator(_func):

            self.inject(_func)

            @wraps(_func)
            def _wrap(_self, *wrap_args, **wrap_kwargs):
                # print(_self)
                # print(wrap_args)
                # print(wrap_kwargs)
                return
            return _wrap

        return decorator

    def invoke(self, name,  *payload_args, **payload_kwargs):
        return self.__invoke(name, *payload_args, **payload_kwargs)

    def init_invoke(self, ins_fd: str):
        if ins_fd in self.__objs_class_mappings:
            return self.__get_instance_obj(ins_fd)
        if ins_fd in self.__fac_objs_class_mappings:
            return self.__fac_objs_class_mappings[ins_fd]['objs'][0]

    def __get_probable_instance_or_class(self, _c_name):
        """
        返回实例 或者 类
        :param _c_name:
        :return:
        """
        if self.__objs_class_mappings[_c_name]['_obj'] is None:
            return self.__objs_class_mappings[_c_name]['_cls'], False
        return self.__objs_class_mappings[_c_name]['_obj'], True

    def __get_payload(self, _c_name):
        """
            根据实例化名获取类初始化参数
        :param _c_name:
        :return:
        """
        return self.__objs_class_mappings[_c_name]['_payload']

    def __invoke(self, _c_name, *payload_args, **payload_kwargs):
        _maybe_ins_obj, is_ins = self.__get_probable_instance_or_class(_c_name)
        # 判断是否为实例
        if is_ins:
            return _maybe_ins_obj
        else:
            _ins_obj = _maybe_ins_obj(*payload_args, **payload_kwargs)
            self.__set_inst_obj(_c_name, _ins_obj)
            return _ins_obj

    def __set_inst_obj(self, _c_name, _ins_obj):
        """ 存储实例 """
        if self.__objs_class_mappings[_c_name]['_obj'] is None:
            self.__objs_class_mappings[_c_name]['_obj'] = _ins_obj

    def __get_instance_obj(self, _c_name):
        _ins_obj = None
        _maybe_ins_obj, is_ins = self.__get_probable_instance_or_class(_c_name)
        if is_ins:
            return _maybe_ins_obj
        else:
            __get_payload = self.__get_payload(_c_name)
            if len(__get_payload):
                _ins_obj = self.__set_val_into_class(__get_payload, _maybe_ins_obj)
            else:
                _ins_obj = _maybe_ins_obj()
            self.__set_inst_obj(_c_name, _ins_obj)
            return _ins_obj

    def __getattr__(self, _ins_name: str):
        """
            根据实例名获取实例对象
        :param _ins_name:
        :return:
        """

        if _ins_name in self.__objs_class_mappings:
            return self.__get_instance_obj(_ins_name)
        if _ins_name in self.__fac_objs_class_mappings:
            return self.__fac_objs_class_mappings[_ins_name]['objs'][0]

    @staticmethod
    def __set_val_into_class(__get_payload: dict, _maybe_ins_obj: Any):

        _ins_obj = None

        if '___args' in __get_payload and '___kwargs' in __get_payload:
            __args = __get_payload['___args']
            __kwargs = __get_payload['___kwargs']
            _ins_obj = _maybe_ins_obj(*__args, **__kwargs)
        elif '___args' in __get_payload:
            __args = __get_payload['___args']
            _ins_obj = _maybe_ins_obj(*__args)
        elif '___kwargs' in __get_payload:
            __kwargs = __get_payload['___kwargs']
            if __kwargs and not isinstance(_maybe_ins_obj, MethodType):
                _del_params = []
                _func_sign = signature(_maybe_ins_obj.__init__)
                for p in __kwargs:
                    if p not in _func_sign.parameters:
                        _del_params.append(p)
                    # print(_func_sign.parameters)
                for del_k in _del_params:
                    __kwargs.pop(del_k)
            _ins_obj = _maybe_ins_obj(**__kwargs)
        return _ins_obj

    @staticmethod
    def __filter_valid_params(_func: FunctionType, params: dict):

        __full_args = getfullargspec(_func)

        if __full_args.varkw is not None and __full_args.varargs is not None:
            _args = params.pop(__full_args.varkw)
            return 'both', _args, params
        if __full_args.varkw is not None:
            return 'only_has_kw', None, params
        if __full_args.varargs is not None:
            # _args = params.pop(__full_args.varargs)
            return 'only_has_args', params
        _del_params = []
        _func_sign = signature(_func)
        if params:
            for p in params:
                if p not in _func_sign.parameters:
                    _del_params.append(p)
                # print(_func_sign.parameters)
            for del_k in _del_params:
                params.pop(del_k)
        return 'normal', params, None

    def __repr__(self):
        """
            打印仓库所有实例库存
        :return:
        """
        _ret = ''
        for _cls, _repo in self.__objs_class_mappings.items():
            _ret += f'class -> {_cls} repo -> {_repo}\n'
        return _ret


class HostFactory(object):
    box: Box

    def __init__(self):
        self.box = Box()

    def __getattr__(self, _ins_name: str):
        return self.box.init_invoke(_ins_name)


def factory_inject(*factory_args: Type[FactoryInjectAPI], **factory_kwargs):

    def decorator(_host_c: Union[BoxAPI, HostFactory, Any]):
        """
        :param _host_c: 宿主类
        """
        @wraps(_host_c)
        def _wrap(*_host_c_args, **_host_c_kwargs):
            """
            :param refer: 从宿主类的实例 引用进 注入类的实例
            :param _host_c_args:
            :param _host_c_kwargs:
            :return:
            """
            _host_cal_depends_prop_fd_map = dict()

            for property_fd, _cal in _host_c.__annotations__.items():
                if _cal in _host_cal_depends_prop_fd_map:
                    _host_cal_depends_prop_fd_map[_cal].append(property_fd)
                else:
                    _host_cal_depends_prop_fd_map[_cal] = [property_fd, ]
            """ 宿主类的实例化 """
            _host_c_ins = _host_c(*_host_c_args, **_host_c_kwargs)
            _refer = factory_kwargs.get('refer', None)

            # 引用宿主实例的指定对象
            # 全局
            _refer_mapping = {}
            # 单一
            _special_refer_mapping = {}
            """ 获取宿主实例的待引用的属性 """
            if _refer is not None:
                for property_in_host_ins, property_in_host_cal in _host_c_ins.__annotations__.items():
                    if isinstance(_refer, tuple):
                        pass
                    else:
                        if property_in_host_cal == _refer:
                            _refer_mapping.update({property_in_host_cal: getattr(_host_c_ins, property_in_host_ins)})

            """
                解构子类构造函数签名
                1、塞入宿主引用属性
            """
            for _child_fac in factory_args:

                """ 注入类的构造函数签名 """

                if isinstance(_child_fac, tuple):
                    child_construct_func_sign = _child_fac[0].construct.__annotations__
                else:
                    child_construct_func_sign = _child_fac.construct.__annotations__

                """ 注入类的构造函数入参 搬进宿主类引用 """

                _child_params = copy.deepcopy(child_construct_func_sign)
                if 'return' in _child_params:
                    del _child_params['return']
                for _param_str, _p_cal in _child_params.items():
                    if _p_cal in _refer_mapping:
                        _child_params[_param_str] = _refer_mapping.get(_p_cal)

                """ 注入类的构造函数调用 """
                child_cls = child_construct_func_sign['return']
                if factory_kwargs.get('__lazy', True) and isinstance(_host_c_ins, HostFactory) \
                        and child_cls in _host_cal_depends_prop_fd_map:
                    for _fd in _host_cal_depends_prop_fd_map[child_cls]:
                        _host_c_ins.box.inject_lazy_factory(_fd, _child_fac().construct, kwargs_payload=_child_params)
                else:
                    if child_cls in _host_cal_depends_prop_fd_map:
                        for _fd in _host_cal_depends_prop_fd_map[child_cls]:
                            if _refer_mapping.__len__() > 0:
                                """ 构造函数有参数 """
                                setattr(_host_c_ins, _fd, _child_fac().construct(**_child_params))
                            else:
                                """ 构造函数无参数 """
                                setattr(_host_c_ins, _fd, _child_fac().construct())
            return _host_c_ins
        return _wrap
    return decorator
