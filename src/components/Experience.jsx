import { motion } from 'framer-motion'
import { FiBriefcase } from 'react-icons/fi'
import SectionHeading from './SectionHeading'
import { experience } from '../data/data'

export default function Experience() {
  return (
    <section id="experience" className="relative bg-surface py-28">
      <div className="mx-auto max-w-4xl px-6 md:px-8">
        <SectionHeading eyebrow="Where I've worked" title="Experience" />

        <div className="relative border-l border-slate-900/12 pl-8">
          {experience.map((exp, i) => (
            <motion.div
              key={exp.role}
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{ duration: 0.55, delay: i * 0.1 }}
              className="relative mb-12 last:mb-0"
            >
              <span className="absolute -left-[41px] flex h-8 w-8 items-center justify-center rounded-full bg-grad-primary text-white shadow-glow">
                <FiBriefcase size={14} />
              </span>
              <div className="glass rounded-2xl p-6">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <h3 className="font-display text-lg font-semibold text-slate-900">{exp.role}</h3>
                  <span className="font-mono-data text-xs text-accent">{exp.duration}</span>
                </div>
                <p className="mt-1 text-sm font-medium text-secondary">{exp.org}</p>
                <ul className="mt-4 space-y-2">
                  {exp.points.map((pt) => (
                    <li key={pt} className="flex gap-2 text-sm text-slate-600">
                      <span className="mt-1.5 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-primary" />
                      {pt}
                    </li>
                  ))}
                </ul>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}