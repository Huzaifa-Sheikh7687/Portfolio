import { useState, useEffect, useMemo, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  FiClock,
  FiCalendar,
  FiArrowRight,
  FiSearch,
  FiChevronLeft,
  FiChevronRight,
  FiLayers,
  FiGrid,
  FiSliders,
} from "react-icons/fi";
import SectionHeading from "./SectionHeading";
import BlogReaderModal from "./BlogReaderModal";
import initialBlogs from "../data/blogs.json";

export default function Blogs() {
  const [blogs, setBlogs] = useState(initialBlogs);
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [searchQuery, setSearchQuery] = useState("");
  const [activeBlog, setActiveBlog] = useState(null);
  const [showAllArchive, setShowAllArchive] = useState(false);
  const [activeIndex, setActiveIndex] = useState(0);

  const sliderRef = useRef(null);

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

  // Track active slide index from scroll position
  const handleScroll = () => {
    if (!sliderRef.current) return;
    const { scrollLeft, clientWidth } = sliderRef.current;
    const cardWidth = 360; // approximate card step
    const newIdx = Math.round(scrollLeft / cardWidth);
    setActiveIndex(Math.min(newIdx, filteredBlogs.length - 1));
  };

  const scrollToCard = (index) => {
    if (!sliderRef.current) return;
    const cards = sliderRef.current.children;
    if (cards[index]) {
      cards[index].scrollIntoView({
        behavior: "smooth",
        block: "nearest",
        inline: "start",
      });
      setActiveIndex(index);
    }
  };

  const handleNext = () => {
    if (!sliderRef.current) return;
    const nextIdx = (activeIndex + 1) % filteredBlogs.length;
    scrollToCard(nextIdx);
  };

  const handlePrev = () => {
    if (!sliderRef.current) return;
    const prevIdx = activeIndex === 0 ? filteredBlogs.length - 1 : activeIndex - 1;
    scrollToCard(prevIdx);
  };

  return (
    <section id="blogs" className="relative bg-ink py-28 overflow-hidden">
      {/* Dynamic SEO JSON-LD schema for Blog List */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            "@context": "https://schema.org",
            "@type": "Blog",
            "name": "Huzaifa Sheikh - Data Science & AI Systems",
            "description": "Realistic engineering post-mortems and industrial deep-dives into Data Science, Machine Learning, and Production Pipelines.",
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
          eyebrow="Practical Engineering Journey"
          title="Data Science & ML Deep-Dives"
          subtitle="Realistic post-mortems, hands-on debugging, and industrial architectures from student projects to production."
        />

        {/* Top Controls Bar */}
        <div className="mb-8 flex flex-col md:flex-row items-center justify-between gap-4">
          {/* Category Filter Pills */}
          <div className="flex flex-wrap items-center justify-center gap-2">
            {categories.map((cat) => (
              <button
                key={cat}
                onClick={() => {
                  setSelectedCategory(cat);
                  setActiveIndex(0);
                  if (sliderRef.current) sliderRef.current.scrollLeft = 0;
                }}
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

          {/* Navigation Controls: Slider Left/Right Arrows + Mode Toggle */}
          <div className="flex items-center gap-3">
            {!showAllArchive && filteredBlogs.length > 1 && (
              <div className="flex items-center gap-2">
                <button
                  onClick={handlePrev}
                  className="rounded-full p-2.5 glass text-slate-800 hover:bg-white hover:text-primary hover:shadow-md transition cursor-pointer active:scale-95 border border-slate-200/80"
                  aria-label="Previous article"
                  title="Previous article"
                >
                  <FiChevronLeft size={18} />
                </button>
                <button
                  onClick={handleNext}
                  className="rounded-full p-2.5 glass text-slate-800 hover:bg-white hover:text-primary hover:shadow-md transition cursor-pointer active:scale-95 border border-slate-200/80"
                  aria-label="Next article"
                  title="Next article"
                >
                  <FiChevronRight size={18} />
                </button>
              </div>
            )}

            {/* Toggle Full Archive View */}
            <button
              onClick={() => setShowAllArchive(!showAllArchive)}
              className="inline-flex items-center gap-1.5 rounded-full border border-slate-200/80 bg-white/80 px-4 py-2 text-xs font-semibold text-slate-700 shadow-sm transition hover:bg-white hover:text-primary"
            >
              {showAllArchive ? (
                <>
                  <FiSliders size={14} />
                  <span>Show Slider View</span>
                </>
              ) : (
                <>
                  <FiGrid size={14} />
                  <span>View All ({blogs.length})</span>
                </>
              )}
            </button>
          </div>
        </div>

        {/* Search Bar when Archive view is open */}
        {showAllArchive && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            className="mb-8 flex justify-center"
          >
            <div className="relative w-full max-w-md">
              <FiSearch className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                placeholder="Search topics, algorithms, or tags..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full rounded-full border border-slate-200/80 bg-white/80 py-2.5 pl-10 pr-4 text-xs text-slate-800 placeholder-slate-400 backdrop-blur focus:border-primary focus:bg-white focus:outline-none focus:ring-2 focus:ring-primary/20 transition shadow-sm"
              />
            </div>
          </motion.div>
        )}

        {/* MODE 1: Horizontal Slider / Carousel View with visible overflow peek */}
        {!showAllArchive ? (
          <div>
            <div
              ref={sliderRef}
              onScroll={handleScroll}
              className="flex gap-6 overflow-x-auto scroll-smooth snap-x snap-mandatory py-4 pb-6 px-1"
              style={{
                scrollbarWidth: "thin",
                scrollbarColor: "#CBD5E1 transparent",
              }}
            >
              {filteredBlogs.map((blog, idx) => (
                <div
                  key={blog.id || blog.slug}
                  className="w-[88%] sm:w-[48%] lg:w-[31.6%] min-w-[290px] max-w-[380px] flex-shrink-0 snap-start"
                >
                  <motion.article
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.4, delay: (idx % 3) * 0.08 }}
                    onClick={() => setActiveBlog(blog)}
                    className="glass group flex flex-col h-full overflow-hidden rounded-3xl transition-all duration-300 hover:-translate-y-2 hover:shadow-glow cursor-pointer border border-slate-200/80 bg-white"
                  >
                    {/* Unique Infographic Banner */}
                    <div className="relative aspect-[16/9] w-full overflow-hidden bg-slate-950 border-b border-slate-100">
                      <img
                        src={blog.coverImage}
                        alt={blog.title}
                        className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                      />

                      {/* Category Badge on Image */}
                      <span className="absolute top-3 left-3 rounded-full bg-slate-900/90 backdrop-blur-md px-3 py-1 text-[10px] font-semibold text-white shadow-sm border border-slate-700/50">
                        {blog.category}
                      </span>

                      {/* Read Time on Image */}
                      <span className="absolute bottom-3 right-3 inline-flex items-center gap-1 rounded-full bg-slate-900/90 backdrop-blur-md px-2.5 py-0.5 text-[10px] font-medium text-slate-200 border border-slate-700/50">
                        <FiClock size={11} className="text-primary" />
                        {blog.readTime || "5 min read"}
                      </span>
                    </div>

                    {/* Card Body */}
                    <div className="flex flex-1 flex-col p-6">
                      <div className="mb-2.5 flex items-center justify-between text-xs text-slate-500">
                        <span className="inline-flex items-center gap-1.5 font-medium text-[11px]">
                          <FiCalendar className="text-primary" />
                          {blog.date}
                        </span>
                        {idx === 0 && (
                          <span className="rounded-full bg-emerald-50 px-2 py-0.5 text-[10px] font-bold text-emerald-600 border border-emerald-200">
                            NEWEST
                          </span>
                        )}
                      </div>

                      <h3 className="font-display text-base font-bold leading-snug text-slate-900 group-hover:text-primary transition-colors line-clamp-2">
                        {blog.title}
                      </h3>

                      <p className="mt-2 text-xs leading-relaxed text-slate-600 line-clamp-3 flex-1">
                        {blog.excerpt}
                      </p>

                      {blog.tags && blog.tags.length > 0 && (
                        <div className="mt-4 flex flex-wrap gap-1.5">
                          {blog.tags.slice(0, 3).map((tag) => (
                            <span
                              key={tag}
                              className="rounded-full bg-slate-100 px-2.5 py-0.5 text-[10px] font-medium text-slate-600"
                            >
                              #{tag}
                            </span>
                          ))}
                        </div>
                      )}

                      <div className="mt-5 flex items-center justify-between border-t border-slate-100 pt-3.5 text-xs font-semibold text-primary">
                        <span className="inline-flex items-center gap-1 group-hover:underline">
                          Read Case Study
                        </span>
                        <FiArrowRight className="transform transition-transform group-hover:translate-x-1" />
                      </div>
                    </div>
                  </motion.article>
                </div>
              ))}
            </div>

            {/* Slider Dots Navigation + Indicators */}
            <div className="mt-6 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 border-t border-slate-200/60 pt-4">
              {/* Pagination Dots */}
              <div className="flex items-center gap-2">
                {filteredBlogs.map((_, i) => (
                  <button
                    key={i}
                    onClick={() => scrollToCard(i)}
                    className={`h-2 rounded-full transition-all ${
                      activeIndex === i
                        ? "w-7 bg-primary"
                        : "w-2 bg-slate-300 hover:bg-slate-400"
                    }`}
                    aria-label={`Go to slide ${i + 1}`}
                  />
                ))}
                <span className="ml-2 font-mono-data text-[11px] text-slate-500">
                  {activeIndex + 1} of {filteredBlogs.length}
                </span>
              </div>

              <div className="mt-2 sm:mt-0 flex items-center gap-4">
                <span className="text-slate-400 hidden md:inline">
                  Use arrow buttons or swipe horizontally
                </span>
                <button
                  onClick={() => setShowAllArchive(true)}
                  className="font-semibold text-primary hover:underline inline-flex items-center gap-1"
                >
                  View all in grid mode →
                </button>
              </div>
            </div>
          </div>
        ) : (
          /* MODE 2: Full Archive Grid View */
          <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
            {filteredBlogs.map((blog, idx) => (
              <motion.article
                key={blog.id || blog.slug}
                initial={{ opacity: 0, y: 24 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.4, delay: (idx % 3) * 0.08 }}
                onClick={() => setActiveBlog(blog)}
                className="glass group flex flex-col overflow-hidden rounded-3xl transition-all duration-300 hover:-translate-y-2 hover:shadow-glow cursor-pointer border border-slate-200/80 bg-white"
              >
                <div className="relative aspect-[16/9] w-full overflow-hidden bg-slate-950 border-b border-slate-100">
                  <img
                    src={blog.coverImage}
                    alt={blog.title}
                    className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                  />

                  <span className="absolute top-3 left-3 rounded-full bg-slate-900/90 backdrop-blur-md px-3 py-1 text-[10px] font-semibold text-white shadow-sm border border-slate-700/50">
                    {blog.category}
                  </span>

                  <span className="absolute bottom-3 right-3 inline-flex items-center gap-1 rounded-full bg-slate-900/90 backdrop-blur-md px-2.5 py-0.5 text-[10px] font-medium text-slate-200 border border-slate-700/50">
                    <FiClock size={11} className="text-primary" />
                    {blog.readTime || "5 min read"}
                  </span>
                </div>

                <div className="flex flex-1 flex-col p-6">
                  <div className="mb-2.5 flex items-center justify-between text-xs text-slate-500">
                    <span className="inline-flex items-center gap-1.5 font-medium text-[11px]">
                      <FiCalendar className="text-primary" />
                      {blog.date}
                    </span>
                  </div>

                  <h3 className="font-display text-base font-bold leading-snug text-slate-900 group-hover:text-primary transition-colors line-clamp-2">
                    {blog.title}
                  </h3>

                  <p className="mt-2 text-xs leading-relaxed text-slate-600 line-clamp-3 flex-1">
                    {blog.excerpt}
                  </p>

                  {blog.tags && blog.tags.length > 0 && (
                    <div className="mt-4 flex flex-wrap gap-1.5">
                      {blog.tags.slice(0, 3).map((tag) => (
                        <span
                          key={tag}
                          className="rounded-full bg-slate-100 px-2.5 py-0.5 text-[10px] font-medium text-slate-600"
                        >
                          #{tag}
                        </span>
                      ))}
                    </div>
                  )}

                  <div className="mt-5 flex items-center justify-between border-t border-slate-100 pt-3.5 text-xs font-semibold text-primary">
                    <span className="inline-flex items-center gap-1 group-hover:underline">
                      Read Case Study
                    </span>
                    <FiArrowRight className="transform transition-transform group-hover:translate-x-1" />
                  </div>
                </div>
              </motion.article>
            ))}
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
