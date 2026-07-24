import { useState } from "react";
import { motion } from "framer-motion";
import emailjs from "@emailjs/browser";
import {
  FiMail,
  FiMapPin,
  FiGithub,
  FiLinkedin,
  FiEye,
  FiDownload,
  FiSend,
} from "react-icons/fi";
import { FaWhatsapp } from "react-icons/fa6";
import SectionHeading from "./SectionHeading";
import { personal } from "../data/data";

// Replace these with your own EmailJS credentials from emailjs.com
const EMAILJS_SERVICE_ID = "service_dgbdcwq";
const EMAILJS_TEMPLATE_ID = "template_8300icr";
const EMAILJS_PUBLIC_KEY = "fOmgwW8qKaDIXMv0h";

function ContactItem({ href, icon: Icon, label, ariaLabel, external = true }) {
  return (
    <a
      href={href}
      target={external ? "_blank" : undefined}
      rel={external ? "noopener noreferrer" : undefined}
      aria-label={ariaLabel}
      className="glass flex cursor-pointer items-center gap-3 rounded-2xl p-4 transition-all duration-300 hover:-translate-y-1 hover:border-primary/40 hover:bg-white/10"
    >
      <Icon className="text-xl text-primary" />
      <span className="text-sm text-white/70">{label}</span>
    </a>
  );
}

export default function Contact() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    subject: "",
    message: "",
  });
  const [status, setStatus] = useState("idle"); // idle | sending | sent | error

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("sending");
    try {
      await emailjs.send(
        EMAILJS_SERVICE_ID,
        EMAILJS_TEMPLATE_ID,
        form,
        EMAILJS_PUBLIC_KEY,
      );
      setStatus("sent");
      setForm({ name: "", email: "", subject: "", message: "" });
    } catch (err) {
      console.error(err);
      setStatus("error");
    }
  };

  return (
    <section id="contact" className="relative bg-surface py-28">
      <div className="mx-auto max-w-5xl px-6 md:px-8">
        <SectionHeading
          eyebrow="Let's talk"
          title="Contact"
          subtitle="Open to internships, entry-level Data Science & AI roles, and collaborations"
        />

        <div className="grid grid-cols-1 gap-10 md:grid-cols-5">
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.55 }}
            className="md:col-span-2 space-y-4"
          >
            <ContactItem
              href={`mailto:${personal.email}`}
              icon={FiMail}
              label="Email"
              ariaLabel={`Send an email to ${personal.email}`}
              external={false}
            />
            <ContactItem
              href={personal.github}
              icon={FiGithub}
              label="GitHub"
              ariaLabel="Open GitHub profile in a new tab"
            />
            <ContactItem
              href={personal.linkedin}
              icon={FiLinkedin}
              label="LinkedIn"
              ariaLabel="Open LinkedIn profile in a new tab"
            />
            <ContactItem
              href={personal.whatsapp}
              icon={FaWhatsapp}
              label="WhatsApp"
              ariaLabel="Start a WhatsApp chat"
            />

            <div className="flex gap-3 pt-2">
              <a
                href={personal.resumeUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex flex-1 items-center justify-center gap-2 rounded-xl glass px-4 py-3 text-sm font-semibold text-white"
              >
                <FiEye /> View CV
              </a>
              <a
                href={personal.resumeUrl}
                download="Huzaifa_Sheikh_CV.pdf"
                className="btn-gradient inline-flex flex-1 items-center justify-center gap-2 rounded-xl px-4 py-3 text-sm font-semibold text-white"
              >
                <FiDownload /> Download CV
              </a>
            </div>
          </motion.div>

          <motion.form
            initial={{ opacity: 0, x: 20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.55 }}
            onSubmit={handleSubmit}
            className="glass md:col-span-3 space-y-4 rounded-2xl p-6"
          >
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
              <input
                required
                name="name"
                value={form.name}
                onChange={handleChange}
                placeholder="Your name"
                className="rounded-xl border border-white/10 bg-white/5 px-4 py-3 text-sm text-white placeholder-white/30 outline-none focus:border-accent"
              />
              <input
                required
                type="email"
                name="email"
                value={form.email}
                onChange={handleChange}
                placeholder="Your email"
                className="rounded-xl border border-white/10 bg-white/5 px-4 py-3 text-sm text-white placeholder-white/30 outline-none focus:border-accent"
              />
            </div>
            <input
              required
              name="subject"
              value={form.subject}
              onChange={handleChange}
              placeholder="Subject"
              className="w-full rounded-xl border border-white/10 bg-white/5 px-4 py-3 text-sm text-white placeholder-white/30 outline-none focus:border-accent"
            />
            <textarea
              required
              name="message"
              value={form.message}
              onChange={handleChange}
              rows={5}
              placeholder="Your message"
              className="w-full resize-none rounded-xl border border-white/10 bg-white/5 px-4 py-3 text-sm text-white placeholder-white/30 outline-none focus:border-accent"
            />
            <button
              type="submit"
              disabled={status === "sending"}
              className="btn-gradient inline-flex items-center gap-2 rounded-xl px-6 py-3 text-sm font-semibold text-white disabled:opacity-60"
            >
              <FiSend /> {status === "sending" ? "Sending..." : "Send Message"}
            </button>
            {status === "sent" && (
              <p className="text-sm text-accent">Message sent — thank you!</p>
            )}
            {status === "error" && (
              <p className="text-sm text-red-400">
                Couldn't send — add your EmailJS keys in Contact.jsx first.
              </p>
            )}
          </motion.form>
        </div>
      </div>
    </section>
  );
}
