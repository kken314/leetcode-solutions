class Solution:
    def intToRoman(self, num: int) -> str:
        # num = abcd
        roman = "" 
        roman += "M" * (num // 1000)
        num %= 1000
        # num = bcd
        hundred = num // 100 # hundred = b
        if hundred == 9: # 900
            roman += "CM"
        elif hundred == 4: # 400
            roman += "CD"
        elif hundred < 5: # 000, 100, 200, 300
            roman += "C" * hundred
        else: # 500, 600, 700, 800
            roman +=  "D" + ("C" * (hundred - 5))
        num %= 100
        # num = cd
        ten = num // 10 # ten = c
        if ten == 9: # 90
            roman += "XC"
        elif ten == 4: # 40
            roman += "XL"
        elif ten < 5: # 00, 10, 20, 30
            roman += "X" * ten
        else: # 50, 60, 70, 80
            roman += "L" + ("X" * (ten - 5))
        num %= 10
        # num = d
        if num == 9:
            roman += "IX"
        elif num == 4:
            roman += "IV"
        elif num < 5:
            roman += "I" * num
        else:
            roman += "V" + ("I" * (num - 5))
        
        return roman