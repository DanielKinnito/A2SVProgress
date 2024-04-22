class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        outdegree = {}
        adj_list = defaultdict(list)
        
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                adj_list[ing].append(recipes[i])
                outdegree[recipes[i]] = outdegree.get(recipes[i], 0) + 1
                outdegree[ing] = outdegree.get(ing, 0) + 0
        
        recipes = set(recipes)
        supplies = set(supplies)
        que = deque()
        for key in outdegree:
            if outdegree[key] == 0 and key in supplies:
                que.append(key)
        
        answer = []
        while que:
            ing = que.popleft()
            if ing in recipes:
                answer.append(ing)
            
            for ne in adj_list[ing]:
                outdegree[ne] = outdegree.get(ne, 0) - 1
                if ne in outdegree and outdegree[ne] == 0:
                    que.append(ne)
            
        return answer