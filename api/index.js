const express = require('express')

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
