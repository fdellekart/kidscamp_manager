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
        const applications = req.body.children.map((child) => {
          return { parent: req.body.parent, child }
        })
        successFullCaptchaCallback(applications, res)
      } else {
        unsuccessfulCaptchaCallback(req, res)
      }
    })
})

function successFullCaptchaCallback(applications, res) {
  let returnValue
  const updates = {}
  applications.forEach((application) => {
    const newApplicationKey = firebase
      .database()
      .ref()
      .child('applications')
      .push().key

    updates['/applications/' + newApplicationKey] = {
      parent: application.parent,
      child: application.child,
      created: new Date().toISOString(),
    }
  })
  firebase
    .database()
    .ref()
    .update(updates)
    .then(() => {
      res.status = 200
      res.send({ message: 'Successfully added applications!' })
    })
    .catch((e) => {
      res.status = 500
      res.send({ error: e })
    })
  return returnValue
}

function unsuccessfulCaptchaCallback(req, res) {
  res.statusCode = 400
  res.send({ msg: 'reCaptcha not verified!' })
}

module.exports = router
