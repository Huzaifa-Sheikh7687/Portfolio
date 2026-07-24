import { motion } from 'framer-motion'

export default function SectionHeading({ eyebrow, title, subtitle }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 24 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.4 }}
      transition={{ duration: 0.6, ease: 'easeOut' }}
      className="mx-auto mb-14 max-w-xl text-center"
    >
      {eyebrow && (
        <p className="section-eyebrow font-mono-data text-xs uppercase text-accent">{eyebrow}</p>
      )}
      <h2 className="mt-2 font-display text-3xl font-bold text-white sm:text-4xl">{title}</h2>
      {subtitle && <p className="mt-3 text-sm text-white/50">{subtitle}</p>}
    </motion.div>
  )
}
