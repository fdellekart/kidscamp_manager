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
    .then(() => {
      res.statusCode = 200
      res.send({
        message: 'Successfully added application!',
        child: req.body.child,
        parent: req.body.parent,
      })
    })
    .catch((e) => {
      res.statusCode = 500
      res.send(e)
    })
})

module.exports = router
