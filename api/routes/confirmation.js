const fs = require('fs')
const { Router } = require('express')
const nodemailer = require('nodemailer')

const router = Router()

const getAmountInfo = function (nChildren) {
  if (nChildren === 1) {
    return '50€'
  } else {
    const amount = nChildren * 50
    return String(amount) + '€ (50€ pro Kind)'
  }
}

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
  .readFileSync('./api/confirmation-mail-template.html')
  .toString()

const transporter = nodemailer.createTransport({
  host: 'smtp.kidscamp.at',
  port: 465,
  secure: true, // true for 465, false for other ports
  auth: {
    user: process.env.CONFIRMATION_MAIL,
    pass: process.env.CONFIRMATION_MAIL_PASSWORD,
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
        amount: getAmountInfo(req.body.children.length),
      }), // html body
    })
    .then((x) => {
      res.statusCode = 200
      res.send({
        message: 'Successfully sent confirmation mail!',
        children: req.body.children,
        smtpResponse: x,
      })
    })
    .catch((e) => {
      res.statusCode = 500
      res.send(e)
    })
})

module.exports = router
