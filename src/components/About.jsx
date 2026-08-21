import { motion } from 'framer-motion'
import { FiDatabase, FiCpu, FiCode, FiTarget, FiZap, FiUsers } from 'react-icons/fi'
import SectionHeading from './SectionHeading'
import { about } from '../data/data'

const iconMap = {
  data: FiDatabase,
  ai: FiCpu,
  code: FiCode,
  puzzle: FiTarget,
  spark: FiZap,
  team: FiUsers,
}

export default function About() {
  return (
    <section id="about" className="relative bg-surface py-28">
      <div className="mx-auto max-w-6xl px-6 md:px-8">
        <SectionHeading eyebrow="Get to know me" title="About Me" />

        <div className="grid grid-cols-1 gap-12 md:grid-cols-5">
          <motion.div
            initial={{ opacity: 0, x: -24 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.6 }}
            className="md:col-span-3 space-y-5"
          >
            {about.paragraphs.map((p, i) => (
              <p key={i} className="text-slate-600 leading-relaxed">
                {p}
              </p>
            ))}
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 24 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.6, delay: 0.1 }}
            className="grid grid-cols-2 gap-4 md:col-span-2"
          >
            {about.highlights.map(({ label, icon }) => {
              const Icon = iconMap[icon]
              return (
                <div
                  key={label}
                  className="glass flex flex-col items-center gap-2 rounded-2xl p-5 text-center transition-transform hover:-translate-y-1 hover:shadow-glow"
                >
                  <Icon className="text-2xl text-primary" />
                  <span className="text-xs font-medium text-slate-700">{label}</span>
                </div>
              )
            })}
          </motion.div>
        </div>
      </div>
    </section>
  )
}