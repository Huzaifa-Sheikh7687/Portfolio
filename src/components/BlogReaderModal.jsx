import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  FiX,
  FiClock,
  FiCalendar,
  FiShare2,
  FiCheck,
  FiCopy,
  FiArrowLeft,
  FiExternalLink,
} from "react-icons/fi";
import { FaLinkedin, FaTwitter, FaWhatsapp } from "react-icons/fa";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export default function BlogReaderModal({ blog, onClose }) {
  const [copied, setCopied] = useState(false);
  const [codeCopiedIndex, setCodeCopiedIndex] = useState(null);

  useEffect(() => {
    if (!blog) return;

    // Set page title for SEO and user experience
    const originalTitle = document.title;
    document.title = `${blog.title} | Huzaifa Sheikh`;

    // Prevent body scroll when modal is open
    document.body.style.overflow = "hidden";

    // Update URL hash without reload for shareable links
    window.location.hash = `blog-${blog.slug}`;

    const handleKeyDown = (e) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", handleKeyDown);

    return () => {
      document.title = originalTitle;
      document.body.style.overflow = "auto";
      window.removeEventListener("keydown", handleKeyDown);
      if (window.location.hash.startsWith("#blog-")) {
        history.replaceState(null, "", window.location.pathname);
      }
    };
  }, [blog, onClose]);

  if (!blog) return null;

  const currentUrl = typeof window !== "undefined" ? window.location.href : "";

  const handleCopyLink = () => {
    navigator.clipboard.writeText(currentUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  };

  const handleCopyCode = (text, idx) => {
    navigator.clipboard.writeText(text);
    setCodeCopiedIndex(idx);
    setTimeout(() => setCodeCopiedIndex(null), 2000);
  };

  return (
    <AnimatePresence>
      <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 md:p-6 overflow-y-auto">
        {/* Dynamic SEO JSON-LD schema for Google Search & Rich Results */}
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              "@context": "https://schema.org",
              "@type": "BlogPosting",
              "headline": blog.title,
              "description": blog.excerpt,
              "image": blog.coverImage?.startsWith("http")
                ? blog.coverImage
                : `https://huzaifa-sheikh-portfolio.vercel.app${blog.coverImage}`,
              "datePublished": blog.date,
              "dateModified": blog.date,
              "author": {
                "@type": "Person",
                "name": blog.author?.name || "Huzaifa Sheikh",
                "url": "https://huzaifa-sheikh-portfolio.vercel.app"
              },
              "publisher": {
                "@type": "Person",
                "name": "Huzaifa Sheikh"
              },
              "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": `https://huzaifa-sheikh-portfolio.vercel.app/#blog-${blog.slug}`
              },
              "keywords": blog.tags?.join(", ")
            })
          }}
        />

        {/* Backdrop */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
          className="fixed inset-0 bg-slate-950/70 backdrop-blur-md transition-opacity"
        />

        {/* Modal Card */}
        <motion.article
          initial={{ opacity: 0, scale: 0.95, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.95, y: 20 }}
          transition={{ duration: 0.3, ease: "easeOut" }}
          className="relative z-10 my-auto flex max-h-[92vh] w-full max-w-4xl flex-col rounded-3xl bg-white shadow-2xl border border-slate-200/80 overflow-hidden"
          onClick={(e) => e.stopPropagation()}
        >
          {/* Header Bar */}
          <div className="sticky top-0 z-20 flex items-center justify-between border-b border-slate-100 bg-white/90 px-6 py-4 backdrop-blur-md">
            <button
              onClick={onClose}
              className="inline-flex items-center gap-2 rounded-full px-3 py-1.5 text-xs font-medium text-slate-600 transition-colors hover:bg-slate-100 hover:text-slate-900"
            >
              <FiArrowLeft size={16} />
              <span>Back to Blogs</span>
            </button>

            <div className="flex items-center gap-2">
              <button
                onClick={handleCopyLink}
                className="inline-flex items-center gap-1.5 rounded-full border border-slate-200 bg-slate-50 px-3 py-1.5 text-xs font-medium text-slate-700 transition hover:bg-slate-100"
                title="Copy share link"
              >
                {copied ? (
                  <>
                    <FiCheck className="text-emerald-600" />
                    <span className="text-emerald-600 font-semibold">Copied!</span>
                  </>
                ) : (
                  <>
                    <FiCopy />
                    <span>Copy Link</span>
                  </>
                )}
              </button>

              <button
                onClick={onClose}
                className="rounded-full p-2 text-slate-400 hover:bg-slate-100 hover:text-slate-700"
                aria-label="Close article"
              >
                <FiX size={20} />
              </button>
            </div>
          </div>

          {/* Scrollable Blog Content */}
          <div className="overflow-y-auto px-6 py-8 sm:px-10 md:px-14">
            {/* Cover Image */}
            {blog.coverImage && (
              <div className="relative mb-8 aspect-video w-full overflow-hidden rounded-2xl bg-slate-100 shadow-md">
                <img
                  src={blog.coverImage}
                  alt={blog.title}
                  className="h-full w-full object-cover"
                  onError={(e) => {
                    // Fallback to abstract gradient if image fails to load
                    e.currentTarget.style.display = "none";
                  }}
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent opacity-60" />
                <span className="absolute bottom-4 left-4 rounded-full bg-slate-900/80 backdrop-blur-md px-3.5 py-1 text-xs font-semibold text-white shadow-sm">
                  {blog.category}
                </span>
              </div>
            )}

            {/* Meta Tags & Date */}
            <div className="mb-4 flex flex-wrap items-center gap-4 text-xs text-slate-500">
              <span className="inline-flex items-center gap-1.5 font-medium">
                <FiCalendar className="text-primary" />
                {blog.date}
              </span>
              <span className="inline-flex items-center gap-1.5 font-medium">
                <FiClock className="text-secondary" />
                {blog.readTime || "5 min read"}
              </span>
            </div>

            {/* Title */}
            <h1 className="font-display text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl md:text-4xl leading-tight">
              {blog.title}
            </h1>

            {/* Excerpt */}
            {blog.excerpt && (
              <p className="mt-4 text-base sm:text-lg font-normal leading-relaxed text-slate-600 border-l-4 border-primary/60 pl-4 italic bg-slate-50/70 py-2 rounded-r-xl">
                {blog.excerpt}
              </p>
            )}

            {/* Author Card */}
            <div className="mt-6 mb-8 flex items-center justify-between border-y border-slate-100 py-4">
              <div className="flex items-center gap-3">
                <img
                  src={blog.author?.avatar || "https://github.com/Huzaifa-Sheikh7687.png"}
                  alt={blog.author?.name || "Huzaifa Sheikh"}
                  className="h-11 w-11 rounded-full border-2 border-primary/20 object-cover"
                />
                <div>
                  <h4 className="text-sm font-semibold text-slate-900">
                    {blog.author?.name || "Huzaifa Sheikh"}
                  </h4>
                  <p className="text-xs text-slate-500">
                    {blog.author?.role || "Data Analyst & AI Engineer"}
                  </p>
                </div>
              </div>

              {/* Social Share Buttons */}
              <div className="flex items-center gap-2">
                <a
                  href={`https://api.whatsapp.com/send?text=${encodeURIComponent(
                    `${blog.title} - Read more: ${currentUrl}`
                  )}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Share on WhatsApp"
                  className="rounded-full p-2 text-emerald-600 hover:bg-emerald-50 transition"
                >
                  <FaWhatsapp size={18} />
                </a>
                <a
                  href={`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(
                    currentUrl
                  )}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Share on LinkedIn"
                  className="rounded-full p-2 text-blue-600 hover:bg-blue-50 transition"
                >
                  <FaLinkedin size={18} />
                </a>
                <a
                  href={`https://twitter.com/intent/tweet?text=${encodeURIComponent(
                    blog.title
                  )}&url=${encodeURIComponent(currentUrl)}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Share on X"
                  className="rounded-full p-2 text-slate-700 hover:bg-slate-100 transition"
                >
                  <FaTwitter size={18} />
                </a>
              </div>
            </div>

            {/* Markdown Body */}
            <div className="prose prose-slate max-w-none text-slate-700 leading-relaxed">
              <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                components={{
                  h1: ({ node, ...props }) => (
                    <h2
                      className="mt-8 mb-4 font-display text-2xl font-bold text-slate-900 border-b border-slate-100 pb-2"
                      {...props}
                    />
                  ),
                  h2: ({ node, ...props }) => (
                    <h2
                      className="mt-8 mb-4 font-display text-2xl font-bold text-slate-900"
                      {...props}
                    />
                  ),
                  h3: ({ node, ...props }) => (
                    <h3
                      className="mt-6 mb-3 font-display text-xl font-semibold text-slate-800"
                      {...props}
                    />
                  ),
                  p: ({ node, ...props }) => (
                    <p className="mb-5 text-base sm:text-lg leading-relaxed text-slate-700" {...props} />
                  ),
                  ul: ({ node, ...props }) => (
                    <ul className="mb-6 list-disc list-inside space-y-2 text-slate-700 pl-2" {...props} />
                  ),
                  ol: ({ node, ...props }) => (
                    <ol className="mb-6 list-decimal list-inside space-y-2 text-slate-700 pl-2" {...props} />
                  ),
                  li: ({ node, ...props }) => (
                    <li className="text-base sm:text-lg leading-relaxed" {...props} />
                  ),
                  blockquote: ({ node, ...props }) => (
                    <blockquote
                      className="my-6 border-l-4 border-primary bg-primary/5 py-3 px-5 text-slate-700 italic rounded-r-lg"
                      {...props}
                    />
                  ),
                  a: ({ node, ...props }) => (
                    <a
                      className="text-primary hover:underline font-medium inline-flex items-center gap-1"
                      target="_blank"
                      rel="noopener noreferrer"
                      {...props}
                    />
                  ),
                  code({ node, inline, className, children, ...props }) {
                    const match = /language-(\w+)/.exec(className || "");
                    const codeString = String(children).replace(/\n$/, "");

                    if (!inline) {
                      const codeId = Math.random();
                      return (
                        <div className="relative my-6 rounded-xl bg-slate-900 text-slate-100 shadow-lg overflow-hidden border border-slate-800">
                          <div className="flex items-center justify-between bg-slate-800/80 px-4 py-2 text-xs text-slate-400 font-mono-data">
                            <span>{match ? match[1].toUpperCase() : "CODE"}</span>
                            <button
                              onClick={() => handleCopyCode(codeString, codeId)}
                              className="inline-flex items-center gap-1 rounded px-2 py-1 hover:bg-slate-700 hover:text-white transition"
                            >
                              {codeCopiedIndex === codeId ? (
                                <>
                                  <FiCheck className="text-emerald-400" />
                                  <span className="text-emerald-400">Copied</span>
                                </>
                              ) : (
                                <>
                                  <FiCopy />
                                  <span>Copy</span>
                                </>
                              )}
                            </button>
                          </div>
                          <pre className="p-4 overflow-x-auto text-sm font-mono-data leading-relaxed">
                            <code className={className} {...props}>
                              {children}
                            </code>
                          </pre>
                        </div>
                      );
                    }
                    return (
                      <code
                        className="rounded bg-slate-100 px-1.5 py-0.5 font-mono-data text-xs text-secondary font-medium"
                        {...props}
                      >
                        {children}
                      </code>
                    );
                  },
                }}
              >
                {blog.content}
              </ReactMarkdown>
            </div>

            {/* Tags footer */}
            {blog.tags && blog.tags.length > 0 && (
              <div className="mt-10 border-t border-slate-100 pt-6">
                <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-3">
                  Topic Tags
                </h4>
                <div className="flex flex-wrap gap-2">
                  {blog.tags.map((tag) => (
                    <span
                      key={tag}
                      className="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-600"
                    >
                      #{tag}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* Bottom Author Box */}
            <div className="mt-10 rounded-2xl bg-gradient-to-br from-blue-50 to-purple-50 p-6 border border-blue-100/60">
              <div className="flex flex-col sm:flex-row items-center sm:items-start gap-4 text-center sm:text-left">
                <img
                  src={blog.author?.avatar || "https://github.com/Huzaifa-Sheikh7687.png"}
                  alt={blog.author?.name || "Huzaifa Sheikh"}
                  className="h-16 w-16 rounded-full border-2 border-white shadow-md object-cover"
                />
                <div>
                  <h3 className="font-display text-lg font-bold text-slate-900">
                    Written by {blog.author?.name || "Huzaifa Sheikh"}
                  </h3>
                  <p className="mt-1 text-sm text-slate-600">
                    Data Analyst, AI Engineer & Full Stack Developer. Passionate about machine learning, autonomous systems, and interactive data visualizations.
                  </p>
                  <div className="mt-3 flex flex-wrap gap-3 justify-center sm:justify-start">
                    <a
                      href="https://github.com/Huzaifa-Sheikh7687"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-1.5 text-xs font-semibold text-primary hover:underline"
                    >
                      GitHub Profile <FiExternalLink size={12} />
                    </a>
                    <a
                      href="https://www.linkedin.com/in/huzaifa-sheikh-7909142bb/"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-1.5 text-xs font-semibold text-secondary hover:underline"
                    >
                      LinkedIn Profile <FiExternalLink size={12} />
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </motion.article>
      </div>
    </AnimatePresence>
  );
}
