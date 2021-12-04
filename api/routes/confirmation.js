const fs = require('fs')
const { Router } = require('express')
const nodemailer = require('nodemailer')

const router = Router()

const format = function (text, args) {
  let newText = text
  for (const attr in args) {
    newText = newText.split('${' + attr + '}').join(args[attr])
  }
  return newText
}

const ulFromChildren = function (children) {
  const strings = children.map((child) => {
    return (
      '<li>' +
      child.firstName +
      ' ' +
      child.lastName +
      ', ' +
      child.age +
      ' Jahre</li>'
    )
  })
  return '<ul>' + strings.join('\n') + '</ul>'
}

const mailTemplate = fs
  .readFileSync(
    '/home/florian/Documents/KidsCamp/kidscamp_manager/api/confirmation-mail-template.html'
  )
  .toString()

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
      subject: 'Bestätigung Anmeldung KidsCamp ' + new Date().getFullYear(), // Subject line
      text: 'Anmdeldung KidsCamp', // plain text body
      html: format(mailTemplate, {
        name: req.body.firstName,
        children: ulFromChildren(req.body.children),
        amount: req.body.children.length * 50,
      }), // html body
    })
    .then((x) => console.log(x))
    .catch((e) => console.log('Error:', e))
  res.sendStatus(200)
})

module.exports = router
