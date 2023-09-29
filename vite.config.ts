import { fileURLToPath, URL } from 'node:url'
import Components from 'unplugin-vue-components/vite';
import { AntDesignVueResolver } from 'unplugin-vue-components/resolvers';
import Markdown from 'unplugin-vue-markdown/vite'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({
      include: [/\.vue$/, /\.md$/],
    }),
    Components({
      extensions: ['vue', 'md'],
      resolvers: [AntDesignVueResolver({
        importStyle: false, // css in js
      })],
    }),
    Markdown({}),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: {
    sourcemap: true,
  },
})
