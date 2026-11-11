#!/usr/bin/env python3
"""
Technical Architecture Infographic Generator for Huzaifa Sheikh's Portfolio
Generates industrial-grade technical diagrams (like Ghufran Naseer's reference style) in crisp 1200x630 SVG format.
"""

import os
import html

IMAGES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public", "blog-images")
os.makedirs(IMAGES_DIR, exist_ok=True)

def generate_svg_infographic(
    filename,
    category,
    title,
    subtitle,
    cards,
    quote,
    tags,
    config_name,
    metrics
):
    """
    Renders a 1200x630 dark-mode cybernetic system architecture diagram.
    """
    safe_title = html.escape(title)
    safe_subtitle = html.escape(subtitle)
    safe_category = html.escape(category.upper())
    safe_quote = html.escape(quote)
    safe_config = html.escape(config_name)

    # Split title if too long into two lines
    words = safe_title.split()
    line1, line2 = "", ""
    if len(words) > 5:
        mid = len(words) // 2
        line1 = " ".join(words[:mid])
        line2 = " ".join(words[mid:])
    else:
        line1 = safe_title

    # Generate 3 cards XML
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

    # Generate metric rows XML
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

    # Generate tag pills
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

    <!-- Canvas Background -->
    <rect width="1200" height="630" fill="url(#bgGrad)" />
    <rect width="1200" height="630" fill="url(#glow)" />
    <rect width="1200" height="630" fill="url(#glowRight)" />
    <rect width="1200" height="630" fill="url(#gridDots)" />

    <!-- Top Border Line & Eyebrow -->
    <line x1="60" y1="50" x2="1140" y2="50" stroke="#1E293B" stroke-width="1.5" />
    <text x="60" y="40" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="600" fill="#38BDF8" letter-spacing="2">— {safe_category} ARCHITECTURE • 2026</text>
    <text x="1140" y="40" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="500" fill="#64748B" text-anchor="end">PRODUCTION DEPLOYED</text>

    <!-- Main Title & Subtitle -->
    <text x="60" y="95" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="34" fill="url(#titleGrad)">{line1}</text>
    {"<text x='60' y='135' font-family=\"'Space Grotesk', sans-serif\" font-weight='700' font-size='34' fill='url(#titleGrad)'>" + line2 + "</text>" if line2 else ""}
    <text x="60" y="{170 if line2 else 135}" font-family="'Inter', sans-serif" font-size="15" fill="#94A3B8">{safe_subtitle}</text>

    <!-- Left Side: Architectural Cards -->
    {"".join(cards_xml)}

    <!-- Left Side: Quote Box -->
    <g transform="translate(60, 440)">
        <rect x="0" y="0" width="4" height="34" fill="#818CF8" rx="2" />
        <text x="16" y="16" font-family="'Inter', sans-serif" font-style="italic" font-size="12" fill="#CBD5E1">"{safe_quote}"</text>
        <text x="16" y="32" font-family="'Inter', sans-serif" font-size="10" font-weight="600" fill="#64748B">PRODUCTION BEST PRACTICE</text>
    </g>

    <!-- Left Side: Tag Pills -->
    {"".join(tags_xml)}

    <!-- Right Side: Terminal / Metrics Window Container -->
    <g transform="translate(640, 190)">
        <!-- Outer Window Box -->
        <rect width="500" height="330" rx="16" fill="#090E17" fill-opacity="0.9" stroke="#1E293B" stroke-width="1.5" />
        
        <!-- Header Bar -->
        <rect width="500" height="42" rx="16" fill="#0F172A" />
        <rect y="26" width="500" height="16" fill="#0F172A" /> <!-- Flatten bottom corners -->
        <line x1="0" y1="42" x2="500" y2="42" stroke="#1E293B" stroke-width="1" />

        <!-- Window Controls -->
        <circle cx="24" cy="21" r="5" fill="#EF4444" />
        <circle cx="40" cy="21" r="5" fill="#F59E0B" />
        <circle cx="56" cy="21" r="5" fill="#10B981" />

        <text x="76" y="25" font-family="'JetBrains Mono', monospace" font-size="12" fill="#94A3B8">{safe_config}</text>

        <!-- Status Badge -->
        <rect x="420" y="11" width="60" height="20" rx="6" fill="#064E3B" stroke="#059669" stroke-width="0.8" />
        <text x="450" y="24" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#34D399" text-anchor="middle">STABLE</text>

        <!-- Metrics Content -->
        <g transform="translate(20, 20)">
            {"".join(metrics_xml)}
        </g>
    </g>

    <!-- Footer Divider & Meta Details -->
    <line x1="60" y1="570" x2="1140" y2="570" stroke="#1E293B" stroke-width="1" />
    <text x="60" y="595" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748B" letter-spacing="1.5">DATA SCIENCE &amp; ML SYSTEMS</text>
    <text x="600" y="595" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#94A3B8" text-anchor="middle">Huzaifa Sheikh • Engineering Deep-Dive</text>
    <text x="1140" y="595" font-family="'JetBrains Mono', monospace" font-size="11" fill="#38BDF8" text-anchor="end">huzaifa-sheikh-portfolio.vercel.app</text>
