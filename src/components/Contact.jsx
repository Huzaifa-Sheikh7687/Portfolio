import { useState } from "react";
import { motion } from "framer-motion";
import emailjs from "@emailjs/browser";
import {
  FiMail,
  FiGithub,
  FiLinkedin,
  FiEye,
  FiDownload,
  FiSend,
} from "react-icons/fi";
import { FaWhatsapp } from "react-icons/fa6";
import SectionHeading from "./SectionHeading";
import { personal } from "../data/data";

// EmailJS credentials
const EMAILJS_SERVICE_ID = "service_dgbdcwq";
const EMAILJS_TEMPLATE_ID = "template_8300icr";
const EMAILJS_PUBLIC_KEY = "fOmgwW8qKaDIXMv0h";

function ContactItem({
  href,
  icon: Icon,
  label,
  ariaLabel,
  external = true,
}) {
  return (
    <a
      href={href}
      target={external ? "_blank" : undefined}
      rel={external ? "noopener noreferrer" : undefined}
      aria-label={ariaLabel}
      className="glass flex cursor-pointer items-center gap-3 rounded-2xl p-4 transition-all duration-300 hover:-translate-y-1 hover:border-primary/40 hover:bg-slate-900/5"
    >
      <Icon className="text-xl text-primary" />
      <span className="text-sm text-slate-600">{label}</span>
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

  const [status, setStatus] = useState("idle");

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("sending");

    try {
      await emailjs.send(
        EMAILJS_SERVICE_ID,
        EMAILJS_TEMPLATE_ID,
        form,
        EMAILJS_PUBLIC_KEY
      );

      setStatus("sent");

      setForm({
        name: "",
        email: "",
        subject: "",
        message: "",
      });
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
          {/* Contact Links */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.55 }}
            className="space-y-4 md:col-span-2"
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

            {/* CV Buttons */}
            <div className="flex gap-3 pt-2">
              <a
                href={personal.resumeUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex flex-1 items-center justify-center gap-2 rounded-xl glass px-4 py-3 text-sm font-semibold text-slate-900"
              >
                <FiEye />
                View CV
              </a>

              <a
                href={personal.resumeUrl}
                download="Huzaifa_Sheikh_CV.pdf"
                className="btn-gradient inline-flex flex-1 items-center justify-center gap-2 rounded-xl px-4 py-3 text-sm font-semibold text-white"
              >
                <FiDownload />
                Download CV
              </a>
            </div>
          </motion.div>

          {/* Contact Form */}
          <motion.form
            initial={{ opacity: 0, x: 20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.55 }}
            onSubmit={handleSubmit}
            className="glass space-y-4 rounded-2xl p-6 md:col-span-3"
          >
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
              <input
                required
                name="name"
                value={form.name}
                onChange={handleChange}
                placeholder="Your name"
                className="rounded-xl border border-slate-900/10 bg-slate-900/[0.03] px-4 py-3 text-sm text-slate-900 placeholder-slate-400 outline-none focus:border-accent"
              />

              <input
                required
                type="email"
                name="email"
                value={form.email}
                onChange={handleChange}
                placeholder="Your email"
                className="rounded-xl border border-slate-900/10 bg-slate-900/[0.03] px-4 py-3 text-sm text-slate-900 placeholder-slate-400 outline-none focus:border-accent"
              />
            </div>

            <input
              required
              name="subject"
              value={form.subject}
              onChange={handleChange}
              placeholder="Subject"
              className="w-full rounded-xl border border-slate-900/10 bg-slate-900/[0.03] px-4 py-3 text-sm text-slate-900 placeholder-slate-400 outline-none focus:border-accent"
            />

            <textarea
              required
              name="message"
              value={form.message}
              onChange={handleChange}
              rows={5}
              placeholder="Your message"
              className="w-full resize-none rounded-xl border border-slate-900/10 bg-slate-900/[0.03] px-4 py-3 text-sm text-slate-900 placeholder-slate-400 outline-none focus:border-accent"
            />

            <button
              type="submit"
              disabled={status === "sending"}
              className="btn-gradient inline-flex items-center gap-2 rounded-xl px-6 py-3 text-sm font-semibold text-white disabled:opacity-60"
            >
              <FiSend />
              {status === "sending" ? "Sending..." : "Send Message"}
            </button>

            {status === "sent" && (
              <p className="text-sm text-accent">
                Message sent — thank you!
              </p>
            )}

            {status === "error" && (
              <p className="text-sm text-red-600">
                Couldn't send — add your EmailJS keys in Contact.jsx first.
              </p>
            )}
          </motion.form>
        </div>
      </div>
    </section>
  );
}