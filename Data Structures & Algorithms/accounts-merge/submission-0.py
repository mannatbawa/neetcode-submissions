class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 1. initialization needed for find and union to work proplery
        # map main email key to the other emails
        self.parent = {}
        self.size = {}
        self.email_name = {}
    
        # every email should be set to a parent of itself
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                self.parent[accounts[i][j]] = accounts[i][j]
                # every size of the email should be set to 1
                self.size[accounts[i][j]] = 1
                self.email_name[accounts[i][j]] = accounts[i][0]


        # 2. go through each account and union the emails to the first one in the account accounts[i][1]
        for i in range(len(accounts)):
            for j in range(2, len(accounts[i])):
                self.union(accounts[i][1], accounts[i][j])

        # 3. go through the keys in parent and start grouping the emails
        groupings = {}
        for email in self.parent.keys():
            root = self.find(email)
            if root not in groupings:
                groupings[root] = [email]
            else:
                groupings[root].append(email)

        # 4. create an answer ready 
        ans = []
        for emails in groupings.values():
            emails.sort()
            name = self.email_name[emails[0]]
            ans.append([name] + emails)

        return ans

    # basic find function

    def find(self, email:str) -> str:
        #recursive function
        if self.parent[email] == email:
            return self.parent[email]
        return self.find(self.parent[email])

    # basic union function
    def union(self, x:str, y:str) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]


        