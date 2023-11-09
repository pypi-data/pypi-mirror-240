from github import Github, Auth
import os

class GithubService:

    def __init__(self):
        self.auth = self.authenticate()

    def authenticate(self):
        token = os.getenv("GITHUB_TOKEN")
        auth = Auth.Token(token)
        return auth
    
    def get_repos(self):
        gh = Github(auth=self.auth)
        # with open("repos.json", "w+") as f:
        #     data = json.loads(gh.get_user().get_repos())
        #     f.write(data)
        return [repo for repo in gh.get_user().get_repos() if repo.language == "PHP"]
    
    
