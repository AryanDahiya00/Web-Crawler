import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import validators

st.title("Web Crawler")
st.sidebar.header("Crawler Settings")
root_url = st.sidebar.text_input("Enter the Root URL", "https://example.com")
depth = st.sidebar.number_input("Depth", min_value=0, max_value=10, value=2)
start_crawl = st.sidebar.button("Start Crawling")

# Web crawler function
def crawl_url(root_url, max_depth):
    crawled_links = []
    visited = set()
    def crawl(current_url, depth):
        if depth > max_depth or current_url in visited:
            return
        visited.add(current_url)

        try:
            response = requests.get(current_url, timeout=5)
            status = f"{response.status_code} {response.reason}"
            crawled_links.append({
                "url": current_url,
                "depth_level": depth,
                "status": status
            })
            
            if response.status_code == 200 and depth < max_depth:
                soup = BeautifulSoup(response.text, "html.parser")
                for link in soup.find_all("a", href=True):
                    next_url = urljoin(current_url, link["href"])
                    if validators.url(next_url) and next_url not in visited:
                        crawl(next_url, depth + 1)
        except requests.RequestException as e:
            crawled_links.append({
                "url": current_url,
                "depth_level": depth,
                "status": "Error: " + str(e)
            })

    # Start crawling from the root URL at depth 0
    crawl(root_url, 0)
    return crawled_links

# Run crawler and display results
if start_crawl:
    if validators.url(root_url):
        with st.spinner("Crawling..."):
            results = crawl_url(root_url, depth)
        if results:
            st.write("## Crawled Links")
            st.table(results)
        else:
            st.warning("No links found.")
    else:
        st.error("Invalid URL format. Please enter a valid URL.")