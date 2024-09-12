/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.{html,js}",
  ],
  theme: {
    extend: {
      colors: {
        'darkest': '#45474B',
        'light': '#F5F7F8',
        'secondary': '#F4CE14',
        'dark': '#495E57',
      }
    },
  },
  plugins: [],
}

