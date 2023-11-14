from typing import Tuple, Dict, TypeVar, Generic

from dftools.core.compare.compare_events import ComparisonResult, ComparisonResults
from dftools.utils.dict_util import get_unique_key_list

T = TypeVar('T')
C = TypeVar('C', bound=ComparisonResult)

class Comparator(Generic[T, C]):
    """
        Comparator class for the type T with a comparison output object for compare method as type C
    """
    def __init__(self) -> None:
        pass

    def compare(self, obj1 : T, obj2 : T, root_key_path : Tuple[str] = ()) -> C:
        return NotImplementedError('The compare method is not implemented for class : ' + str(type(self)))

    def compare_multiple(self, objects1 : Dict[str, T], objects2 : Dict[str, T]) -> ComparisonResults:
        results = ComparisonResults()
        key_list = get_unique_key_list(objects1, objects2)
        for key in key_list :
            results.append(self.compare(
                objects1[key] if key in objects1 else None
                , objects2[key] if key in objects2 else None
                , ()
            ))
        return results
