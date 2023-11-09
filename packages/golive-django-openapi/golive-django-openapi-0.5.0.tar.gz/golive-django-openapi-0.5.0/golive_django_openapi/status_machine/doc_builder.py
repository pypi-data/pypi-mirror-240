# Author: kk.Fang(fkfkbill@gmail.com)

__all__ = [
    "StatusMachineDocBuilder",
]

from os import linesep
from typing import Type

from .status_machine import *


class StatusMachineDocBuilder:
    """状态机文档输出"""

    def __init__(self, sm: Type[StatusMachine]):
        assert sm.EXPORT_FLAG, f"using doc builder, the export_flag of the target StatusMachine is required."
        self.sm = sm

    def build_markdown(self) -> str:
        """输出markdown文档"""
        title = f"""
## {self.sm.__doc__}

导出唯一标识：{self.sm.EXPORT_FLAG}
"""
        content = [
            "|展示标签|值|值类型|下一步值|",
            "|----|----|----|----|",
        ]
        for v, smv in self.sm.ALL_STATUS_DICT.items():
            content.append(f"|{smv.name}|{smv.value}|{type(smv.value).__name__}|{smv.next_status_values}|")
        return linesep.join([title, linesep.join(content)])
