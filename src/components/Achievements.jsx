import { motion } from 'framer-motion'
import { FiAward } from 'react-icons/fi'
import SectionHeading from './SectionHeading'
import { achievements } from '../data/data'

export default function Achievements() {
  return (
    <section id="achievements" className="relative bg-ink py-24">
      <div className="mx-auto max-w-6xl px-6 md:px-8">
        <SectionHeading eyebrow="Milestones" title="Achievements" />
        <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {achievements.map((a, i) => (
            <motion.div
              key={a.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{ duration: 0.45, delay: (i % 3) * 0.08 }}
              className="glass flex items-start gap-4 rounded-2xl p-5"
            >
              <span className="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-xl bg-grad-primary text-white">
                <FiAward size={16} />
              </span>
              <div>
                <h3 className="font-display text-sm font-semibold text-slate-900">{a.title}</h3>
                <p className="mt-1 text-xs text-slate-500">{a.desc}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}