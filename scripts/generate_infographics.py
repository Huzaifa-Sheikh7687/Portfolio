#!/usr/bin/env python3
"""
Technical Architecture Infographic Generator for Huzaifa Sheikh's Portfolio
Generates 4 COMPLETELY UNIQUE, visually distinct infographics matching industrial references:
- Style 1: Clean Light-Mode 3-Column Architecture (like Ghufran's 1st reference image)
- Style 2: Cybernetic Cyan/Blue Vector Geometry & Topology (HNSW Indexing)
- Style 3: Amber/Ruby Diagnostic Comparison Matrix (Model Leakage & Drift)
- Style 4: Deep Purple GPU Memory & Tensor Architecture (QLoRA Fine-Tuning)
"""

import os
import html

IMAGES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public", "blog-images")
os.makedirs(IMAGES_DIR, exist_ok=True)


# ==========================================
# STYLE 1: CLEAN LIGHT-MODE 3-COLUMN (Ghufran's Reference 1)
# ==========================================
def generate_light_3column_infographic(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
    <defs>
        <pattern id="lightDots" x="0" y="0" width="24" height="24" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="1.2" fill="#CBD5E1" fill-opacity="0.6" />
        </pattern>
        <filter id="softShadow" x="-5%" y="-5%" width="110%" height="110%">
            <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0F172A" flood-opacity="0.06"/>
        </filter>
    </defs>

    <!-- Canvas Background -->
    <rect width="1200" height="630" fill="#F8FAFC" />
    <rect width="1200" height="630" fill="url(#lightDots)" />

    <!-- Top Eyebrow Bar -->
    <rect x="50" y="32" width="230" height="24" rx="12" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1" />
    <text x="65" y="48" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#2563EB" letter-spacing="1">DATA PIPELINE ARCHITECTURE</text>
    <text x="1150" y="48" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="600" fill="#64748B" text-anchor="end">POLARS • CHUNKING • CACHING</text>

    <!-- Main Title -->
    <text x="50" y="96" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="33" fill="#0F172A">
        Solving The <tspan fill="#2563EB">Pandas OOM Crash</tspan>: Ingestion <tspan fill="#64748B">vs</tspan> <tspan fill="#059669">Memory</tspan> <tspan fill="#64748B">vs</tspan> <tspan fill="#D97706">Serving</tspan>
    </text>

    <!-- 3 COLUMNS CONTAINER -->
    <!-- Column 1: Blue (Ingestion) -->
    <g transform="translate(50, 130)">
        <rect width="345" height="420" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#softShadow)" />
        <rect width="345" height="8" rx="4" fill="#2563EB" />
        
        <text x="20" y="36" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="17" fill="#0F172A">| Ingestion Layer</text>
        <text x="325" y="36" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#2563EB" text-anchor="end">STREAMING &amp; CHUNK</text>
        
        <!-- Card 1 -->
        <g transform="translate(16, 55)">
            <rect width="313" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0" />
            <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#2563EB">chunk_size=50_000</text>
            <text x="14" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#64748B">Stream raw CSV/JSON in bounded batches</text>
        </g>
        <!-- Card 2 -->
        <g transform="translate(16, 125)">
            <rect width="313" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0" />
            <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#2563EB">polars.scan_csv()</text>
            <text x="14" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#64748B">Lazy evaluation &amp; query plan optimization</text>
        </g>
        <!-- Card 3 -->
        <g transform="translate(16, 195)">
            <rect width="313" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0" />
            <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#2563EB">parquet_zstd</text>
            <text x="14" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#64748B">Columnar compression saving 82% disk</text>
        </g>

        <!-- Bottom Callout -->
        <text x="20" y="340" font-family="'Inter', sans-serif" font-size="12" font-weight="500" fill="#334155">Eliminate RAM spikes before transformation.</text>
        <text x="20" y="360" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#2563EB">USE FOR INGESTION PIPELINES</text>
    </g>

    <!-- Column 2: Emerald (Runtime Logic) -->
    <g transform="translate(427, 130)">
        <rect width="345" height="420" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#softShadow)" />
        <rect width="345" height="8" rx="4" fill="#059669" />
        
        <text x="20" y="36" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="17" fill="#0F172A">| Runtime Memory</text>
        <text x="325" y="36" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#059669" text-anchor="end">ARROW &amp; ZERO-COPY</text>
        
        <!-- Card 1 -->
        <g transform="translate(16, 55)">
            <rect width="313" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0" />
            <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#059669">pyarrow.Table</text>
            <text x="14" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#64748B">Zero-copy shared memory architecture</text>
        </g>
        <!-- Card 2 -->
        <g transform="translate(16, 125)">
            <rect width="313" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0" />
            <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#059669">downcast_dtypes()</text>
            <text x="14" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#64748B">float64 -> float32 &amp; category encoding</text>
        </g>
        <!-- Card 3 -->
        <g transform="translate(16, 195)">
            <rect width="313" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0" />
            <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#059669">gc.collect()</text>
            <text x="14" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#64748B">Explicit circular reference memory release</text>
        </g>

        <!-- Bottom Callout -->
        <text x="20" y="340" font-family="'Inter', sans-serif" font-size="12" font-weight="500" fill="#334155">Keep peak memory usage below 2 GB.</text>
        <text x="20" y="360" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#059669">USE FOR FEATURE ENGINEERING</text>
    </g>

    <!-- Column 3: Amber (Serving Strategy) -->
    <g transform="translate(805, 130)">
        <rect width="345" height="420" rx="16" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#softShadow)" />
        <rect width="345" height="8" rx="4" fill="#D97706" />
        
        <text x="20" y="36" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="17" fill="#0F172A">| Feature Serving</text>
        <text x="325" y="36" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#D97706" text-anchor="end">REDIS &amp; FEAST</text>
        
        <!-- Card 1 -->
        <g transform="translate(16, 55)">
            <rect width="313" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0" />
            <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#D97706">redis.mget()</text>
            <text x="14" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#64748B">Sub-5ms multi-key real-time retrieval</text>
        </g>
        <!-- Card 2 -->
        <g transform="translate(16, 125)">
            <rect width="313" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0" />
            <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#D97706">point_in_time_join</text>
            <text x="14" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#64748B">Zero target leakage AS-OF temporal joins</text>
        </g>
        <!-- Card 3 -->
        <g transform="translate(16, 195)">
            <rect width="313" height="60" rx="10" fill="#F8FAFC" stroke="#E2E8F0" />
            <text x="14" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#D97706">feature_ttl=30d</text>
            <text x="14" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#64748B">Automated eviction of stale observations</text>
        </g>

        <!-- Bottom Callout -->
        <text x="20" y="340" font-family="'Inter', sans-serif" font-size="12" font-weight="500" fill="#334155">Deliver production vectors at scale.</text>
        <text x="20" y="360" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#D97706">USE FOR PRODUCTION INFERENCE</text>
    </g>

    <!-- Footer Bar -->
    <line x1="50" y1="585" x2="1150" y2="585" stroke="#E2E8F0" stroke-width="1" />
    <text x="50" y="608" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#64748B">Huzaifa Sheikh • Practical Data Engineering</text>
    <text x="1150" y="608" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="500" fill="#2563EB" text-anchor="end">huzaifa-sheikh-portfolio.vercel.app</text>
</svg>"""
    filepath = os.path.join(IMAGES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print(f"✅ Generated Style 1 (Light Mode 3-Column): {filename}")


# ==========================================
# STYLE 2: CYBERNETIC CYAN/BLUE VECTOR GEOMETRY (HNSW Vector Search)
# ==========================================
def generate_vector_search_infographic(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
    <defs>
        <linearGradient id="vBg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#030712" />
            <stop offset="50%" stop-color="#0B132B" />
            <stop offset="100%" stop-color="#020617" />
        </linearGradient>
        <radialGradient id="vCyan" cx="70%" cy="30%" r="50%">
            <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.2" />
            <stop offset="100%" stop-color="#06B6D4" stop-opacity="0" />
        </radialGradient>
        <linearGradient id="vTextGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FFFFFF" />
            <stop offset="70%" stop-color="#38BDF8" />
            <stop offset="100%" stop-color="#06B6D4" />
        </linearGradient>
    </defs>

    <rect width="1200" height="630" fill="url(#vBg)" />
    <rect width="1200" height="630" fill="url(#vCyan)" />

    <!-- Grid lines -->
    <line x1="50" y1="50" x2="1150" y2="50" stroke="#1E293B" stroke-width="1.5" />
    <text x="50" y="40" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#38BDF8">— ALGORITHM &amp; VECTOR RETRIEVAL DEEP-DIVE</text>
    <text x="1150" y="40" font-family="'JetBrains Mono', monospace" font-size="12" fill="#64748B" text-anchor="end">O(log N) SIMILARITY SEARCH</text>

    <!-- Main Title -->
    <text x="50" y="98" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="34" fill="url(#vTextGrad)">High-Dimensional Vector Search: HNSW &amp; PQ-8</text>
    <text x="50" y="132" font-family="'Inter', sans-serif" font-size="15" fill="#94A3B8">How approximate nearest neighbor graphs eliminate 1.4s brute-force cosine bottlenecks down to 4.1ms.</text>

    <!-- LEFT SIDE: 3 ARCHITECTURE PILLARS -->
    <g transform="translate(50, 165)">
        <!-- Box 1 -->
        <g transform="translate(0, 0)">
            <rect width="500" height="80" rx="12" fill="#0F172A" stroke="#0284C7" stroke-width="1" />
            <text x="20" y="32" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#38BDF8">1. Hierarchical Skip-List Topology</text>
            <text x="20" y="55" font-family="'Inter', sans-serif" font-size="12" fill="#94A3B8">Upper sparse layers hop vast distances; lower dense layers refine local clusters.</text>
        </g>
        <!-- Box 2 -->
        <g transform="translate(0, 95)">
            <rect width="500" height="80" rx="12" fill="#0F172A" stroke="#0284C7" stroke-width="1" />
            <text x="20" y="32" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#38BDF8">2. Product Quantization (16x RAM Reduction)</text>
            <text x="20" y="55" font-family="'Inter', sans-serif" font-size="12" fill="#94A3B8">Splits 1536-dim vectors into sub-vectors encoded as 8-bit cluster centroid indices.</text>
        </g>
        <!-- Box 3 -->
        <g transform="translate(0, 190)">
            <rect width="500" height="80" rx="12" fill="#0F172A" stroke="#0284C7" stroke-width="1" />
            <text x="20" y="32" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#38BDF8">3. AVX-512 SIMD Distance Acceleration</text>
            <text x="20" y="55" font-family="'Inter', sans-serif" font-size="12" fill="#94A3B8">Fuses vector dot products directly inside CPU vector registers for 3x throughput.</text>
        </g>

        <!-- Bottom Quote -->
        <g transform="translate(0, 290)">
            <rect x="0" y="0" width="4" height="40" fill="#38BDF8" rx="2" />
            <text x="16" y="18" font-family="'Inter', sans-serif" font-style="italic" font-size="13" fill="#E2E8F0">"Never run brute-force numpy cosine loops in production; index topology is everything."</text>
            <text x="16" y="36" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#38BDF8">PRODUCTION PRINCIPLE</text>
        </g>
    </g>

    <!-- RIGHT SIDE: VISUAL BENCHMARK & TOPOLOGY CARD -->
    <g transform="translate(600, 165)">
        <rect width="550" height="360" rx="16" fill="#090E17" stroke="#1E293B" stroke-width="1.5" />
        
        <!-- Header -->
        <rect width="550" height="44" rx="16" fill="#0F172A" />
        <rect y="28" width="550" height="16" fill="#0F172A" />
        <line x1="0" y1="44" x2="550" y2="44" stroke="#1E293B" />
        <circle cx="24" cy="22" r="5" fill="#EF4444" />
        <circle cx="40" cy="22" r="5" fill="#F59E0B" />
        <circle cx="56" cy="22" r="5" fill="#10B981" />
        <text x="76" y="26" font-family="'JetBrains Mono', monospace" font-size="12" fill="#94A3B8">vector-benchmark.py</text>
        <text x="520" y="26" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#34D399" text-anchor="end">100K VECTORS @ 1536-D</text>

        <!-- Benchmarks Comparison Rows -->
        <g transform="translate(24, 75)">
            <text x="0" y="0" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#E2E8F0">Brute-Force k-NN (Flat)</text>
            <text x="500" y="0" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="#EF4444" text-anchor="end">1,420 ms (Unusable)</text>
            <rect x="0" y="10" width="500" height="8" rx="4" fill="#334155" />
            <rect x="0" y="10" width="500" height="8" rx="4" fill="#EF4444" />

            <g transform="translate(0, 60)">
                <text x="0" y="0" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#E2E8F0">IVF-PQ (Inverted File Quantized)</text>
                <text x="500" y="0" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="#F59E0B" text-anchor="end">28.4 ms (91% Recall)</text>
                <rect x="0" y="10" width="500" height="8" rx="4" fill="#334155" />
                <rect x="0" y="10" width="180" height="8" rx="4" fill="#F59E0B" />
            </g>

            <g transform="translate(0, 120)">
                <text x="0" y="0" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#E2E8F0">HNSW + PQ-8 (Our Architecture)</text>
                <text x="500" y="0" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="#34D399" text-anchor="end">4.1 ms (98.7% Recall) ⚡</text>
                <rect x="0" y="10" width="500" height="8" rx="4" fill="#334155" />
                <rect x="0" y="10" width="40" height="8" rx="4" fill="#34D399" />
            </g>

            <!-- Memory comparison -->
            <g transform="translate(0, 180)">
                <line x1="0" y1="0" x2="500" y2="0" stroke="#1E293B" stroke-dasharray="3 3" />
                <text x="0" y="24" font-family="'JetBrains Mono', monospace" font-size="12" fill="#94A3B8">Memory Footprint (10M Vectors):</text>
                <text x="500" y="24" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" fill="#38BDF8" text-anchor="end">61.4 GB -> 3.84 GB (-93.7%)</text>
            </g>
        </g>
    </g>

    <!-- Footer -->
    <line x1="50" y1="580" x2="1150" y2="580" stroke="#1E293B" stroke-width="1" />
    <text x="50" y="605" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#94A3B8">Huzaifa Sheikh • Vector Database Engineering</text>
    <text x="1150" y="605" font-family="'JetBrains Mono', monospace" font-size="12" fill="#38BDF8" text-anchor="end">huzaifa-sheikh-portfolio.vercel.app</text>
</svg>"""
    filepath = os.path.join(IMAGES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print(f"✅ Generated Style 2 (Vector Search Geometry): {filename}")


# ==========================================
# STYLE 3: AMBER/ROSE DIAGNOSTIC COMPARISON (Target Leakage & Drift)
# ==========================================
def generate_drift_diagnostic_infographic(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
    <defs>
        <linearGradient id="dBg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#140A07" />
            <stop offset="50%" stop-color="#1C100D" />
            <stop offset="100%" stop-color="#0A0605" />
        </linearGradient>
        <radialGradient id="dAmber" cx="20%" cy="20%" r="50%">
            <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.18" />
            <stop offset="100%" stop-color="#F59E0B" stop-opacity="0" />
        </radialGradient>
        <linearGradient id="dTextGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FFFFFF" />
            <stop offset="60%" stop-color="#FBBF24" />
            <stop offset="100%" stop-color="#F87171" />
        </linearGradient>
    </defs>

    <rect width="1200" height="630" fill="url(#dBg)" />
    <rect width="1200" height="630" fill="url(#dAmber)" />

    <line x1="50" y1="50" x2="1150" y2="50" stroke="#291814" stroke-width="1.5" />
    <text x="50" y="40" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#F59E0B">— REALISTIC MACHINE LEARNING PITFALLS</text>
    <text x="1150" y="40" font-family="'JetBrains Mono', monospace" font-size="12" fill="#A87165" text-anchor="end">COLLEGE NOTEBOOK VS INDUSTRIAL REALITY</text>

    <!-- Main Title -->
    <text x="50" y="98" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="33" fill="url(#dTextGrad)">Why My Model Had 99% Accuracy But Failed In Production</text>
    <text x="50" y="132" font-family="'Inter', sans-serif" font-size="15" fill="#D6A59A">The temporal leakage trap: how random train_test_split destroys real-world inference.</text>

    <!-- TWO COLUMN SIDE-BY-SIDE COMPARISON -->
    <!-- Left Box: The Naive Bug (Red) -->
    <g transform="translate(50, 160)">
        <rect width="520" height="380" rx="16" fill="#1A0D0A" stroke="#7F1D1D" stroke-width="1.5" />
        
        <rect width="520" height="42" rx="16" fill="#450A0A" />
        <rect y="26" width="520" height="16" fill="#450A0A" />
        <line x1="0" y1="42" x2="520" y2="42" stroke="#7F1D1D" />
        <text x="24" y="27" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700" fill="#FCA5A5">❌ The Naive Student Mistake</text>
        <text x="496" y="27" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#F87171" text-anchor="end">TRAIN ACC: 99.4% | LIVE: 52%</text>

        <g transform="translate(24, 65)">
            <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#FCA5A5">1. Random train_test_split()</text>
            <text x="0" y="22" font-family="'Inter', sans-serif" font-size="13" fill="#D6A59A">Shuffling temporal time-series leaks future user actions into training history.</text>

            <text x="0" y="70" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#FCA5A5">2. Global Mean Imputation</text>
            <text x="0" y="92" font-family="'Inter', sans-serif" font-size="13" fill="#D6A59A">df.fillna(df.mean()) calculates statistics across both past and future rows.</text>

            <text x="0" y="140" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#FCA5A5">3. Silent Covariate Shift</text>
            <text x="0" y="162" font-family="'Inter', sans-serif" font-size="13" fill="#D6A59A">Model continues predicting with 0.95 confidence while data distribution drifts.</text>

            <g transform="translate(0, 210)">
                <rect width="472" height="60" rx="8" fill="#2B100C" stroke="#7F1D1D" />
                <text x="16" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#F87171">FATAL OUTCOME:</text>
                <text x="16" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#FECACA">Model memorizes temporal shortcuts instead of learning real patterns.</text>
            </g>
        </g>
    </g>

    <!-- Right Box: The Industrial Fix (Green) -->
    <g transform="translate(630, 160)">
        <rect width="520" height="380" rx="16" fill="#0A1811" stroke="#065F46" stroke-width="1.5" />
        
        <rect width="520" height="42" rx="16" fill="#064E3B" />
        <rect y="26" width="520" height="16" fill="#064E3B" />
        <line x1="0" y1="42" x2="520" y2="42" stroke="#065F46" />
        <text x="24" y="27" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700" fill="#6EE7B7">✅ The Production-Grade Fix</text>
        <text x="496" y="27" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#34D399" text-anchor="end">STABLE LIVE ACC: 91.8%</text>

        <g transform="translate(24, 65)">
            <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#6EE7B7">1. Purged Group TimeSeriesSplit</text>
            <text x="0" y="22" font-family="'Inter', sans-serif" font-size="13" fill="#A7F3D0">Strict temporal boundary evaluation ensuring zero future glimpse.</text>

            <text x="0" y="70" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#6EE7B7">2. Scikit-Learn Pipeline Fitting</text>
            <text x="0" y="92" font-family="'Inter', sans-serif" font-size="13" fill="#A7F3D0">Imputers &amp; Scalers fit ONLY on training fold, strictly transforming test.</text>

            <text x="0" y="140" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#6EE7B7">3. Statistical KS-Test &amp; PSI Drift Guard</text>
            <text x="0" y="162" font-family="'Inter', sans-serif" font-size="13" fill="#A7F3D0">Nightly Kolmogorov-Smirnov runs trigger automated retraining alerts.</text>

            <g transform="translate(0, 210)">
                <rect width="472" height="60" rx="8" fill="#064E3B" stroke="#059669" />
                <text x="16" y="24" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#34D399">PRODUCTION OUTCOME:</text>
                <text x="16" y="44" font-family="'Inter', sans-serif" font-size="12" fill="#D1FAE5">Robust, resilient models that maintain revenue impact across quarters.</text>
            </g>
        </g>
    </g>

    <!-- Footer -->
    <line x1="50" y1="580" x2="1150" y2="580" stroke="#291814" stroke-width="1" />
    <text x="50" y="605" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#D6A59A">Huzaifa Sheikh • Machine Learning Pitfall Analysis</text>
    <text x="1150" y="605" font-family="'JetBrains Mono', monospace" font-size="12" fill="#F59E0B" text-anchor="end">huzaifa-sheikh-portfolio.vercel.app</text>
</svg>"""
    filepath = os.path.join(IMAGES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print(f"✅ Generated Style 3 (Diagnostic Comparison Matrix): {filename}")


# ==========================================
# STYLE 4: DEEP PURPLE/VIOLET GPU MEMORY ARCHITECTURE (QLoRA)
# ==========================================
def generate_qlora_gpu_infographic(filename):
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
    <defs>
        <linearGradient id="qBg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0B0618" />
            <stop offset="50%" stop-color="#14092A" />
            <stop offset="100%" stop-color="#070310" />
        </linearGradient>
        <radialGradient id="qPurple" cx="80%" cy="30%" r="50%">
            <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.25" />
            <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0" />
        </radialGradient>
        <linearGradient id="qTextGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#FFFFFF" />
            <stop offset="60%" stop-color="#C084FC" />
            <stop offset="100%" stop-color="#8B5CF6" />
        </linearGradient>
    </defs>

    <rect width="1200" height="630" fill="url(#qBg)" />
    <rect width="1200" height="630" fill="url(#qPurple)" />

    <line x1="50" y1="50" x2="1150" y2="50" stroke="#2E1065" stroke-width="1.5" />
    <text x="50" y="40" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#C084FC">— DEEP LEARNING &amp; GPU HARDWARE OPTIMIZATION</text>
    <text x="1150" y="40" font-family="'JetBrains Mono', monospace" font-size="12" fill="#A78BFA" text-anchor="end">SINGLE-GPU CONSUMER FINE-TUNING</text>

    <!-- Main Title -->
    <text x="50" y="98" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="34" fill="url(#qTextGrad)">Fine-Tuning Llama 3 on a Single Laptop GPU: QLoRA</text>
    <text x="50" y="132" font-family="'Inter', sans-serif" font-size="15" fill="#DDD6FE">How 4-bit NormalFloat quantization and rank decomposition train 8B models in under 16 GB VRAM.</text>

    <!-- LEFT SIDE: 3 TENSOR MODULES -->
    <g transform="translate(50, 165)">
        <g transform="translate(0, 0)">
            <rect width="500" height="80" rx="12" fill="#1E0E38" stroke="#581C87" stroke-width="1" />
            <text x="20" y="32" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#C084FC">1. 4-bit NormalFloat (NF4) Quantization</text>
            <text x="20" y="55" font-family="'Inter', sans-serif" font-size="12" fill="#DDD6FE">Saves 75% memory by matching normal weight distribution quantiles.</text>
        </g>
        <g transform="translate(0, 95)">
            <rect width="500" height="80" rx="12" fill="#1E0E38" stroke="#581C87" stroke-width="1" />
            <text x="20" y="32" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#C084FC">2. Rank Decomposition (LoRA r=16)</text>
            <text x="20" y="55" font-family="'Inter', sans-serif" font-size="12" fill="#DDD6FE">Freezes 8B base weights; updates only 0.52% parameters in adapter matrices A &amp; B.</text>
        </g>
        <g transform="translate(0, 190)">
            <rect width="500" height="80" rx="12" fill="#1E0E38" stroke="#581C87" stroke-width="1" />
            <text x="20" y="32" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#C084FC">3. FlashAttention-2 &amp; Paged Optimizers</text>
            <text x="20" y="55" font-family="'Inter', sans-serif" font-size="12" fill="#DDD6FE">Eliminates quadratic attention VRAM explosion and pages spikes to CPU RAM.</text>
        </g>

        <g transform="translate(0, 290)">
            <rect x="0" y="0" width="4" height="40" fill="#C084FC" rx="2" />
            <text x="16" y="18" font-family="'Inter', sans-serif" font-style="italic" font-size="13" fill="#EDE9FE">"You do not need an enterprise server cluster to master LLM engineering in 2026."</text>
            <text x="16" y="36" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#C084FC">STUDENT EMPOWERMENT PRINCIPLE</text>
        </g>
    </g>

    <!-- RIGHT SIDE: VRAM CONSUMPTION COMPARISON -->
    <g transform="translate(600, 165)">
        <rect width="550" height="360" rx="16" fill="#100824" stroke="#3B0764" stroke-width="1.5" />
        
        <rect width="550" height="44" rx="16" fill="#1E0E38" />
        <rect y="28" width="550" height="16" fill="#1E0E38" />
        <line x1="0" y1="44" x2="550" y2="44" stroke="#3B0764" />
        <circle cx="24" cy="22" r="5" fill="#EF4444" />
        <circle cx="40" cy="22" r="5" fill="#F59E0B" />
        <circle cx="56" cy="22" r="5" fill="#10B981" />
        <text x="76" y="26" font-family="'JetBrains Mono', monospace" font-size="12" fill="#DDD6FE">vram-allocation-budget.py</text>
        <text x="520" y="26" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#34D399" text-anchor="end">LLAMA 3 (8B PARAMS)</text>

        <g transform="translate(24, 75)">
            <!-- Standard FP16 Full Fine-Tuning -->
            <text x="0" y="0" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#EDE9FE">Standard Full Fine-Tuning (FP16 / AdamW)</text>
            <text x="500" y="0" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="#EF4444" text-anchor="end">64.0 GB VRAM (OOM Crash ❌)</text>
            <rect x="0" y="10" width="500" height="12" rx="6" fill="#2E1065" />
            <rect x="0" y="10" width="500" height="12" rx="6" fill="#EF4444" />

            <!-- LoRA FP16 -->
            <g transform="translate(0, 65)">
                <text x="0" y="0" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#EDE9FE">Standard LoRA (FP16 Base Weights)</text>
                <text x="500" y="0" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="#F59E0B" text-anchor="end">28.5 GB VRAM (Requires A100)</text>
                <rect x="0" y="10" width="500" height="12" rx="6" fill="#2E1065" />
                <rect x="0" y="10" width="220" height="12" rx="6" fill="#F59E0B" />
            </g>

            <!-- QLoRA NF4 -->
            <g transform="translate(0, 130)">
                <text x="0" y="0" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#EDE9FE">QLoRA 4-bit NF4 + FlashAttention-2 (Our Stack)</text>
                <text x="500" y="0" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="#34D399" text-anchor="end">14.2 GB VRAM (Fits on 16GB GPU ✅)</text>
                <rect x="0" y="10" width="500" height="12" rx="6" fill="#2E1065" />
                <rect x="0" y="10" width="110" height="12" rx="6" fill="#34D399" />
            </g>

            <g transform="translate(0, 190)">
                <line x1="0" y1="0" x2="500" y2="0" stroke="#3B0764" stroke-dasharray="3 3" />
                <text x="0" y="24" font-family="'JetBrains Mono', monospace" font-size="12" fill="#A78BFA">Cost per Training Run:</text>
                <text x="500" y="24" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="700" fill="#34D399" text-anchor="end">$450 cloud cluster -> $0 (Local GPU)</text>
            </g>
        </g>
    </g>

    <!-- Footer -->
    <line x1="50" y1="580" x2="1150" y2="580" stroke="#2E1065" stroke-width="1" />
    <text x="50" y="605" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#A78BFA">Huzaifa Sheikh • Applied Deep Learning</text>
    <text x="1150" y="605" font-family="'JetBrains Mono', monospace" font-size="12" fill="#C084FC" text-anchor="end">huzaifa-sheikh-portfolio.vercel.app</text>
</svg>"""
    filepath = os.path.join(IMAGES_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg.strip())
    print(f"✅ Generated Style 4 (GPU VRAM Budget): {filename}")


def build_all():
    generate_light_3column_infographic("production-feature-stores-low-latency-serving.svg")
    generate_vector_search_infographic("high-dimensional-vector-search-hnsw-indexing.svg")
    generate_drift_diagnostic_infographic("automated-model-drift-detection-ks-psi.svg")
    generate_qlora_gpu_infographic("industrial-llm-fine-tuning-qlora-quantization.svg")


if __name__ == "__main__":
    build_all()
