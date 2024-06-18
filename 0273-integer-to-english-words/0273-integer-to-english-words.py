class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        num2word = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred'
        }
        
        coll_words = [(10**9, 'Billion'), (10**6, 'Million'), (1000, 'Thousand')]
        
        def helper(number):
            # Not greater than thousand
            res = []
            v = number//100
            number %= 100
            if v != 0:
                res.append(num2word[v])
                res.append('Hundred')
                
            if number in num2word:
                res.append(num2word[number])
            else:
                v = number//10
                number %= 10
                if v != 0:
                    res.append(num2word[v*10])

                if number != 0:
                    res.append(num2word[number])
                
            return res
        
        ans = []
        for v, word in coll_words:
            val = num // v
            if val == 0:
                continue
            
            num = num % v
            ans.extend(helper(val))
            ans.append(word)
            
        ans.extend(helper(num))
        return ' '.join(ans)