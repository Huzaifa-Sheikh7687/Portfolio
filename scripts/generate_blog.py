#!/usr/bin/env python3
"""
Automated AI Blog Generator for Huzaifa Sheikh's Portfolio
100% FREE Workflow:
1. Discovers trending tech topics from Hacker News & tech trends.
2. Uses Google Gemini API (Free tier from Google AI Studio) to generate in-depth, SEO-optimized articles.
3. Uses Pollinations.ai (100% Free AI image generator) to generate and download featured cover images.
4. Prepends the new blog post into `src/data/blogs.json`.
5. Automatically updates `public/sitemap.xml` for Google SEO indexing.
"""

import os
import sys
import json
import re
import ssl
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime

# Setup paths relative to script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_FILE = os.path.join(PROJECT_ROOT, "src", "data", "blogs.json")
IMAGES_DIR = os.path.join(PROJECT_ROOT, "public", "blog-images")
SITEMAP_FILE = os.path.join(PROJECT_ROOT, "public", "sitemap.xml")

# Allow unverified SSL context if user has local corporate/antivirus MITM certs
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


def http_get_json(url, timeout=15):
    """Fetch JSON from a URL using standard library."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AutoBlogBot/1.0"}
    )
    with urllib.request.urlopen(req, timeout=timeout, context=ssl_context) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_trending_topics():
    """Fetch current top tech headlines from Hacker News to discover trending ideas."""
    print("🔍 Fetching trending tech topics from Hacker News...")
    headlines = []
    try:
        top_ids = http_get_json("https://hacker-news.firebaseio.com/v0/topstories.json")[:15]
        for item_id in top_ids[:8]:
            try:
                item = http_get_json(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json")
                if item and "title" in item:
                    headlines.append(item["title"])
            except Exception:
                continue
    except Exception as e:
        print(f"⚠️ Warning: Could not reach Hacker News API ({e}). Using default tech trend signals.")
        headlines = [
            "Agentic AI and autonomous code workflows in 2026",
            "Vector databases vs traditional relational search at scale",
            "Modern React 19 server components and performance gains",
            "Advanced SQL window functions and real-time Power BI ETL",
            "Small Language Models (SLMs) running locally with Ollama and WebGPU"
        ]

    print(f"✅ Discovered {len(headlines)} trending topics.")
    return headlines


def load_existing_blogs():
    """Load existing blog posts from JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Error reading {DATA_FILE}: {e}")
            return []
    return []


def generate_with_gemini(api_key, trending_topics, existing_titles):
    """Generate article content via Google Gemini API (Free tier)."""
    print("🤖 Calling Google Gemini API to write high quality technical blog...")

    models = [
        "gemini-2.5-flash",
        "gemini-3.8-flash",
        "gemini-flash-latest",
        "gemini-2.0-flash",
        "gemini-1.5-flash"
    ]
    
    prompt = f"""
You are writing a top-tier technical blog article for Huzaifa Sheikh's portfolio website.
Huzaifa is a Data Analyst, Data Scientist, and AI Engineer with deep expertise in Python, SQL, Power BI, React, and Machine Learning.

Current trending tech topics and headlines:
{json.dumps(trending_topics, indent=2)}

Existing blog titles (DO NOT REPEAT OR DUPLICATE THESE TOPICS):
{json.dumps(existing_titles, indent=2)}

TASK:
Pick ONE highly relevant, trending, and practical tech topic in Artificial Intelligence, Machine Learning, Data Analytics, or Full-Stack Engineering.
Write an authoritative, engaging, in-depth technical blog post (approx 700 to 1200 words).

FORMAT:
Respond ONLY with a valid JSON object with the following schema:
{{
  "title": "A catchy, authoritative, SEO-optimized title",
  "slug": "kebab-case-url-slug-without-special-characters",
  "category": "Artificial Intelligence" (choose one of: Artificial Intelligence, Data Science, Data Analytics, Web Development, Cloud & DevOps, Machine Learning),
  "tags": ["Tag1", "Tag2", "Tag3", "Tag4"],
  "readTime": "6 min read",
  "excerpt": "A compelling 2-sentence hook and summary that makes readers click.",
  "metaTitle": "SEO title under 60 chars",
  "metaDescription": "SEO meta description between 140-160 chars with main keywords.",
  "keywords": "comma, separated, high, traffic, keywords",
  "imagePrompt": "A futuristic, clean, cyberpunk/tech minimal 3D digital illustration prompt for the article banner. No text on image.",
  "content": "Full markdown content starting with ## headers. Include practical architecture explanations, bullet points, real-world case studies, and at least one code snippet (Python, SQL, or JS) formatted with markdown code blocks. Keep tone professional yet approachable."
}}
"""

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "topP": 0.95,
            "responseMimeType": "application/json"
        }
    }

    last_error = None
    for model in models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=45, context=ssl_context) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                text_content = data["candidates"][0]["content"]["parts"][0]["text"]
                return json.loads(text_content)
        except Exception as e:
            last_error = e
            print(f"⚠️ Model {model} attempt failed ({e}). Trying next model...")
            time.sleep(2)

    raise RuntimeError(f"All Gemini models failed: {last_error}")


