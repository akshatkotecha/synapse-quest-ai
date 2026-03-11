/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'cyber-black': '#0a0a0f',
        'cyber-gray': '#13131f',
        'neon-blue': '#00f3ff',
        'neon-purple': '#bc13fe',
        'neon-red': '#ff003c',
        'glass': 'rgba(255, 255, 255, 0.05)',
      },
      fontFamily: {
        mono: ['"JetBrains Mono"', 'monospace'], 
      },
    },
  },
  plugins: [],
}