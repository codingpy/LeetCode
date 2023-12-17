class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            ruleKey = 0
        elif ruleKey == "color":
            ruleKey = 1
        elif ruleKey == "name":
            ruleKey = 2

        return len([item for item in items if item[ruleKey] == ruleValue])
