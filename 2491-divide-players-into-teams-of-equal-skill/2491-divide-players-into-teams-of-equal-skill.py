class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) < 3:
            return skill[0] * skill[1]

        skill.sort()   
        l , r = 0, len(skill)-1

        goal = skill[l] + skill[r]
        chemo = skill[l] * skill[r]
        l+=1
        r-=1
        while l < r:
            sumSkill = skill[l] + skill[r]
            if sumSkill != goal:
                return -1
            chemo += skill[l] * skill[r]
            l+=1
            r-=1
        return chemo