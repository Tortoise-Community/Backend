from github import Github
from Tortoise.settings import GITHUB_ACCESS_TOKEN

g = Github(GITHUB_ACCESS_TOKEN)

class git():
    url :str
    full_name: str
    base_url = "https://github.com/"
    commits : str
    stars : str
    collaborators : str
    forks : str
    created_at: str


    def __init__(self,url):
        self.url = url
        self.full_name = url.replace(self.base_url,"")
        repo = g.get_repo(self.full_name)
        self.commits = repo.get_commits().totalCount
        self.stars = repo.stargazers_count
        self.contributors = repo.get_contributors().totalCount
        self.forks = repo.get_forks().totalCount


