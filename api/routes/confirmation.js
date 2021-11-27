const { Router } = require('express')
const nodemailer = require('nodemailer')

const router = Router()

const transporter = nodemailer.createTransport({
  host: 'smtp.kidscamp.at',
  port: 465,
  secure: true, // true for 465, false for other ports
  auth: {
    user: process.env.CONFIRMATION_MAIL, // generated ethereal user
    pass: process.env.CONFIRMATION_MAIL_PASSWORD, // generated ethereal password
  },
  tls: {
    rejectUnauthorized: false,
  },
})

router.post('/application/confirm', function (req, res, next) {
  transporter
    .sendMail({
      from: '"KidsCamp Anmeldung" <noreply@kidscamp.at>', // sender address
      to: req.body.mail, // list of receivers
      subject: 'Hello ✔', // Subject line
      text: 'Hello world?', // plain text body
      html: '<b>Hello world?</b>', // html body
    })
    .then((x) => console.log(x))
    .catch((e) => console.log('Error:', e))
  res.sendStatus(200)
})

module.exports = router
