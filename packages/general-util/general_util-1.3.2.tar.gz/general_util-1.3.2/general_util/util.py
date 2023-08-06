from __future__ import annotations

class Util:
    @staticmethod
    def unique_append(list: list, element) -> list:
        if element not in list:
            list.append(element)

        return list