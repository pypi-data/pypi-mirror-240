from simple_value_object import ValueObject, invariant


sources: list = []


class Source:
    def __init__(self, path: str, probability: int | None = None):
        self.path: str = path
        self.probability: int | None = probability


class Parameters(ValueObject):

    def __init__(self, 
        url: str, 
        explore: bool, 
        recursive: bool, 
        path: tuple, 
        index: int | None
    ):
        pass

    @invariant
    def recursive_only_for_explore(self) -> bool:
        return not self.recursive or self.recursive and self.explore

    @invariant
    def index_only_for_files(self) -> bool:
        return self.explore and self.index is None or not self.explore

    @invariant
    def max_one_path_for_explore(self) -> bool:
        return not self.explore or (self.explore and len(self.path) <= 1)

    @invariant
    def validate_path(self) -> bool:
        try:
            if self.path and not self.explore:
                for value in self.path:
                    if value[0] == '%':
                        if self._expected_path():
                            raise ValueError('Invalid path')
                        sources[-1].probability = int(value[1:])
                    else:
                        sources.append(Source(value))
        except ValueError:
            return False
        return True

    @staticmethod
    def _expected_path() -> int:
        return len(sources) == 0 or sources[-1].probability is not None

