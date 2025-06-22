🌐 SmartChef — AI-Powered Interactive Recipe Web App
“A smarter way to find, follow, and save recipes — beyond YouTube.”
Cook Smart. Eat Smarter.

📌 Overview
SmartChef is a modern, intelligent web app that allows users to search any recipe by name and instantly get:

✅ Best YouTube tutorial videos.

✅ Blog links with step-by-step instructions.

✅ Auto-scraped instructions.

✅ Option to save recipes to a local database.

✅ A clean, responsive web interface

✅ No need to browse 10 YouTube videos — get only the best

⚙️ Full Feature Set – With How & Why
Feature	How It Works	Why It’s Included
1. Streamlit UI	Built using streamlit — Python web UI framework	Fast, lightweight, mobile-ready UI without frontend coding
2. YouTube API Integration	Uses YouTube Data API v3 to fetch top 3 videos based on the search term	Direct access to high-quality videos, avoids ads, shows title/channel/thumbnail
3. YouTube Thumbnails	Video thumbnails displayed using Pillow + URL fetch	Makes it more interactive and scannable visually
4. Blog Article Scraper	Google search scraped via requests + BeautifulSoup	Fetches cooking blogs without needing an API, shows real step-by-step blogs
5. Recipe Instructions	First paragraph from top DuckDuckGo result scraped and shown	Quick view without needing to visit any page
6. Save to Database	Stored locally in SQLite as structured JSON & text	Allows offline access to favorite recipes
7. Saved Recipes Viewer	Tabbed interface to review saved queries	Organizes data neatly, allows quick reference
8. Streamlit Tabs	Uses st.tabs() to separate Search & Saved tabs	Cleaner user experience, like mobile apps
9. Minimal Dependencies	Only standard libraries and light packages used	Lightweight, quick to set up, no bloat

🔁 How the App Works — Step by Step

1. User enters a recipe name → clicks “Get Recipe”

2. App triggers:
    a. DuckDuckGo search → scrapes first result → extracts text steps
    b. YouTube API → fetches top 3 videos → collects title, channel, thumbnail, link
    c. Google scraping → pulls 3 relevant blog links

3. All info is shown in tabs:
    ✅ Instruction paragraph
    ✅ YouTube video cards (clickable)
    ✅ Blog links (clickable)

4. The data is saved into a local SQLite database.

5. Saved Recipes tab loads recent saved recipes in expandable cards.



🔍 Why Use This Instead of YouTube or Google?
SmartChef	YouTube / Google
✅ Shows top 3 best videos only	❌ You scroll endlessly through dozens
✅ Shows blog links	❌ YouTube doesn’t link to blogs
✅ Shows step-by-step text	❌ You must watch full video
✅ Saves recipe for offline reuse	❌ You lose it if not bookmarked
✅ Clean & fast interface	❌ Distracted by ads/suggestions
✅ All in one tab	❌ Switching between tabs/videos

🟢 SmartChef = YouTube + Blogs + Google Search + Personal Notebook — All in One.

smartchef/
├── streamlit_recipe_book.py      # Your main app
├── requirements.txt              # List of packages (optional but recommended)
├── README.md                     # Description, instructions, etc.
└── recipes_web.db                # (Optional) local DB (can be gitignored)

📦 Technology Stack:
UI/Frontend:-	Streamlit,Pillow,
API Integration:-Google API Client (YouTube),
Web Scraping:-	requests, BeautifulSoup,
Backend Logic:-	Python3,
Local Storage:-	SQLite3, JSON

📥 How to Run This App

pip install streamlit google-api-python-client beautifulsoup4 requests

Then:

Replace the API key:
YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"

Launch the app:
streamlit run streamlit_recipe_book.py

✅ Advantages
Clean, ad-free recipe dashboard

Search + Save + Reuse

Fast to deploy, runs locally

Smart scraping using search engines

Easy to extend with login or export features

Modern feel without frontend code

❌ Limitations
YouTube API key required

Scraping blogs is brittle (format can break)

Instructions might not be 100% complete

No cloud sync or multi-device login

🚀 Potential Future Upgrades
Feature	Purpose
🧾 Export to PDF	Save recipes for printing or sharing
🌐 Deploy to Web	Use Streamlit Cloud / HuggingFace Spaces
🌍 Multi-language support	Use Google Translate API
🔐 User Login	Firebase or Supabase for user accounts
🧑‍🍳 Ingredient filter	Suggest recipes based on fridge ingredients
📊 Dashboard	Most popular searches, cuisine types, etc.

🧠 Ideal For
Students building AI/web apps
Food bloggers organizing content
Anyone wanting a smarter way to cook
A cooking tablet/kitchen screen app
Integrating with voice assistants (next level)





![Screenshot 2025-06-22 123902](https://github.com/user-attachments/assets/c0f45e40-dc61-4d7d-9fc4-7e9bc50c46a3)
![Screenshot 2025-06-22 123800](https://github.com/user-attachments/assets/98d85724-4a6c-49a3-b929-ffc047f4a210)
![Screenshot 2025-06-22 124113](https://github.com/user-attachments/assets/43d731fd-3103-4792-8a7a-16fffbd2e0e2)
![Screenshot 2025-06-22 124012](https://github.com/user-attachments/assets/93deddbf-0ddc-43e6-a086-4ef832beb0cf)

Admin note for you:-
Okay as this project is made just 2 hours and the reason behind this to make this project is I don't know about streamit lib and recently I learned about it so, I want to test my skills by doing. I have learnt many things logics and real cases & function & dealed with errors.So this is what, i made if you like this then star this repo.I will meet you with in next projects.
Happy Learning
Happy Hacking...
