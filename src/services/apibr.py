import requests
import os

from dotenv import load_dotenv

load_dotenv()

class JobService:
    def __init__(self):
        self.base_url = "https://apibr.com/vagas/api/v1/"

    def get_jobs(self, technology, per_page=3, page=1):
        try:
            technology = self.clen_tech(technology)
            url = self.base_url + f"issues?page={page}&per_page={per_page}&term={technology}"
            headers = {
                "User-Agent": os.getenv("USER_AGENT"),
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                jobs = []
                for item in data:
                    job = {
                        "title": item["title"],
                        "url": item["url"],
                        "keywords": item["keywords"],
                        "created_at": item["created_at"],
                        "author": item["user"]["login"],
                        "author_url": item["user"]["url"],
                        "url_avatar": item["user"]["avatar_url"],
                        "repository": item["repository"]["full_name"],
                        "org_avatar": item["repository"]["organization"]["avatar_url"],
                    }
                    jobs.append(job)
                return jobs
            else:
                return None
        except Exception as e:
            print("An error occurred:", str(e))
            return None

    def clen_tech(self, technology):
        technology = technology.translate(str.maketrans("", "", " -"))
        technology = technology.lower()
        return technology
