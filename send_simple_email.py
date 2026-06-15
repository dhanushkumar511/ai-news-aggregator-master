from dotenv import load_dotenv
load_dotenv()

from app.database.repository import Repository
from app.services.email import send_email
from datetime import datetime

repo = Repository()

articles = repo.get_articles_without_digest(limit=20)

# Plain text version
body = f"""
AI NEWS DIGEST
Generated: {datetime.now().strftime('%d %b %Y %H:%M')}

==================================================
"""

# HTML version
html_body = f"""
<html>
<body style="font-family: Arial, sans-serif; max-width: 800px; margin: auto;">
<h1>🤖 AI News Digest</h1>
<p><b>Generated:</b> {datetime.now().strftime('%d %b %Y %H:%M')}</p>
<hr>
"""

for i, article in enumerate(articles, start=1):

    title = article.get("title", "No Title")
    url = article.get("url", "#")
    article_type = article.get("type", "Unknown")

    body += f"""

{i}. {title}

Source: {article_type}
Link: {url}

--------------------------------------------------
"""

    html_body += f"""
    <div style="margin-bottom:25px;">
        <h3>{i}. {title}</h3>

        <p>
            <b>Source:</b> {article_type}
        </p>

        <p>
            <a href="{url}" target="_blank">
                Read Article →
            </a>
        </p>

        <hr>
    </div>
    """

html_body += """
</body>
</html>
"""

send_email(
    subject="🤖 AI News Digest",
    body_text=body,
    body_html=html_body
)

print(f"Email sent with {len(articles)} articles!")