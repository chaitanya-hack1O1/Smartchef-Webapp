import streamlit as st
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from PIL import Image
from io import BytesIO
import sqlite3
import json

# YouTube API Key (replace this with your actual API key)
YOUTUBE_API_KEY = "AIzaSyBnSMLJ7vFAUA9QkXs03QRAMpvqlZI2UZs"

# Database file name
DB_NAME = "recipes_web.db"

# ---------------------- Database Initialization ---------------------- #
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            instructions TEXT,
            youtube_links TEXT,
            blog_links TEXT
        )
    """)
    conn.commit()
    conn.close()

# ---------------------- DuckDuckGo Scraping ---------------------- #
def get_duckduckgo_recipe(recipe_name):
    query = f"how to make {recipe_name} recipe"
    url = f"https://duckduckgo.com/html/?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.find_all("a", class_="result__a", limit=1)

    if links:
        href = links[0]['href']
        # Fix URL scheme if missing
        if href.startswith('//'):
            href = 'https:' + href
        elif not href.startswith(('http://', 'https://')):
            href = 'https://' + href
            
        try:
            full_page = requests.get(href, headers=headers, timeout=10)
            full_soup = BeautifulSoup(full_page.text, "html.parser")
            paras = full_soup.find_all("p")
            text = "\n".join([p.get_text() for p in paras[:10]])
            return text, href
        except Exception as e:
            return f"Error fetching recipe: {str(e)}", href
    return "No instructions found.", ""

# ---------------------- YouTube API ---------------------- #
def get_youtube_videos(query):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    req = youtube.search().list(
        part="snippet",
        maxResults=3,
        q=f"{query} recipe",
        type="video"
    )
    res = req.execute()
    videos = []
    for item in res['items']:
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        channel = item['snippet']['channelTitle']
        thumbnail = item['snippet']['thumbnails']['medium']['url']
        videos.append({
            "title": title,
            "channel": channel,
            "thumbnail": thumbnail,
            "url": f"https://www.youtube.com/watch?v={video_id}"
        })
    return videos

# ---------------------- Blog Link Scraping ---------------------- #
def get_blog_links(recipe_name):
    search_url = f"https://www.google.com/search?q={recipe_name}+recipe+blog"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.find_all('a')
        blog_links = []
        for link in links:
            href = link.get('href')
            if href and "/url?q=" in href and "webcache" not in href:
                real_url = href.split("/url?q=")[1].split("&")[0]
                if "http" in real_url:
                    # Fix URL scheme if missing
                    if real_url.startswith('//'):
                        real_url = 'https:' + real_url
                    elif not real_url.startswith(('http://', 'https://')):
                        real_url = 'https://' + real_url
                    blog_links.append(real_url)
            if len(blog_links) >= 3:
                break
        return blog_links
    except Exception as e:
        return [f"Error fetching blog links: {str(e)}"]

# ---------------------- Save Recipe ---------------------- #
def save_recipe(name, instructions, yt_links, blog_links):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO recipes (name, instructions, youtube_links, blog_links) VALUES (?, ?, ?, ?)",
              (name, instructions, json.dumps(yt_links), json.dumps(blog_links)))
    conn.commit()
    conn.close()

# ---------------------- Get Saved Recipes ---------------------- #
def get_saved_recipes():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT name, instructions FROM recipes ORDER BY id DESC LIMIT 10")
    data = c.fetchall()
    conn.close()
    return data

# ---------------------- Streamlit App ---------------------- #
def main():
    st.set_page_config(page_title="Smart Recipe Book", layout="wide")
    st.title("🥗 Smart Recipe Book Web App")

    tabs = st.tabs(["🔍 Search Recipes", "💾 Saved Recipes"])

    # Tab 1: Recipe Search
    with tabs[0]:
        recipe_name = st.text_input("Enter a recipe name", placeholder="e.g., Vada Pav")

        if st.button("Get Recipe"):
            if recipe_name:
                with st.spinner("Fetching recipe..."):
                    instructions, source_url = get_duckduckgo_recipe(recipe_name)
                    yt_videos = get_youtube_videos(recipe_name)
                    blog_links = get_blog_links(recipe_name)
                    save_recipe(recipe_name, instructions, yt_videos, blog_links)

                st.subheader("🍽️ Instructions")
                st.write(instructions)

                st.subheader("🎥 YouTube Videos")
                cols = st.columns(3)
                for i, video in enumerate(yt_videos):
                    with cols[i]:
                        st.image(video['thumbnail'], use_container_width=True)
                        st.markdown(f"[{video['title']}]({video['url']})  \n_Channel: {video['channel']}_")

                st.subheader("📚 Blog Links")
                for link in blog_links:
                    st.markdown(f"[{link}]({link})")
            else:
                st.warning("Please enter a recipe name.")

    # Tab 2: Saved Recipes
    with tabs[1]:
        st.subheader("💾 Recently Saved Recipes")
        recipes = get_saved_recipes()
        if not recipes:
            st.info("No recipes saved yet.")
        for name, instr in recipes:
            with st.expander(name):
                st.write(instr[:400] + "...")


if __name__ == "__main__":
    init_db()
    main()