def generate_fallback_blog(existing_slugs):
    """Pre-curated rotation fallback if API key is missing during local dry runs."""
    fallback_pool = [
        {
            "title": "Building Production RAG with Hybrid Search & Re-ranking in Python",
            "slug": "production-rag-hybrid-search-reranking",
            "category": "Artificial Intelligence",
            "tags": ["RAG", "Vector Search", "Python", "LLMs", "NLP"],
            "readTime": "7 min read",
            "excerpt": "Why basic vector search fails in production, and how combining BM25 keyword matching with cross-encoder re-rankers yields 40% higher retrieval precision.",
            "metaTitle": "Production RAG with Hybrid Search & Re-ranking | Huzaifa Sheikh",
            "metaDescription": "Master production Retrieval-Augmented Generation (RAG) using hybrid dense-sparse search and Cohere/HuggingFace re-rankers.",
            "keywords": "RAG, Hybrid Search, BM25, Vector Database, Python, LLM",
            "imagePrompt": "Futuristic glowing holographic neural network connecting documents in a clean cybernetic server room, 3d render, octane render, 8k",
            "content": """## The Limits of Naive Vector Search\n\nRetrieval-Augmented Generation (RAG) is the backbone of enterprise LLM applications. However, most developers start with a naive pipeline: chunk documents, embed with an off-the-shelf model, store in a vector database, and retrieve top-$k$ by cosine similarity.\n\nIn real enterprise scenarios, this naive approach suffers from three major flaws:\n1. **Keyword Blindness:** Vector embeddings struggle with exact part numbers, product SKUs, and unique acronyms.\n2. **Context Fragmentation:** Fixed chunking splits vital tabular data across chunk boundaries.\n3. **Ranking Inaccuracy:** Cosine similarity measures topical closeness, not factual answer relevance.\n\n---\n\n## The Solution: Hybrid Search Architecture\n\nProduction-grade RAG blends two complementary search paradigms:\n- **Dense Retrieval (Semantic):** Uses high-dimensional vectors to capture contextual semantics and synonyms.\n- **Sparse Retrieval (Lexical):** Uses BM25 or SPLADE algorithms to guarantee exact token and keyword matches.\n\n```python\n# Hybrid Search Fusion with Reciprocal Rank Fusion (RRF)\ndef reciprocal_rank_fusion(dense_ranks, sparse_ranks, k=60):\n    rrf_scores = {}\n    for rank, doc_id in enumerate(dense_ranks):\n        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1.0 / (k + rank)\n    for rank, doc_id in enumerate(sparse_ranks):\n        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1.0 / (k + rank)\n    return sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)\n```\n\n---\n\n## Adding a Cross-Encoder Re-ranker\n\nOnce top candidates are retrieved via hybrid fusion, pass the top 25 candidates through a lightweight cross-encoder model (e.g. `bge-reranker-large`). Unlike bi-encoders that process query and document independently, cross-encoders perform full cross-attention across both, boosting answer accuracy by up to 35%.\n\n## Conclusion\n\nTransitioning from demo RAG to production reliability requires disciplined search engineering. Implementing hybrid search and cross-encoder re-ranking gives your LLMs the exact grounding data they need without hallucination."""
        },
        {
            "title": "Optimizing High-Volume SQL Pipelines for Real-Time Power BI Dashboards",
            "slug": "optimizing-sql-pipelines-powerbi-dashboards",
            "category": "Data Analytics",
            "tags": ["SQL", "Power BI", "Data Modeling", "ETL", "Performance"],
            "readTime": "5 min read",
            "excerpt": "Learn how indexing strategies, query pushdown, and VertiPaq compression transform slow 30-second Power BI report refreshes into sub-second interactions.",
            "metaTitle": "Optimizing SQL for Power BI Reports | Huzaifa Sheikh",
            "metaDescription": "Techniques for accelerating SQL transformations and DAX calculations in Power BI business reporting.",
            "keywords": "SQL Optimization, Power BI, DAX, Data Modeling, Star Schema",
            "imagePrompt": "Modern glowing data analytics dashboard hovering in clean modern high-tech workspace, abstract data streams, 3d minimal render",
            "content": """## The Bottleneck: Slow BI Refreshes\n\nWhen executive dashboards take 30+ seconds to load, user adoption plummets. In 90% of cases, the culprit is not Power BI itself, but inefficient upstream SQL queries and unoptimized dimensional models.\n\n---\n\n## Key Optimization Pillars\n\n1. **Push Filtering to Database Layer:** Never pull million-row tables into memory when a pre-aggregated view can deliver the exact needed metrics.\n2. **Avoid Bi-Directional Cross-Filtering:** Keep all relationships single-direction in a strict Star Schema.\n3. **Use Integer Surrogate Keys:** VertiPaq dictionary encoding compresses integers far better than string GUIDs.\n\n## Summary\n\nA performant dashboard is built in SQL before a single visual is created in Power BI."""
        }
    ]

    for item in fallback_pool:
        if item["slug"] not in existing_slugs:
            return item

    # If all existing, append timestamp to make unique
    res = fallback_pool[0].copy()
    ts = int(time.time())
    res["slug"] = f"{res['slug']}-{ts}"
    res["title"] = f"{res['title']} ({datetime.now().strftime('%B %Y')})"
    return res


