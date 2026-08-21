import { motion } from 'framer-motion'
import { FiBookOpen } from 'react-icons/fi'
import SectionHeading from './SectionHeading'
import { education } from '../data/data'

export default function Education() {
  return (
    <section id="education" className="relative bg-surface py-28">
      <div className="mx-auto max-w-5xl px-6 md:px-8">
        <SectionHeading eyebrow="My academic path" title="Education" />

        <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
          {education.map((ed, i) => (
            <motion.div
              key={ed.degree}
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{ duration: 0.5, delay: i * 0.1 }}
              className="glass flex flex-col rounded-2xl p-6"
            >
              <FiBookOpen className="mb-3 text-2xl text-primary" />
              <h3 className="font-display text-base font-semibold text-slate-900">{ed.degree}</h3>
              <p className="mt-1 text-sm text-secondary">{ed.school}</p>
              <p className="mt-3 font-mono-data text-xs text-accent">{ed.duration}</p>
              <p className="mt-1 text-sm text-slate-600">{ed.detail}</p>
              {ed.focus && (
                <div className="mt-4 flex flex-wrap gap-2">
                  {ed.focus.map((f) => (
                    <span
                      key={f}
                      className="rounded-full bg-slate-900/5 px-3 py-1 text-[11px] text-slate-500"
                    >
                      {f}
                    </span>
                  ))}
                </div>
              )}
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}