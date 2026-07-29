import { motion } from "framer-motion";
import { FiExternalLink, FiGithub } from "react-icons/fi";
import SectionHeading from "./SectionHeading";
import { projects } from "../data/data";
import { personal } from "../data/data";

export default function Projects() {
  return (
    <section id="projects" className="relative bg-ink py-28">
      <div className="mx-auto max-w-6xl px-6 md:px-8">
        <SectionHeading eyebrow="Selected work" title="Projects" />

        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2">
          {projects.map((p, i) => (
            <motion.div
              key={p.title}
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.25 }}
              transition={{ duration: 0.55, delay: (i % 2) * 0.1 }}
              className="glass group rounded-2xl p-6 transition-transform hover:-translate-y-1.5 hover:shadow-glowPurple"
            >
              <div className="mb-4 flex flex-wrap gap-2">
                {p.tags.map((t) => (
                  <span
                    key={t}
                    className="rounded-full bg-white/5 px-3 py-1 text-[11px] font-medium text-white/50"
                  >
                    {t}
                  </span>
                ))}
              </div>
              <h3 className="font-display text-xl font-semibold text-white">
                {p.title}
              </h3>
              <p className="mt-2 text-sm leading-relaxed text-white/60">
                {p.description}
              </p>

              <div className="mt-4 flex flex-wrap gap-2">
                {p.tech.map((t) => (
                  <span
                    key={t}
                    className="font-mono-data text-[11px] text-accent"
                  >
                    #{t.replace(/\s/g, "")}
                  </span>
                ))}
              </div>

              <div className="mt-6 flex gap-4 opacity-0 transition-opacity group-hover:opacity-100">
                <a
                  href={p.github}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1.5 text-sm text-white/70 hover:text-white"
                >
                  <FiGithub /> GitHub
                </a>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
