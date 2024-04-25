class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_ac = {}
        email_to_id = {}
        id_to_email = {}

        for idx, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                name_ac[email] = name
                if email not in email_to_id:
                    email_to_id[email] = len(email_to_id)
                    id_to_email[len(id_to_email)] = email

        dsu = DSU(len(email_to_id))

        for account in accounts:
            for i in range(1, len(account) - 1):
                email1, email2 = account[i], account[i + 1]
                dsu.union(email_to_id[email1], email_to_id[email2])

        groups = {}
        for email, idx in email_to_id.items():
            group_id = dsu.find(idx)
            if group_id not in groups:
                groups[group_id] = []
            groups[group_id].append(email)

        merged_accounts = []
        for group_id, emails in groups.items():
            name = name_ac[emails[0]]
            merged_accounts.append([name] + sorted(emails))

        return merged_accounts