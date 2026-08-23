import { motion } from 'framer-motion'
import { FiFileText, FiExternalLink, FiCheckCircle } from 'react-icons/fi'
import SectionHeading from './SectionHeading'
import { certificates } from '../data/data'

export default function Certificates() {
  return (
    <section id="certificates" className="relative bg-surface py-28">
      <div className="mx-auto max-w-4xl px-6 md:px-8">
        <SectionHeading eyebrow="Proof of work" title="Certificates" />

        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {certificates.map((cert, i) => (
            <motion.a
              key={cert.title}
              href={cert.file}
              target="_blank"
              rel="noopener noreferrer"
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{ duration: 0.5, delay: (i % 3) * 0.08 }}
              className="glass group relative flex flex-col items-center gap-3 overflow-hidden rounded-2xl p-6 text-center transition-transform hover:-translate-y-1.5 hover:shadow-glowPurple"
            >
              {/* verified badge */}
              <span className="absolute right-3 top-3 flex items-center gap-1 rounded-full bg-emerald-500/10 px-2.5 py-1 text-[10px] font-semibold text-emerald-600">
                <FiCheckCircle size={11} />
                Verified
              </span>

              {/* top accent strip */}
              <span className="absolute inset-x-0 top-0 h-1 bg-grad-primary" />

              <span className="mt-2 flex h-16 w-16 flex-shrink-0 items-center justify-center rounded-2xl bg-grad-primary text-white shadow-glow">
                <FiFileText size={26} />
              </span>

              <div>
                <h3 className="font-display text-sm font-semibold text-slate-900">
                  {cert.previewLabel || 'Certificate Preview'}
                </h3>
                <p className="mt-1.5 text-sm font-medium text-slate-700">{cert.title}</p>
                {cert.org && (
                  <p className="mt-0.5 text-xs text-slate-500">{cert.org}</p>
                )}
              </div>

              {(cert.id || cert.date) && (
                <div className="flex flex-wrap items-center justify-center gap-1.5">
                  {cert.id && (
                    <span className="rounded-full bg-slate-900/5 px-2.5 py-1 font-mono-data text-[10px] text-slate-500">
                      {cert.id}
                    </span>
                  )}
                  {cert.date && (
                    <span className="rounded-full bg-slate-900/5 px-2.5 py-1 font-mono-data text-[10px] text-slate-500">
                      {cert.date}
                    </span>
                  )}
                </div>
              )}

              <span className="mt-2 inline-flex items-center gap-1.5 rounded-full bg-grad-primary px-4 py-2 font-mono-data text-xs font-medium text-white shadow-sm">
                Open PDF
                <FiExternalLink size={12} />
              </span>
            </motion.a>
          ))}
        </div>
      </div>
    </section>
  )
}