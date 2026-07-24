/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#3B82F6',
        secondary: '#8B5CF6',
        accent: '#06B6D4',
        ink: '#05070D',
        surface: '#0B0F1A',
        surface2: '#10162A',
      },
      fontFamily: {
        display: ['"Space Grotesk"', 'sans-serif'],
        body: ['"Inter"', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      backgroundImage: {
        'grad-primary': 'linear-gradient(135deg, #3B82F6 0%, #8B5CF6 50%, #06B6D4 100%)',
        'grad-radial': 'radial-gradient(circle at 50% 0%, rgba(59,130,246,0.18), transparent 60%)',
      },
      boxShadow: {
        glow: '0 0 40px -8px rgba(59,130,246,0.45)',
        glowPurple: '0 0 40px -8px rgba(139,92,246,0.45)',
      },
      keyframes: {
        float: {
          '0%,100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-16px)' },
        },
        pulseSlow: {
          '0%,100%': { opacity: 0.4 },
          '50%': { opacity: 0.9 },
        },
      },
      animation: {
        float: 'float 6s ease-in-out infinite',
        pulseSlow: 'pulseSlow 4s ease-in-out infinite',
      },
    },
  },
  plugins: [],
}
