from bs4 import BeautifulSoup
import requests




url = "https://github.com/trending"
def request_github_trending(url):
    repos_page = requests.get(url)
    return repos_page




#function to extract page from html parser
def extract(page_):
    soup = BeautifulSoup(page_.text, "html.parser")
    return soup.find_all("article")




#function to transform page
def transform(html_repOs):
    result = []
    for repo in html_repOs:
        # Find repository name
        repo_name_tag = repo.find("a", class_="Link")
        repos_name = repo_name_tag.get_text(strip=True).split("/")[1] if repo_name_tag else "Unknown Repository"

        # Find number of stars
        stars_tag = repo.find("span", class_="d-inline-block float-sm-right")
        nbr_stars = stars_tag.get_text(strip=True) if stars_tag else "0"

        try:
            # Find developer name
            developer_tag = repo.find("span", class_="text-normal")
            developer_name = developer_tag.get_text(strip=True).replace('/', '') if developer_tag else "Unknown Developer"
        except (AttributeError, TypeError):
            developer_name = "Unknown Developer"

        result.append({'developer': developer_name, 'repository_name': repos_name, 'nbr_stars': nbr_stars})
    
    return result


def format(repositories_daTa):
    final_result = []
    for element in repositories_daTa:
        developer = element.get('developer', "")
        repos_name = element.get('repository_name', "")
        stars = element.get('nbr_stars', "")
         # Format the data into a CSV string
        csv_line = f"{developer},{repos_name},{stars}"
        final_result.append(csv_line)
   
    return '\n'.join(final_result)
