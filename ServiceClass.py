from enum import Enum


class ServiceState(Enum):
    ERROR = -1
    NOT_ACTIVE = 0
    ACTIVE = 1


class Service:
    name = ''
    state = ServiceState.NOT_ACTIVE
    service = None  # This needs to be a reference to a function. Take the service class method you want to run and put it here

    def __init__(self, name, service):
        self.name = name
        self.state = ServiceState.ACTIVE
        self.service = service
