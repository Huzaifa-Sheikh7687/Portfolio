import { motion } from 'framer-motion'
import SectionHeading from './SectionHeading'
import { skillGroups, softSkills } from '../data/data'

function SkillBar({ name, level }) {
  return (
    <div>
      <div className="mb-1.5 flex justify-between text-sm text-white/70">
        <span>{name}</span>
        <span className="font-mono-data text-xs text-white/40">{level}%</span>
      </div>
      <div className="h-2 w-full overflow-hidden rounded-full bg-white/5">
        <motion.div
          className="h-full rounded-full bg-grad-primary"
          initial={{ width: 0 }}
          whileInView={{ width: `${level}%` }}
          viewport={{ once: true, amount: 0.6 }}
          transition={{ duration: 1, ease: 'easeOut' }}
        />
      </div>
    </div>
  )
}

export default function Skills() {
  return (
    <section id="skills" className="relative bg-ink py-28">
      <div className="mx-auto max-w-6xl px-6 md:px-8">
        <SectionHeading eyebrow="What I work with" title="Skills" />

        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {skillGroups.map((group, gi) => (
            <motion.div
              key={group.title}
              initial={{ opacity: 0, y: 24 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{ duration: 0.5, delay: gi * 0.08 }}
              className="glass rounded-2xl p-6"
            >
              <h3 className="mb-5 font-display text-sm font-semibold uppercase tracking-wide text-secondary">
                {group.title}
              </h3>
              <div className="space-y-4">
                {group.items.map((s) => (
                  <SkillBar key={s.name} {...s} />
                ))}
              </div>
            </motion.div>
          ))}
        </div>

        <motion.div
          initial={{ opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{ duration: 0.5 }}
          className="mt-10 flex flex-wrap justify-center gap-3"
        >
          {softSkills.map((s) => (
            <span
              key={s}
              className="glass rounded-full px-4 py-2 text-xs font-medium text-white/70"
            >
              {s}
            </span>
          ))}
        </motion.div>
      </div>
    </section>
  )
}