def download_ai_image(prompt, slug):
    """
    Generate and download AI cover image using Pollinations.ai (100% FREE, no API key needed).
    Saves image into public/blog-images/{slug}.jpg
    """
    print(f"🎨 Generating AI cover image with Pollinations.ai for: {slug}...")
    os.makedirs(IMAGES_DIR, exist_ok=True)
    image_filename = f"{slug}.jpg"
    target_path = os.path.join(IMAGES_DIR, image_filename)

    # Encode prompt for URL
    clean_prompt = re.sub(r'[^a-zA-Z0-9\s,]', '', prompt)[:200]
    encoded_prompt = urllib.parse.quote(f"futuristic tech editorial illustration, {clean_prompt}, octane render, vibrant, 8k, photorealistic, sharp focus")
    pollinations_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1200&height=630&nologo=true&model=flux"

    try:
        req = urllib.request.Request(
            pollinations_url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AutoBlogBot/1.0"}
        )
        with urllib.request.urlopen(req, timeout=35, context=ssl_context) as resp:
            content_type = resp.headers.get("Content-Type", "")
            data = resp.read()
            if len(data) > 5000:  # Valid image payload
                with open(target_path, "wb") as f:
                    f.write(data)
                print(f"✅ AI Cover Image downloaded successfully: /blog-images/{image_filename} ({len(data)} bytes)")
                return f"/blog-images/{image_filename}"
    except Exception as e:
        print(f"⚠️ Image generation warning: {e}. Using curated high-res tech fallback.")

    # High quality tech fallback cover image
    return "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80"


def update_sitemap(blogs):
    """Generate and update public/sitemap.xml for Google SEO indexing."""
    print("🗺️ Updating public/sitemap.xml for search engines...")
    today = datetime.now().strftime("%Y-%m-%d")
    base_url = "https://huzaifa-sheikh-portfolio.vercel.app"

    urls_xml = [
        f"""  <url>
    <loc>{base_url}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""",
        f"""  <url>
    <loc>{base_url}/#blogs</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>"""
    ]

    for b in blogs:
        slug = b.get("slug")
        if slug:
            urls_xml.append(f"""  <url>
    <loc>{base_url}/#blog-{slug}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls_xml)}
</urlset>
"""
    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("✅ Sitemap updated with all blog posts.")


def main():
    print("🚀 Starting Automated Daily Blog Generation Workflow...")
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()

    existing_blogs = load_existing_blogs()
    existing_titles = [b.get("title", "") for b in existing_blogs]
    existing_slugs = [b.get("slug", "") for b in existing_blogs]

    trending_topics = fetch_trending_topics()

    if api_key:
        try:
            blog_data = generate_with_gemini(api_key, trending_topics, existing_titles)
        except Exception as e:
            print(f"❌ Gemini generation failed ({e}). Falling back to curated post.")
            blog_data = generate_fallback_blog(existing_slugs)
    else:
        print("ℹ️ GEMINI_API_KEY environment variable not set. Running in test/fallback mode.")
        blog_data = generate_fallback_blog(existing_slugs)

    # Sanitize slug
    slug = re.sub(r'[^a-zA-Z0-9-]', '', blog_data.get("slug", "").lower().replace(" ", "-"))
    if not slug:
        slug = f"article-{int(time.time())}"

    # Generate/download cover image
    cover_image = download_ai_image(blog_data.get("imagePrompt", blog_data.get("title", "")), slug)

    # Build final blog record
    new_post = {
        "id": str(int(time.time())),
        "slug": slug,
        "title": blog_data.get("title", "Untitled Technical Deep Dive"),
        "excerpt": blog_data.get("excerpt", ""),
        "category": blog_data.get("category", "Artificial Intelligence"),
        "tags": blog_data.get("tags", ["AI", "Tech"]),
        "date": datetime.now().strftime("%B %d, %Y"),
        "readTime": blog_data.get("readTime", "5 min read"),
        "coverImage": cover_image,
        "author": {
            "name": "Huzaifa Sheikh",
            "role": "Data Analyst & AI Engineer",
            "avatar": "https://github.com/Huzaifa-Sheikh7687.png"
        },
        "seo": {
            "metaTitle": blog_data.get("metaTitle", f"{blog_data.get('title')} | Huzaifa Sheikh"),
            "metaDescription": blog_data.get("metaDescription", blog_data.get("excerpt", "")),
            "keywords": blog_data.get("keywords", "AI, Data Science, Huzaifa Sheikh")
        },
        "content": blog_data.get("content", "")
    }

    # Prepend to blogs list
    existing_blogs.insert(0, new_post)

    # Save to src/data/blogs.json
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(existing_blogs, f, indent=2, ensure_ascii=False)

    print(f"🎉 New blog post published: '{new_post['title']}' (slug: {new_post['slug']})")

    # Update sitemap
    update_sitemap(existing_blogs)

    print("🏁 Auto-blog workflow completed successfully!")


if __name__ == "__main__":
    main()
