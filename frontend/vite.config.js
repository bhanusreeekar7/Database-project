import { defineConfig } from 'vite'

// Same-origin proxy for local development. MySQL/FastAPI deployment is unchanged.
export default defineConfig({
  server: {
    proxy: {
      '/api': { target: 'http://127.0.0.1:8000', changeOrigin: true }
    }
  }
})
