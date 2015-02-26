from lib.action import CheckmateBaseAction

__all__ = [
    'ShowServerVersionAction'
]


class ShowServerVersionAction(CheckmateBaseAction):
    def run(self):
        return self.version
