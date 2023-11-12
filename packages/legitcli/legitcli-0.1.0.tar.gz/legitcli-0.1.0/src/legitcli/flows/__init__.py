from enum import Enum
from typing import Callable, Set
import flows.validate as validate
import flows.help as help
import flows.setup as setup


class Flows(Enum):
    VALIDATE = validate.run_flow
    HELP = help.run_flow
    SETUP = setup.run_flow

    @staticmethod
    def get(key: str) -> Callable[[], None]:
        """Get flow function from key. If key can't be found, returns
        default 'help' flow. Key value is not case sensitive"""
        key = key.upper()
        self_dict = {
            name: value
            for name, value in filter(lambda x: x[0].isupper(), Flows.__dict__.items())
        }
        return self_dict.get(key, Flows.HELP)

    @staticmethod
    def get_flow_names() -> Set[str]:
        """Returns a set of all flow variants' names, lower cased."""
        return {name.lower() for name in filter(str.isupper, Flows.__dict__)}
