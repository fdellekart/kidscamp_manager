const express = require('express')
const firebase = require('firebase')

const firebaseConfig = {
  apiKey: process.env.AUTH_API_KEY,
  authDomain: process.env.FIREBASE_AUTH_DOMAIN,
  databaseURL: process.env.FIREBASE_URL,
  projectId: process.env.FIREBASE_PROJECT_ID,
  storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.FIREBASE_APP_ID,
}

// Initialize Firebase
firebase.initializeApp(firebaseConfig)

firebase // Authenticate for firebase
  .auth()
  .signInWithEmailAndPassword(
    process.env.FIREBASE_USER,
    process.env.FIREBASE_PW
  )
  .then((user) => {
    console.log('Logged into firbase successfully!')
  })

// Create express instance
const app = express()

// Require API routes
const download = require('./routes/download')
const confirmation = require('./routes/confirmation')
const applications = require('./routes/applications')

app.use(express.json())

// Import API Routes
app.use(download)
app.use(confirmation)
app.use(applications)

// Export express app
module.exports = app

// Start standalone server if directly running
if (require.main === module) {
  const port = process.env.PORT || 3001
  app.listen(port, () => {
    // eslint-disable-next-line no-console
    console.log(`API server listening on port ${port}`)
  })
}
