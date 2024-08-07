from typing import Optional

class Singleton:

    _instance: Optional['Singleton'] = None

    def __init__(self):
        # Singleton pattern must prevent normal instantiation
        raise Exception("Cannot directly instantiate a Singleton. Access via get_instance()")

    @classmethod
    def get_instance(cls) -> 'Singleton':
        # This is the only way to access the one and only instance
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


class ConfigurableSingleton(Singleton):

    @classmethod
    def get_instance(cls) -> 'Singleton':
        # This is the only way to access the one and only instance
        if cls._instance is None:
            raise Exception("Must call %s.configure_instance(config) first" % cls.__name__)
        return cls._instance

    @classmethod
    def configure_instance(cls, config: any = None):
        # Must be called before the first get_instance() call
        if cls._instance:
            raise Exception("Instance already configured")
