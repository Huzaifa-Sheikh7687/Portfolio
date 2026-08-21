import { useEffect, useRef } from "react";
import Typed from "typed.js";
import { motion } from "framer-motion";
import { FiEye, FiDownload } from "react-icons/fi";
import { SiPython, SiReact, SiTensorflow, SiMysql } from "react-icons/si";
import { FaChartBar } from "react-icons/fa6";
import ParticlesBackground from "./ParticlesBackground";
import { personal } from "../data/data";

const floatIcons = [
  { Icon: SiPython, className: "top-[12%] left-[8%]", delay: 0 },
  { Icon: SiReact, className: "top-[65%] left-[4%]", delay: 0.6 },
  { Icon: SiTensorflow, className: "top-[20%] right-[6%]", delay: 1.1 },
  { Icon: SiMysql, className: "top-[70%] right-[10%]", delay: 1.6 },
  { Icon: FaChartBar, className: "top-[42%] right-[2%]", delay: 2 },
];

export default function Hero() {
  const typedEl = useRef(null);

  useEffect(() => {
    const typed = new Typed(typedEl.current, {
      strings: personal.typedRoles,
      typeSpeed: 55,
      backSpeed: 30,
      backDelay: 1400,
      loop: true,
    });

    return () => typed.destroy();
  }, []);

  return (
    <section
      id="home"
      className="relative flex min-h-screen items-center overflow-hidden bg-ink bg-grad-radial pt-28"
    >
      <ParticlesBackground />

      {floatIcons.map(({ Icon, className, delay }, i) => (
        <motion.div
          key={i}
          className={`absolute hidden text-3xl text-slate-900/10 md:block ${className}`}
          animate={{ y: [0, -18, 0] }}
          transition={{
            duration: 5,
            delay,
            repeat: Infinity,
            ease: "easeInOut",
          }}
        >
          <Icon />
        </motion.div>
      ))}

      <div className="relative z-10 mx-auto grid max-w-6xl grid-cols-1 items-center gap-12 px-6 md:grid-cols-2 md:px-8">
        <motion.div
          initial={{ opacity: 0, y: 24 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7, ease: "easeOut" }}
        >
          <p className="section-eyebrow font-mono-data text-xs uppercase text-accent">
            Hi, my name is
          </p>

          <h1 className="mt-3 font-display text-5xl font-bold leading-tight text-slate-900 sm:text-6xl">
            {personal.name}
          </h1>

          <h2 className="mt-3 font-display text-xl font-medium text-slate-700 sm:text-2xl">
            <span ref={typedEl} className="text-gradient" />
          </h2>

          <p className="mt-6 max-w-lg text-base leading-relaxed text-slate-600">
            {personal.tagline}
          </p>

          <div className="mt-9 flex flex-wrap gap-4">
            {/* View CV */}
            <a
              href={personal.resumeUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-xl glass px-6 py-3 text-sm font-semibold text-slate-900 transition-transform hover:scale-105"
            >
              <FiEye />
              View CV
            </a>

            {/* Download CV */}
            <a
              href={personal.resumeUrl}
              download="Huzaifa_Sheikh_CV.pdf"
              className="btn-gradient inline-flex items-center gap-2 rounded-xl px-6 py-3 text-sm font-semibold text-white"
            >
              <FiDownload />
              Download CV
            </a>

            {/* Contact Me */}
            <button
              onClick={() =>
                document
                  .getElementById("contact")
                  ?.scrollIntoView({ behavior: "smooth" })
              }
              className="inline-flex items-center gap-2 rounded-xl border border-slate-900/15 px-6 py-3 text-sm font-semibold text-slate-700 transition-colors hover:border-accent hover:text-slate-900"
            >
              Contact Me
            </button>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.85 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{
            duration: 0.8,
            ease: "easeOut",
            delay: 0.2,
          }}
          className="relative mx-auto flex h-72 w-72 items-center justify-center sm:h-96 sm:w-96"
        >
          <div className="absolute inset-0 animate-pulseSlow rounded-full bg-grad-primary blur-3xl opacity-30" />

          <div className="glass-strong relative flex h-full w-full items-center justify-center overflow-hidden rounded-full border border-slate-900/10">
            <img
              src="/profile-pic.png"
              alt={personal.name}
              className="h-full w-full rounded-full object-cover"
            />
          </div>
        </motion.div>
      </div>
    </section>
  );
}