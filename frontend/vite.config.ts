import { defineConfig } from "@lovable.dev/vite-tanstack-config";

export default defineConfig({
  tanstackStart: {
    server: { entry: "server" },
  },
  vite: {
    // Add custom Vite configurations here without overriding base plugins
    server: {
      open: true,
    },
  },
});
