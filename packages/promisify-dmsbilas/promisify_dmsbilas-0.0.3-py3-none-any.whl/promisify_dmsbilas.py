from collections.abc import Callable, Iterable, Mapping
from threading import Thread
from typing import Any;


class Promise(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None ):
          Thread.__init__(self, group, target, name, args, kwargs)
          self.name = target
          self._return = None
          self.start()

    """ Overriding RUN method inside Thread class"""

    def run(self):
          print(f"Thread Started : {self.getName}")
          if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)
                return self._return

    """ Overriding JOIN method inside Thread class """

    def join(self):
          Thread.join(self)
          return self._return