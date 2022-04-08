const { Router } = require('express')
const firebase = require('firebase')
const axios = require('axios')

const router = Router()

router.post('/application/add', function (req, res, next) {
  const recaptchaToken = req.body.token
  axios
    .post('https://www.google.com/recaptcha/api/siteverify', null, {
      params: {
        secret: process.env.RECAPTCHA_SECRET_KEY,
        response: recaptchaToken,
      },
    })
    .then((captchaResponse) => {
      if (captchaResponse.data.success) {
        successFullCaptchaCallback(req, res)
      } else {
        unsuccessfulCaptchaCallback(req, res)
      }
    })
})

function successFullCaptchaCallback(req, res) {
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
}

function unsuccessfulCaptchaCallback(req, res) {
  res.statusCode = 400
  res.send({ msg: 'reCaptcha not verified!' })
}

module.exports = router
