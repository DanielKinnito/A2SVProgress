class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        answer = []
        conver = defaultdict(list)

        for t in transactions:
            name, time, amount, city = t.split(',')
            time, amount = int(time), int(amount)
            conver[name].append({'time': time, 'city': city})

        for t in transactions:
            name, time, amount, city = t.split(',')
            time, amount = int(time), int(amount)
            
            if amount > 1000:
                answer.append(t)
            
            elif name in conver:
                for same_name in conver[name]:
                    if abs(same_name['time'] - time) <= 60 and same_name['city'] != city:
                        answer.append(t)
                        break

        return answer
        