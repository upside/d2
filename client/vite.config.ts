import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    proxy: {
      // Backend API
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
      // Mercure hub (SSE). Keeping same-origin via proxy reduces CORS pain.
      '/.well-known/mercure': {
        target: 'http://localhost:8080',
        changeOrigin: true,
      },
    },
  },
})
