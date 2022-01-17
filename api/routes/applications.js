const { Router } = require('express')
const firebase = require('firebase')

const router = Router()

router.post('/application/add', function (req, res, next) {
  const newApplicationKey = firebase
    .database()
    .ref()
    .child('applications')
    .push().key
  const updates = {}
  updates['/applications/' + newApplicationKey] = {
    parent: req.body.parent,
    child: req.body.child,
    created: new Date().toISOString(),
  }
  firebase
    .database()
    .ref()
    .update(updates)
    .then((s) => {
      res.write(s)
      res.sendStatus(200)
    })
    .catch(() => {
      res.sendStatus(500)
    })
})

module.exports = router
