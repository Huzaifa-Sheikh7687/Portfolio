import { motion, AnimatePresence } from "framer-motion";

export default function Loader({ show }) {
  return (
    <AnimatePresence>
      {show && (
        <motion.div
          className="fixed inset-0 z-[100] flex items-center justify-center bg-ink"
          initial={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.6, ease: "easeInOut" }}
        >
          <div className="flex flex-col items-center gap-4">
            <motion.div
              className="font-mono-data text-sm text-accent tracking-widest"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.1 }}
            >
              <span className="query-label">
                Welcome to Huzaifa's Portfolio
              </span>
            </motion.div>
            <div className="h-1 w-48 overflow-hidden rounded-full bg-white/10">
              <motion.div
                className="h-full bg-grad-primary"
                initial={{ x: "-100%" }}
                animate={{ x: "100%" }}
                transition={{
                  repeat: Infinity,
                  duration: 1.1,
                  ease: "easeInOut",
                }}
              />
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