</svg>"""

    filepath = os.path.join(IMAGES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print(f"✅ Generated infographic: {filename}")
    return f"/blog-images/{filename}"


def build_all():
    # 1. Feature Store Architecture
    generate_svg_infographic(
        filename="production-feature-stores-low-latency-serving.svg",
        category="Machine Learning",
        title="Production Feature Stores & Serving Architecture",
        subtitle="Low-latency point-in-time correct lookups for real-time inference.",
        cards=[
            {"icon": "⚡", "title": "Online Storage (Redis)", "desc": "Sub-10ms key-value retrieval for real-time model scoring."},
            {"icon": "📦", "title": "Offline Storage (Parquet/Snowflake)", "desc": "Point-in-time correct joins preventing training-serving skew."},
            {"icon": "🛡️", "title": "Feature Registry (Feast/Hopsworks)", "desc": "Centralized metadata, schema evolution and access governance."}
        ],
        quote="Feature engineering without time-travel guarantees guarantees model failure.",
        tags=["FeatureStore", "MLOps", "LowLatency", "Redis"],
        config_name="feature-store.yaml",
        metrics=[
            ("p99-serving-latency", "8.2ms", "#34D399"),
            ("cache-hit-ratio", "99.1%", "#38BDF8"),
            ("schema-conformity", "100%", "#34D399"),
            ("inference-throughput", "5,200 req/s", "#C084FC")
        ]
    )

    # 2. Vector Search & HNSW Indexing
    generate_svg_infographic(
        filename="high-dimensional-vector-search-hnsw-indexing.svg",
        category="Data Science",
        title="High-Dimensional Vector Search & HNSW Indexing",
        subtitle="Sub-10ms nearest neighbor search across billions of high-dimensional vectors.",
        cards=[
            {"icon": "🕸️", "title": "Hierarchical NSW Graph", "desc": "Multi-layer skip-list graph enabling logarithmic O(log N) search."},
            {"icon": "🎯", "title": "Product Quantization (PQ-8)", "desc": "95% memory compression while preserving 98%+ recall accuracy."},
            {"icon": "📐", "title": "SIMD Cosine Distance", "desc": "Hardware-accelerated AVX-512 distance computations."}
        ],
        quote="Vector indexing balances the fundamental triad: Latency, Recall, and RAM.",
        tags=["VectorSearch", "HNSW", "Embeddings", "Quantization"],
        config_name="hnsw-index.json",
        metrics=[
            ("recall-at-10", "98.7%", "#34D399"),
            ("query-latency-p95", "4.1ms", "#38BDF8"),
            ("index-compression", "16x (PQ-8)", "#C084FC"),
            ("vector-dimensions", "1,536 dims", "#F59E0B")
        ]
    )

    # 3. Model Drift Detection
    generate_svg_infographic(
        filename="automated-model-drift-detection-ks-psi.svg",
        category="Machine Learning",
        title="Automated Model Drift & Covariate Shift Detection",
        subtitle="Statistical monitoring with Kolmogorov-Smirnov test and Population Stability Index.",
        cards=[
            {"icon": "📊", "title": "KS-Test for Continuous Features", "desc": "Detects empirical cumulative distribution divergence at p < 0.01."},
            {"icon": "📈", "title": "Population Stability Index (PSI)", "desc": "Quantifies categorical shift: PSI > 0.25 triggers retraining."},
            {"icon": "🔄", "title": "Automated Retraining Loop", "desc": "Airflow DAG triggered to backfill recent production data."}
        ],
        quote="Silent model degradation is far deadlier than a service crash.",
        tags=["ModelDrift", "Statistics", "MLOps", "PSI"],
        config_name="drift-monitor.py",
        metrics=[
            ("ks-p-value", "0.42 (Healthy)", "#34D399"),
            ("baseline-psi", "0.038", "#34D399"),
            ("monitoring-window", "Rolling 24h", "#38BDF8"),
            ("retrain-trigger-status", "Idle / Stable", "#C084FC")
        ]
    )

    # 4. QLoRA & LLM Fine-Tuning
    generate_svg_infographic(
        filename="industrial-llm-fine-tuning-qlora-quantization.svg",
        category="Deep Learning",
        title="Industrial LLM Fine-Tuning: QLoRA & 4-Bit NF4",
        subtitle="Parameter-efficient adaptation scaling from single GPUs to production clusters.",
        cards=[
            {"icon": "📉", "title": "Low-Rank Adaptation (LoRA)", "desc": "Freezes base weights and trains rank decomposition matrices A and B."},
            {"icon": "🧩", "title": "4-bit NormalFloat (NF4)", "desc": "Information-theoretically optimal quantile quantization for weights."},
            {"icon": "⚡", "title": "FlashAttention-2 Kernel", "desc": "Fuses softmax and matrix multiplication to save 75% GPU VRAM."}
        ],
        quote="Fine-tuning is no longer about raw parameter counts; it's about efficient rank adaptation.",
        tags=["DeepLearning", "QLoRA", "PyTorch", "FlashAttention"],
        config_name="train-qlora.py",
        metrics=[
            ("trainable-params", "0.24% of Total", "#38BDF8"),
            ("vram-footprint", "14.2 GB (NF4)", "#34D399"),
            ("tokens-per-sec", "3,850 tok/s", "#C084FC"),
            ("eval-perplexity", "2.14 (-18%)", "#34D399")
        ]
    )

if __name__ == "__main__":
    build_all()
