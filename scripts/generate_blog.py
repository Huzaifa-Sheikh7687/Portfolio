#!/usr/bin/env python3
"""
Automated Data Science & Machine Learning Blog Generator for Huzaifa Sheikh's Portfolio
100% FREE Workflow:
1. Discovers trending Data Science & ML topics.
2. Uses Google Gemini API (Free tier from Google AI Studio) to generate student/professional/industrial level articles.
3. Generates high-resolution architectural SVG infographics (matching Ghufran Naseer's reference design).
4. Prepends the new blog post into `src/data/blogs.json` (latest is always on the left in the horizontal slider).
5. Automatically updates `public/sitemap.xml` for Google SEO indexing.
"""

import os
import sys
import json
import re
import ssl
import time
import html
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
    print("🔍 Fetching trending Data Science & ML topics from Hacker News...")
    headlines = []
    try:
        top_ids = http_get_json("https://hacker-news.firebaseio.com/v0/topstories.json")[:20]
        for item_id in top_ids[:10]:
            try:
                item = http_get_json(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json")
                if item and "title" in item:
                    title = item["title"]
                    # Prioritize AI, Data, and ML signals
                    if any(k in title.lower() for k in ["ai", "data", "model", "learning", "gpu", "rag", "sql", "analytics", "vector"]):
                        headlines.append(title)
            except Exception:
                continue
    except Exception as e:
        print(f"⚠️ Warning: Could not reach Hacker News API ({e}). Using default tech trend signals.")

    if not headlines:
        headlines = [
            "Feature store architectures for low-latency production ML inference",
            "High-dimensional vector search: HNSW vs IVF-PQ benchmarks",
            "Continuous model monitoring with Kolmogorov-Smirnov and PSI metrics",
            "Parameter-efficient LLM adaptation with QLoRA and FlashAttention-2",
            "Advanced time-series forecasting with DeepAR and Temporal Fusion Transformers"
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


def generate_svg_infographic(filename, category, title, subtitle, cards, quote, tags, config_name, metrics):
    """
    Renders an industrial-grade dark-mode architecture infographic matching the reference design.
    """
    os.makedirs(IMAGES_DIR, exist_ok=True)
    safe_title = html.escape(title)
    safe_subtitle = html.escape(subtitle)
    safe_category = html.escape(category.upper())
    safe_quote = html.escape(quote)
    safe_config = html.escape(config_name)

    words = safe_title.split()
    line1, line2 = "", ""
    if len(words) > 5:
        mid = len(words) // 2
        line1 = " ".join(words[:mid])
        line2 = " ".join(words[mid:])
    else:
        line1 = safe_title

    cards_xml = []
    card_y = 230
    for i, c in enumerate(cards[:3]):
        icon_symbol = c.get("icon", "⚡")
        c_title = html.escape(c.get("title", ""))
        c_desc = html.escape(c.get("desc", ""))
        cards_xml.append(f"""
        <g transform="translate(60, {card_y + i * 68})">
            <rect width="480" height="56" rx="10" fill="#0F172A" fill-opacity="0.8" stroke="#1E293B" stroke-width="1.2"/>
            <rect x="12" y="12" width="32" height="32" rx="8" fill="#1E293B" fill-opacity="0.6"/>
            <text x="28" y="33" font-family="'JetBrains Mono', monospace" font-size="14" fill="#38BDF8" text-anchor="middle">{icon_symbol}</text>
            <text x="56" y="27" font-family="'Space Grotesk', sans-serif" font-weight="600" font-size="14" fill="#F8FAFC">{c_title}</text>
            <text x="56" y="44" font-family="'Inter', sans-serif" font-size="11" fill="#94A3B8">{c_desc}</text>
        </g>
        """)

    metrics_xml = []
    m_y = 110
    for i, (k, v, color) in enumerate(metrics[:4]):
        safe_k = html.escape(k)
        safe_v = html.escape(v)
        metrics_xml.append(f"""
        <g transform="translate(30, {m_y + i * 54})">
            <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="13" fill="#94A3B8">{safe_k}</text>
            <text x="360" y="0" font-family="'JetBrains Mono', monospace" font-weight="600" font-size="14" fill="{color}" text-anchor="end">{safe_v}</text>
            <line x1="0" y1="18" x2="360" y2="18" stroke="#1E293B" stroke-width="1" stroke-dasharray="3 3"/>
        </g>
        """)

    tags_xml = []
    tx = 60
    for t in tags[:4]:
        st = html.escape(t)
        tags_xml.append(f"""
        <rect x="{tx}" y="490" width="{len(st) * 8 + 26}" height="24" rx="12" fill="#1E293B" fill-opacity="0.7" stroke="#334155" stroke-width="0.8"/>
        <text x="{tx + 13}" y="506" font-family="'JetBrains Mono', monospace" font-size="11" fill="#7DD3FC">• {st}</text>
        """)
        tx += len(st) * 8 + 36

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#080E1A" />
            <stop offset="50%" stop-color="#0F172A" />
            <stop offset="100%" stop-color="#050B14" />
        </linearGradient>
        <radialGradient id="glow" cx="20%" cy="30%" r="50%">
            <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.15" />
            <stop offset="100%" stop-color="#38BDF8" stop-opacity="0" />
        </radialGradient>
        <radialGradient id="glowRight" cx="80%" cy="40%" r="60%">
            <stop offset="0%" stop-color="#818CF8" stop-opacity="0.12" />
            <stop offset="100%" stop-color="#818CF8" stop-opacity="0" />
        </radialGradient>
        <pattern id="gridDots" x="0" y="0" width="30" height="30" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="1" fill="#334155" fill-opacity="0.3" />
        </pattern>
        <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FFFFFF" />
            <stop offset="60%" stop-color="#38BDF8" />
            <stop offset="100%" stop-color="#818CF8" />
        </linearGradient>
    </defs>

    <rect width="1200" height="630" fill="url(#bgGrad)" />
    <rect width="1200" height="630" fill="url(#glow)" />
    <rect width="1200" height="630" fill="url(#glowRight)" />
    <rect width="1200" height="630" fill="url(#gridDots)" />

    <line x1="60" y1="50" x2="1140" y2="50" stroke="#1E293B" stroke-width="1.5" />
    <text x="60" y="40" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="600" fill="#38BDF8" letter-spacing="2">— {safe_category} ARCHITECTURE • 2026</text>
    <text x="1140" y="40" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="500" fill="#64748B" text-anchor="end">PRODUCTION DEPLOYED</text>

    <text x="60" y="95" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="34" fill="url(#titleGrad)">{line1}</text>
    {"<text x='60' y='135' font-family=\"'Space Grotesk', sans-serif\" font-weight='700' font-size='34' fill='url(#titleGrad)'>" + line2 + "</text>" if line2 else ""}
    <text x="60" y="{170 if line2 else 135}" font-family="'Inter', sans-serif" font-size="15" fill="#94A3B8">{safe_subtitle}</text>

    {"".join(cards_xml)}

    <g transform="translate(60, 440)">
        <rect x="0" y="0" width="4" height="34" fill="#818CF8" rx="2" />
        <text x="16" y="16" font-family="'Inter', sans-serif" font-style="italic" font-size="12" fill="#CBD5E1">\"{safe_quote}\"</text>
        <text x="16" y="32" font-family="'Inter', sans-serif" font-size="10" font-weight="600" fill="#64748B">PRODUCTION BEST PRACTICE</text>
    </g>

    {"".join(tags_xml)}

    <g transform="translate(640, 190)">
        <rect width="500" height="330" rx="16" fill="#090E17" fill-opacity="0.9" stroke="#1E293B" stroke-width="1.5" />
        <rect width="500" height="42" rx="16" fill="#0F172A" />
        <rect y="26" width="500" height="16" fill="#0F172A" />
        <line x1="0" y1="42" x2="500" y2="42" stroke="#1E293B" stroke-width="1" />

        <circle cx="24" cy="21" r="5" fill="#EF4444" />
        <circle cx="40" cy="21" r="5" fill="#F59E0B" />
        <circle cx="56" cy="21" r="5" fill="#10B981" />

        <text x="76" y="25" font-family="'JetBrains Mono', monospace" font-size="12" fill="#94A3B8">{safe_config}</text>

        <rect x="420" y="11" width="60" height="20" rx="6" fill="#064E3B" stroke="#059669" stroke-width="0.8" />
        <text x="450" y="24" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#34D399" text-anchor="middle">STABLE</text>

        <g transform="translate(20, 20)">
            {"".join(metrics_xml)}
        </g>
    </g>

    <line x1="60" y1="570" x2="1140" y2="570" stroke="#1E293B" stroke-width="1" />
    <text x="60" y="595" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748B" letter-spacing="1.5">DATA SCIENCE &amp; ML SYSTEMS</text>
    <text x="600" y="595" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#94A3B8" text-anchor="middle">Huzaifa Sheikh • Engineering Deep-Dive</text>
    <text x="1140" y="595" font-family="'JetBrains Mono', monospace" font-size="11" fill="#38BDF8" text-anchor="end">huzaifa-sheikh-portfolio.vercel.app</text>
</svg>"""

    filepath = os.path.join(IMAGES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print(f"✅ Generated architectural infographic: {filename}")
    return f"/blog-images/{filename}"


def generate_with_gemini(api_key, trending_topics, existing_titles):
    """Generate article content strictly for Data Science & Machine Learning via Google Gemini API."""
    print("🤖 Calling Google Gemini API for industrial Data Science / Machine Learning topic...")

    models = [
        "gemini-2.5-flash",
        "gemini-3.8-flash",
        "gemini-flash-latest",
        "gemini-2.0-flash",
        "gemini-1.5-flash"
    ]
    
    prompt = f"""
You are writing a top-tier industrial Data Science and Machine Learning technical article for Huzaifa Sheikh's portfolio website.
Huzaifa is a Data Analyst and AI Engineer with expertise in Python, Machine Learning, Deep Learning, SQL, Power BI, and MLOps.

Current trending tech signals:
{json.dumps(trending_topics, indent=2)}

Existing blog titles (DO NOT DUPLICATE OR OVERLAP):
{json.dumps(existing_titles, indent=2)}

TASK:
Pick ONE practical, high-value topic strictly in DATA SCIENCE, MACHINE LEARNING, DEEP LEARNING, or MLOps (student, professional, and industrial grade level).
Examples:
- Distributed training with PyTorch FSDP
- Real-time time series anomaly detection
- Vector embeddings and Approximate Nearest Neighbor index scaling
- Graph Neural Networks for fraud detection
- Feature store architectures & time-travel joins
- Model quantization (AWQ vs GPTQ vs GGUF)

FORMAT:
Respond ONLY with a valid JSON object matching this schema:
{{
  "title": "A catchy, authoritative, industrial title",
  "slug": "kebab-case-slug-without-special-characters",
  "category": "Machine Learning" (choose one of: Machine Learning, Data Science, Deep Learning, MLOps),
  "tags": ["Tag1", "Tag2", "Tag3", "Tag4"],
  "readTime": "6 min read",
  "excerpt": "A compelling 2-sentence hook and summary.",
  "metaTitle": "SEO title under 60 chars | Huzaifa Sheikh",
  "metaDescription": "SEO meta description under 160 chars.",
  "keywords": "comma, separated, keywords",
  "infographic": {{
    "subtitle": "Short 1-line architecture subtitle",
    "quote": "A punchy engineering takeaway quote",
    "config_name": "pipeline-spec.yaml",
    "card1_title": "Component 1 Title",
    "card1_desc": "Component 1 explanation",
    "card2_title": "Component 2 Title",
    "card2_desc": "Component 2 explanation",
    "card3_title": "Component 3 Title",
    "card3_desc": "Component 3 explanation",
    "metric1_name": "p99-latency",
    "metric1_val": "12.4ms",
    "metric2_name": "throughput-qps",
    "metric2_val": "4,200 req/s",
    "metric3_name": "cache-hit-rate",
    "metric3_val": "99.2%",
    "metric4_name": "eval-score",
    "metric4_val": "96.4%"
  }},
  "content": "Full markdown content starting with ## headers. Include practical architecture explanations, tables, bullet points, real-world case studies, and Python/SQL code snippets formatted in markdown. Tone: Senior Data Scientist / ML Engineer."
}}
"""

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
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
    print("🚀 Starting Automated Daily Data Science & ML Blog Generator...")
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()

    existing_blogs = load_existing_blogs()
    existing_titles = [b.get("title", "") for b in existing_blogs]

    trending_topics = fetch_trending_topics()

    if not api_key:
        print("ℹ️ GEMINI_API_KEY not set. Running in dry-run mode.")
        return

    try:
        blog_data = generate_with_gemini(api_key, trending_topics, existing_titles)
    except Exception as e:
        print(f"❌ Gemini generation error: {e}")
        return

    slug = re.sub(r'[^a-zA-Z0-9-]', '', blog_data.get("slug", "").lower().replace(" ", "-"))
    if not slug:
        slug = f"ds-ml-{int(time.time())}"

    # Generate architectural SVG infographic
    info = blog_data.get("infographic", {})
    svg_filename = f"{slug}.svg"
    cover_image = generate_svg_infographic(
        filename=svg_filename,
        category=blog_data.get("category", "Machine Learning"),
        title=blog_data.get("title", "Industrial ML Architecture"),
        subtitle=info.get("subtitle", "Production Machine Learning and Data Science Deep-Dive"),
        cards=[
            {"icon": "⚡", "title": info.get("card1_title", "Ingestion Engine"), "desc": info.get("card1_desc", "High-throughput streaming pipeline")},
            {"icon": "🛡️", "title": info.get("card2_title", "Model Serving"), "desc": info.get("card2_desc", "Optimized low-latency inference")},
            {"icon": "📊", "title": info.get("card3_title", "Validation & Drift"), "desc": info.get("card3_desc", "Statistical metric monitoring")}
        ],
        quote=info.get("quote", "Production ML is 90% engineering rigor and 10% model tuning."),
        tags=blog_data.get("tags", ["DataScience", "MLOps"]),
        config_name=info.get("config_name", "mlops-pipeline.yaml"),
        metrics=[
            (info.get("metric1_name", "p99-latency"), info.get("metric1_val", "14.2ms"), "#34D399"),
            (info.get("metric2_name", "throughput"), info.get("metric2_val", "4,850 req/s"), "#38BDF8"),
            (info.get("metric3_name", "cache-hit-rate"), info.get("metric3_val", "99.1%"), "#34D399"),
            (info.get("metric4_name", "eval-accuracy"), info.get("metric4_val", "96.8%"), "#C084FC")
        ]
    )

    new_post = {
        "id": str(int(time.time())),
        "slug": slug,
        "title": blog_data.get("title", "Untitled Deep-Dive"),
        "excerpt": blog_data.get("excerpt", ""),
        "category": blog_data.get("category", "Machine Learning"),
        "tags": blog_data.get("tags", ["Machine Learning", "Data Science"]),
        "date": datetime.now().strftime("%B %d, %Y"),
        "readTime": blog_data.get("readTime", "6 min read"),
        "coverImage": cover_image,
        "author": {
            "name": "Huzaifa Sheikh",
            "role": "Data Analyst & AI Engineer",
            "avatar": "https://github.com/Huzaifa-Sheikh7687.png"
        },
        "seo": {
            "metaTitle": blog_data.get("metaTitle", f"{blog_data.get('title')} | Huzaifa Sheikh"),
            "metaDescription": blog_data.get("metaDescription", blog_data.get("excerpt", "")),
            "keywords": blog_data.get("keywords", "Data Science, Machine Learning, Huzaifa Sheikh")
        },
        "content": blog_data.get("content", "")
    }

    # Prepend new post (so latest is always at index 0, on the left of slider)
    existing_blogs.insert(0, new_post)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(existing_blogs, f, indent=2, ensure_ascii=False)

    print(f"🎉 New blog post published: '{new_post['title']}' (slug: {new_post['slug']})")

    update_sitemap(existing_blogs)
    print("🏁 Auto-blog workflow completed successfully!")


if __name__ == "__main__":
    main()
