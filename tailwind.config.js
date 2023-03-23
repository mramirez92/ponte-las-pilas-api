/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
        fontFamily: {
            sans: ['"Work Sans"',"sans-serif"],
            urban: ["Urbanist"],
            // work:['"Work Sans"']
        }
    },
  },
  plugins: [],
}
