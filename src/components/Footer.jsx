import { FiGithub, FiLinkedin, FiMail } from "react-icons/fi";
import { FaWhatsapp } from "react-icons/fa6";
import { personal } from "../data/data";

export default function Footer() {
  return (
    <footer className="border-t border-white/5 bg-ink py-10">
      <div className="mx-auto flex max-w-6xl flex-col items-center gap-4 px-6 text-center md:flex-row md:justify-between md:px-8 md:text-left">
        <p className="font-display text-sm text-white/50">
          © 2026 {personal.name}. All Rights Reserved.
        </p>
        <div className="flex gap-4">
          <a
            href={`mailto:${personal.email}`}
            className="text-white/50 hover:text-primary"
          >
            <FiMail size={18} />
          </a>
          <a
            href={personal.github}
            target="_blank"
            rel="noopener noreferrer"
            className="text-white/50 hover:text-primary"
          >
            <FiGithub size={18} />
          </a>
          <a
            href={personal.linkedin}
            target="_blank"
            rel="noopener noreferrer"
            className="text-white/50 hover:text-primary"
          >
            <FiLinkedin size={18} />
          </a>
          <a
            href={personal.whatsapp}
            target="_blank"
            rel="noopener noreferrer"
            className="text-white/50 hover:text-primary"
          >
            <FaWhatsapp size={18} />
          </a>
        </div>
      </div>
    </footer>
  );
}
