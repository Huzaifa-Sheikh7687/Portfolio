import { useState, useEffect, useMemo } from "react";
import { motion } from "framer-motion";
import {
  FiClock,
  FiCalendar,
  FiArrowRight,
  FiSearch,
  FiTag,
  FiBookOpen,
} from "react-icons/fi";
import SectionHeading from "./SectionHeading";
import BlogReaderModal from "./BlogReaderModal";
import initialBlogs from "../data/blogs.json";

export default function Blogs() {
  const [blogs, setBlogs] = useState(initialBlogs);
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [searchQuery, setSearchQuery] = useState("");
  const [activeBlog, setActiveBlog] = useState(null);

  // Extract all unique categories
  const categories = useMemo(() => {
    const cats = new Set(initialBlogs.map((b) => b.category).filter(Boolean));
    return ["All", ...Array.from(cats)];
  }, []);

  // Listen for direct URL hashes like #blog-slug
  useEffect(() => {
    const checkHash = () => {
      const hash = window.location.hash;
      if (hash && hash.startsWith("#blog-")) {
        const slug = hash.replace("#blog-", "");
        const match = initialBlogs.find((b) => b.slug === slug);
        if (match) {
          setActiveBlog(match);
        }
      }
    };

    checkHash();
    window.addEventListener("hashchange", checkHash);
    return () => window.removeEventListener("hashchange", checkHash);
  }, []);

  // Filter blogs based on category & search
  const filteredBlogs = useMemo(() => {
    return blogs.filter((blog) => {
      const matchesCategory =
        selectedCategory === "All" || blog.category === selectedCategory;
      const q = searchQuery.toLowerCase();
      const matchesSearch =
        !searchQuery ||
        blog.title.toLowerCase().includes(q) ||
        blog.excerpt?.toLowerCase().includes(q) ||
        blog.tags?.some((t) => t.toLowerCase().includes(q)) ||
        blog.category?.toLowerCase().includes(q);

      return matchesCategory && matchesSearch;
    });
  }, [blogs, selectedCategory, searchQuery]);

  return (
    <section id="blogs" className="relative bg-ink py-28">
      {/* Dynamic SEO JSON-LD schema for Blog List */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            "@context": "https://schema.org",
            "@type": "Blog",
            "name": "Huzaifa Sheikh - AI & Tech Insights",
            "description": "Daily automated insights on AI Engineering, Data Analytics, and Full Stack Development.",
            "url": "https://huzaifa-sheikh-portfolio.vercel.app/#blogs",
            "author": {
              "@type": "Person",
              "name": "Huzaifa Sheikh",
              "url": "https://huzaifa-sheikh-portfolio.vercel.app"
            },
            "blogPost": blogs.map((b) => ({
              "@type": "BlogPosting",
              "headline": b.title,
              "description": b.excerpt,
              "datePublished": b.date,
              "image": b.coverImage,
              "keywords": b.tags?.join(", "),
              "author": {
                "@type": "Person",
                "name": b.author?.name || "Huzaifa Sheikh"
              }
            }))
          }),
        }}
      />

      <div className="mx-auto max-w-6xl px-6 md:px-8">
        <SectionHeading
          eyebrow="Insights & Articles"
          title="AI & Tech Blog"
          subtitle="Autonomous daily deep-dives into cutting-edge AI Engineering, Data Analytics, and Modern Web Development."
        />

        {/* Filter and Search Controls */}
        <div className="mb-10 flex flex-col md:flex-row items-center justify-between gap-4">
          {/* Category Pills */}
          <div className="flex flex-wrap items-center justify-center gap-2">
            {categories.map((cat) => (
              <button
                key={cat}
                onClick={() => setSelectedCategory(cat)}
                className={`rounded-full px-4 py-1.5 text-xs font-medium transition-all ${
                  selectedCategory === cat
                    ? "bg-slate-900 text-white shadow-md shadow-slate-900/10"
                    : "glass text-slate-600 hover:text-slate-900 hover:bg-white"
                }`}
              >
                {cat}
              </button>
            ))}
          </div>

          {/* Search Box */}
          <div className="relative w-full md:w-72">
            <FiSearch className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="text"
              placeholder="Search articles & tags..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full rounded-full border border-slate-200/80 bg-white/80 py-2 pl-10 pr-4 text-xs text-slate-800 placeholder-slate-400 backdrop-blur focus:border-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-primary/20 transition"
            />
          </div>
        </div>

        {/* Blog Cards Grid */}
        {filteredBlogs.length > 0 ? (
          <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
            {filteredBlogs.map((blog, idx) => (
              <motion.article
                key={blog.id || blog.slug}
                initial={{ opacity: 0, y: 24 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, amount: 0.2 }}
                transition={{ duration: 0.5, delay: (idx % 3) * 0.1 }}
                onClick={() => setActiveBlog(blog)}
                className="glass group flex flex-col overflow-hidden rounded-3xl transition-all duration-300 hover:-translate-y-2 hover:shadow-glow cursor-pointer border border-slate-200/60"
              >
                {/* Thumbnail Image Container */}
                <div className="relative aspect-video w-full overflow-hidden bg-slate-100">
                  <img
                    src={blog.coverImage}
                    alt={blog.title}
                    className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                    onError={(e) => {
                      e.currentTarget.style.display = "none";
                    }}
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-slate-950/60 via-transparent to-transparent opacity-60" />

                  {/* Category Pill on Image */}
                  <span className="absolute top-3 left-3 rounded-full bg-white/90 backdrop-blur-md px-3 py-1 text-[11px] font-semibold text-slate-900 shadow-sm">
                    {blog.category}
                  </span>

                  {/* Read Time on Image */}
                  <span className="absolute bottom-3 right-3 inline-flex items-center gap-1 rounded-full bg-slate-900/80 backdrop-blur-md px-2.5 py-0.5 text-[10px] font-medium text-slate-200">
                    <FiClock size={11} />
                    {blog.readTime || "5 min read"}
                  </span>
                </div>

                {/* Card Body */}
                <div className="flex flex-1 flex-col p-6">
                  {/* Date & Tags */}
                  <div className="mb-3 flex items-center justify-between text-xs text-slate-500">
                    <span className="inline-flex items-center gap-1 font-medium">
                      <FiCalendar className="text-primary" />
                      {blog.date}
                    </span>
                  </div>

                  {/* Title */}
                  <h3 className="font-display text-lg font-semibold leading-snug text-slate-900 group-hover:text-primary transition-colors line-clamp-2">
                    {blog.title}
                  </h3>

                  {/* Excerpt */}
                  <p className="mt-2 text-sm leading-relaxed text-slate-600 line-clamp-3 flex-1">
                    {blog.excerpt}
                  </p>

                  {/* Tags */}
                  {blog.tags && blog.tags.length > 0 && (
                    <div className="mt-4 flex flex-wrap gap-1.5">
                      {blog.tags.slice(0, 3).map((tag) => (
                        <span
                          key={tag}
                          className="rounded-full bg-slate-900/5 px-2.5 py-0.5 text-[11px] font-medium text-slate-500"
                        >
                          #{tag}
                        </span>
                      ))}
                    </div>
                  )}

                  {/* Read Article Action */}
                  <div className="mt-6 flex items-center justify-between border-t border-slate-100 pt-4 text-xs font-semibold text-primary">
                    <span className="inline-flex items-center gap-1 group-hover:underline">
                      Read Full Article
                    </span>
                    <FiArrowRight className="transform transition-transform group-hover:translate-x-1" />
                  </div>
                </div>
              </motion.article>
            ))}
          </div>
        ) : (
          <div className="mx-auto max-w-md rounded-2xl bg-white/60 p-8 text-center backdrop-blur">
            <FiBookOpen className="mx-auto text-slate-400" size={36} />
            <h4 className="mt-3 font-display font-semibold text-slate-800">
              No articles found
            </h4>
            <p className="mt-1 text-xs text-slate-500">
              No blogs match your filter "{searchQuery || selectedCategory}". Try clearing your search!
            </p>
            <button
              onClick={() => {
                setSelectedCategory("All");
                setSearchQuery("");
              }}
              className="mt-4 rounded-full bg-primary px-4 py-1.5 text-xs font-semibold text-white transition hover:bg-primary/90"
            >
              Reset Filters
            </button>
          </div>
        )}
      </div>

      {/* Blog Full Reader Modal */}
      {activeBlog && (
        <BlogReaderModal
          blog={activeBlog}
          onClose={() => setActiveBlog(null)}
        />
      )}
    </section>
  );
}
