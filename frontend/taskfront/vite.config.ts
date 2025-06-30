
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from 'vite-plugin-vuetify'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vuetify({autoImport:true})
  ],
  server: {
    port: 3000,
    host: '0.0.0.0',
    allowedHosts:["08ca1522-3fb3-455c-9248-e538a904d79d-00-ijrqs1e7cp1.spock.replit.dev"]
  }
})
