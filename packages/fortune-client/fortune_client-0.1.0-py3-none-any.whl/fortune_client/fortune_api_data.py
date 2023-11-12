
from typing import ClassVar
from pydantic import BaseModel


SLASH = '/'


class FortuneApiData(BaseModel):

    LIST: ClassVar[str] = 'list'
    DICT: ClassVar[str] = 'dict'

    path: str
    isDirectory: bool
    content: list | dict

    def content_type(self) -> str:
        if isinstance(self.content, list):
            return self.LIST
        return self.DICT

    @classmethod
    def create(cls, path: str, content: list | dict):
        return cls(
            path=path,
            isDirectory=True if path is None
                                or path == ''
                                or path[-1] == SLASH
            else False,
            content=content,
        )
