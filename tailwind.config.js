/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
        fontFamily: {
            sans: ['"Josefin Sans"',"sans-serif"],
            urban: ["Urbanist"],
            work:['"Work Sans"']
        }
    },
  },
  plugins: [],
}
