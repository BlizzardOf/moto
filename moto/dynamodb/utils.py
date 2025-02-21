from typing import List


def extract_duplicates(input_list: List[str]) -> List[List[str]]:
    input_list_copy = input_list.copy()
    while len(input_list_copy) > 0:
        # start at front of list
        item = input_list_copy.pop(0)
        if item in input_list_copy:
            return [[item], [item]]
        else:
            for second_item in input_list_copy:
                if second_item.startswith(item + "."):
                    return [[item], second_item.split(".")]
                elif item.startswith(second_item + "."):
                    return [item.split("."), [second_item]]
    return []
