class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall('[+-]?\d+/\d+', expression)
    
        nume, denom = 0, 1
        
        for frac in fractions:
            num, den = map(int, frac.split('/'))
            nume = nume * den + num * denom
            denom *= den
            common = gcd(abs(nume), denom)
            nume //= common
            denom //= common
        
        if nume == 0:
            return "0/1"
        
        return f"{nume}/{denom}"