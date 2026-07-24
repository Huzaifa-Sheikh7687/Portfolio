import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { FiMenu, FiX } from "react-icons/fi";
import useActiveSection from "../hooks/useActiveSection";

const links = [
  { id: "home", label: "Home" },
  { id: "about", label: "About" },
  { id: "skills", label: "Skills" },
  { id: "experience", label: "Experience" },
  { id: "projects", label: "Projects" },
  { id: "education", label: "Education" },
  { id: "contact", label: "Contact" },
];

export default function Navbar() {
  const [open, setOpen] = useState(false);
  const active = useActiveSection(links.map((l) => l.id));

  const handleClick = (id) => {
    setOpen(false);
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <header className="fixed top-0 z-40 w-full">
      <nav className="glass mx-auto mt-3 flex max-w-6xl items-center justify-between rounded-2xl px-5 py-3 md:px-8">
        <button
          onClick={() => handleClick("home")}
          className="font-display text-lg font-semibold tracking-tight text-white"
        >
          <span className="text-gradient">PORTFOLIO</span>
        </button>

        <ul className="hidden items-center gap-1 md:flex">
          {links.map((l) => (
            <li key={l.id}>
              <button
                onClick={() => handleClick(l.id)}
                className={`relative rounded-full px-4 py-2 text-sm font-medium transition-colors ${
                  active === l.id
                    ? "text-white"
                    : "text-white/60 hover:text-white"
                }`}
              >
                {active === l.id && (
                  <motion.span
                    layoutId="nav-pill"
                    className="absolute inset-0 rounded-full bg-white/10"
                    transition={{ type: "spring", stiffness: 400, damping: 30 }}
                  />
                )}
                <span className="relative">{l.label}</span>
              </button>
            </li>
          ))}
        </ul>

        <button
          className="text-white md:hidden"
          onClick={() => setOpen((o) => !o)}
          aria-label="Toggle navigation menu"
        >
          {open ? <FiX size={22} /> : <FiMenu size={22} />}
        </button>
      </nav>

      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className="glass-strong mx-auto mt-2 flex max-w-6xl flex-col rounded-2xl p-4 md:hidden"
          >
            {links.map((l) => (
              <button
                key={l.id}
                onClick={() => handleClick(l.id)}
                className={`rounded-lg px-4 py-3 text-left text-sm font-medium ${
                  active === l.id ? "bg-white/10 text-white" : "text-white/70"
                }`}
              >
                {l.label}
              </button>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
