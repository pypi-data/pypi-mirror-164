class Container:
    
    def __init__(self, **kwargs) -> None:
        self.__dict__ = kwargs
