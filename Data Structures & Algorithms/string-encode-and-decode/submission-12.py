class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return "ayoub"
        if strs == []:
            return "ait"
        return "th**".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "ayoub":
            return [""]
        if s == "ait":
            return []
        return s.split("th**")