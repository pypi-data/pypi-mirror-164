#! /usr/bin/env python
# -*- coding: utf-8 -*-

from inspect import isclass, isfunction, ismethod

class InjectError(Exception):
    pass

def _inject_to(data, self):
    '''
    actual inject method
    '''
    if not self or not hasattr(self, '_pydatatest_variables'):
        raise InjectError('function not injectable')
    for i, name in enumerate(self._pydatatest_variables):
        setattr(self, name, data[i])


def _inject_multi_to(dataset, self):
    '''
    inject multi data into one testcase method
    '''
    if not self or not hasattr(self, '_pydatatest_variables'):
        raise InjectError('function not injectable')
    if len(dataset) > 1:
        data = dataset[0]
        self._pydatatest_dataset = dataset[1:]
        self._pydatatest_multi = True
    else:
        data = dataset[0]
        self._pydatatest_dataset = None
        self._pydatatest_multi = False
    for i, name in enumerate(self._pydatatest_variables):
        setattr(self, name, data[i])


def _remove(self):
    '''
    delete injected data from runner after completed a testcase method
    '''
    _pydatatest_variables = self._pydatatest_variables
    for name in self._pydatatest_variables:
        delattr(self, name)


def inject(data, multi=False):
    '''
    inject test data to a scope (a testcase method)
    '''
    def decorator(scope):
        if ismethod(scope):
            func = scope
            def wrapper(self):
                if multi:
                    _inject_multi_to(data, self)
                else:
                    _inject_to(data, self)
                func(self)
                _remove(self)
            return wrapper
        else:
            raise InjectError("inject is allowed on testcase method")
    return decorator


def inject_def(title=[], session=False):
    '''
    declare inject data variable (used in a testcase class)
    '''
    def decorator(scope):
        if isclass(scope) and scope.getattr("_dataset"):
            klass = scope
            if session:
                import requests
                def setUpSession(func, klass):
                    def decorator(*args, **kw):
                        klass.session = requests.Session()
                        func(*args, **kw)
                    return decorator

                def tearDownSession(func, klass):
                    def decorator(*args, **kw):
                        klass.session.close()
                        func(*args, **kw)
                    return decorator
                
                klass.setUp = setUpSession(klass.setUp, klass)
                klass.tearDown = tearDownSession(klass.tearDown, klass)
            return type(klass.__name__, (klass, ), {"_pydatatest_variables": title})
        else:
            raise InjectError("inject_def is allowed on testcase class")
    return decorator