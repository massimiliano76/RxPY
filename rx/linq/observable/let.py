from six import add_metaclass

from rx.observable import Observable
from rx.internal import ExtensionMethod

@add_metaclass(ExtensionMethod)
class ObservableLet(Observable):
    """Uses a meta class to extend Observable with the methods in this class"""

    def let_bind(self, func):
        """Returns an observable sequence that is the result of invoking the 
        selector on the source sequence, without sharing subscriptions. This 
        operator allows for a fluent style of writing queries that use the same 
        sequence multiple times.
    
        selector -- {Function} Selector function which can use the source 
            sequence as many times as needed, without sharing subscriptions to 
            the source sequence.
     
        Returns an observable {Observable} sequence that contains the elements 
        of a sequence produced by multicasting the source sequence within a 
        selector function."""
        
        return func(self)
        
    let = let_bind
