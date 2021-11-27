export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'kidscamp_application',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    script: [
      {
        src: 'https://kit.fontawesome.com/f697b56d87.js',
        crossorigin: 'anonymous',
      },
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~plugins/core-components.js' },
    { src: '~plugins/apex-charts.js', mode: 'client' },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    '@nuxtjs/html-validator',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxt/http',
    [
      '@nuxtjs/firebase',
      {
        config: {
          apiKey: 'AIzaSyAc1Q1pdYvZnH9DuornwaZrrOb5WLs80PI',
          authDomain: 'camp-manager-a5d22.firebaseapp.com',
          databaseURL:
            'https://camp-manager-a5d22-default-rtdb.europe-west1.firebasedatabase.app',
          projectId: 'camp-manager-a5d22',
          storageBucket: 'camp-manager-a5d22.appspot.com',
          messagingSenderId: '621343721303',
          appId: '1:621343721303:web:4918c50d99629b4aae2012',
        },
        services: {
          auth: {
            persistence: 'local', // default
            initialize: {
              onAuthStateChangedAction: 'onAuthStateChangedAction',
              subscribeManually: false,
            },
            ssr: false, // default
          },
          database: true,
        },
      },
    ],
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseUrl: 'http://localhost:3000',
  },

  serverMiddleware: {
    '/api': '~/api',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},

  publicRuntimeConfig: {
    authSignInURL: process.env.AUTH_URL,
    authApiKey: process.env.AUTH_API_KEY,
    axios: {
      browserBaseUrl: process.env.API_URL_BROWSER,
    },
  },
  privateRuntimeConfig: {
    axios: {
      baseUrl: process.env.API_URL_BROWSER,
    },
  },
}
