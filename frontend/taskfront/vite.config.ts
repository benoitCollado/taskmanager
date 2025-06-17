import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: true,         // Pour être accessible depuis l'extérieur
    port: 5173,              // Change si besoin
    strictPort: true,        // Pour forcer le port
    cors: true,              // Active CORS globalement
    allowedHosts: ['all'],   // Autorise tous les hôtes pour Replit
  }
})
