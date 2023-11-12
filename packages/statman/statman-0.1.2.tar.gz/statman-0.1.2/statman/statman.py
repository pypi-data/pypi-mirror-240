import statman.stopwatch

_registry = {}


class Statman():

    def __init__(self):
        pass

    @staticmethod
    def reset():
        '''Clears all metrics from the registry.'''
        _registry.clear()

    @staticmethod
    def count():
        '''Returns a count of the registered metrics.'''
        return len(_registry.keys())

    @staticmethod
    def stopwatch(name: str = None, autostart: bool = False, initial_delta: float = None) -> statman.Stopwatch:
        ''' Returns a stopwatch instance.  If there is a registered stopwatch with this name, return it.  If there is no registered stopwatch with this name, create a new instance, register it, and return it. '''
        sw = Statman.get(name)

        if not sw:
            sw = statman.Stopwatch(name=name, autostart=autostart, initial_delta=initial_delta)

        if not name is None:
            Statman.register(name, sw)

        return sw

    @staticmethod
    def register(name, metric):
        '''Manually register a new metric.'''
        _registry[name] = metric

    @staticmethod
    def get(name):
        metric = None
        if name:
            metric = _registry.get(name)
        return metric
