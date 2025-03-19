from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def health_check(request):
    return Response({'Status': 'Working'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def hello_world(request):
    return Response({'Message': 'Hello world!'}, status=status.HTTP_200_OK)


import json
import random
import requests
from playwright.sync_api import sync_playwright


proxy_list = [{'server': 'dc.oxylabs.io:8000', 'username': 'naveen_kY5lG', 'password': 'ea8vWq+NiqjurjkQ'}, {'server': 'dc.oxylabs.io:8000', 'username': 'Gudbadugly_0cqzZ', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'ihubsns_zQVFs', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'Testing_LoNLf', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'HarisankarJ_a5Nj2', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'akash_tNgmM', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'Akilihub_Gy3Z1', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'mugilan_eGYDD', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'RNS_Sanjay_MZyzH', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'lathees_6pZh3', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'shruthi_1vvlk', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'kavin_bakyaraj_5cQ3F', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'Ajay_Chakravarthi_B5RJy', 'password': 'SNS+ihub=123'}]

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.120 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
]

def get_random_proxy(proxy_list,user_agent_list):

    proxy_now = random.choice(proxy_list)

    user_agent = random.choice(user_agent_list)
    try :

        username = proxy_now["username"]
        password = proxy_now["password"]
        proxy = proxy_now["server"]

        print(username,password,proxy)

        proxies = {
        "https": ('https://user-%s:%s@%s' % (username, password, proxy))
        }

        response=requests.get("https://ip.oxylabs.io/location", proxies=proxies)
        if response.status_code == 200:
            return proxy_now,user_agent
        else:
            get_random_proxy(proxy_list.pop(proxy_list.index(proxy_now)))
    except Exception as e:
        print(e)
        get_random_proxy(proxy_list.pop(proxy_list.index(proxy_now)))


def setup_browser():
    playwright = sync_playwright().start()

    proxy_list = [{'server': 'dc.oxylabs.io:8000', 'username': 'naveen_kY5lG', 'password': 'ea8vWq+NiqjurjkQ'}, {'server': 'dc.oxylabs.io:8000', 'username': 'Gudbadugly_0cqzZ', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'ihubsns_zQVFs', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'Testing_LoNLf', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'HarisankarJ_a5Nj2', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'akash_tNgmM', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'Akilihub_Gy3Z1', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'mugilan_eGYDD', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'RNS_Sanjay_MZyzH', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'lathees_6pZh3', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'shruthi_1vvlk', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'kavin_bakyaraj_5cQ3F', 'password': 'SNS+ihub=123'}, {'server': 'dc.oxylabs.io:8000', 'username': 'Ajay_Chakravarthi_B5RJy', 'password': 'SNS+ihub=123'}]

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.120 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
    ]

    #proxy,user_agent = get_random_proxy(proxy_list,user_agent_list)

    #print(proxy,user_agent)

    #browser = playwright.chromium.launch(headless=True,
      #                                   proxy=proxy)
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(user_agent=user_agent)
    return playwright, browser, page

def freelancer_scrapper(search_query):
    playwright, browser, page = setup_browser()
    jobs = []

    try:
        page.goto(f"https://www.freelancer.com/jobs/?keyword={search_query}&results=20", timeout=60000)
        if "freelancer.com" not in page.url:
            raise Exception("Failed to load Freelancer.com jobs page")
        
        print(page.url)

        page.wait_for_selector("//input[@id='keyword-input']", timeout=60000)
        search_box = page.locator("//input[@id='keyword-input']")

        if not search_box.is_visible() or not search_box.is_enabled():
            raise Exception("Search input field not interactable")

        # search_box.fill(search_query)
        search_box.press("Enter")
        page.wait_for_timeout(5000)

        while True:  # Pagination loop
            
            job_cards = page.locator(".JobSearchCard-item").all()
            if not job_cards:
                print("No job listings found on the page")
                break

            for card in job_cards:
                try:
                    title_elem = card.locator(".JobSearchCard-primary-heading-link")
                    title = title_elem.inner_text().strip() if title_elem.count() > 0 else "N/A"
                    link = title_elem.get_attribute("href") if title_elem.count() > 0 else None
                    if link and not link.startswith("http"):
                        link = f"https://www.freelancer.com{link}"

                    print(link)

                    desc_elem = card.locator(".JobSearchCard-primary-description")
                    description = desc_elem.inner_text().strip() if desc_elem.count() > 0 else "N/A"
                    truncated_description = description.replace("\n", " ")

                    budget_elem = card.locator(".JobSearchCard-primary-price")
                    budget = budget_elem.inner_text().strip().replace(" ","") if budget_elem.count() > 0 else "N/A"

                    proposal_elem = card.locator(".JobSearchCard-secondary-price")
                    proposals = proposal_elem.inner_text().strip().replace(" ","") if budget_elem.count() > 0 else "N/A"

                    skills_elem = card.locator(".JobSearchCard-primary-tags")
                    skills = skills_elem.inner_text().strip() if skills_elem.count() > 0 else "N/A"

                    post_ends = card.locator(".JobSearchCard-primary-heading-days")
                    post_ends = post_ends.inner_text().strip() if post_ends else "N/A"

                    posted_time = "N/A"



                    job_data = {
                        "title": title,
                        "link": link,
                        "description": truncated_description,
                        "full_description": truncated_description,
                        "budget": budget,
                        "posted_time": posted_time,
                        'proposals' : proposals,
                        "status": "Open",
                        "post_ends": post_ends,
                        "skills": skills,
                        "keyword": search_query,
                        "platform": "freelancer.com"
                    }

                    jobs.append(job_data)

                    # break

                except Exception as e:
                    print(f"Error processing individual job: {e}")
                    continue


            # Check for next page and navigate
            next_button = page.locator("a[data-link='next_page']")
            if next_button.count() > 0 and next_button.is_enabled():
                next_button.click()
                page.wait_for_timeout(5000)  # Wait for page to load
                print(f"Moving to next page. Current job count: {len(jobs)}")
            else:
                print("No more pages to scrape")
                break

        print(f"Successfully scraped {len(jobs)} jobs for query: '{search_query}'")

        with open("freelancer_jo.json", "w") as f:
            json.dump(jobs, f, indent=2)

    except Exception as e:
        print(f"Scraping error: {e}")
        if 'page' in locals():
            print(f"Current URL: {page.url}")
            print(f"Page title: {page.title()}")

    finally:
        try:
            browser.close()
            playwright.stop()
        except Exception as e:
            print(f"Error during cleanup: {e}")

    print(jobs)
    return jobs

@api_view(['POST'])
def perform_scrapping(request):
    search_query = request.data.get("search_query")
    if not search_query:
        return Response({'error': 'Please provide a search query'}, status=status.HTTP_400_BAD_REQUEST)

    jobs = freelancer_scrapper(search_query)
    return Response({'jobs': jobs}, status=status.HTTP_200_OK)
