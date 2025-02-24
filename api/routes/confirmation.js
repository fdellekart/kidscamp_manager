const fs = require('fs')
const { Router } = require('express')
const nodemailer = require('nodemailer')

const router = Router()

const getAmountInfo = function (nChildren) {
  if (nChildren === 1) {
    return '100€'
  } else {
    const amount = nChildren * 100
    return String(amount) + '€ (100€ pro Kind)'
  }
}

const getSiblingsInfo = function (nChildren) {
  if (nChildren > 1) {
    return 'Falls die angemeldeten Kinder Geschwister sind, kann ab dem zweiten Kind ein Geschwisterrabatt von 10€ abgezogen werden.'
  } else {
    return ''
  }
}

const getSpareAmountInfo = function (nChildren) {
  const amount = nChildren * 70
  return String(amount) + '€'
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

const applicationAttachementFile = function (nChildren) {
  if (nChildren < 4) {
    return './api/Anmeldung_2024_pdf_' + String(nChildren) + 'Kinder.pdf'
  } else {
    return './api/Anmeldung_2024_pdf_3Kinder.pdf'
  }
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
        spareAmount: getSpareAmountInfo(req.body.children.length),
        siblingsInfo: getSiblingsInfo(req.body.children.length),
      }), // html body
      replyTo: 'kontakt@kidscamp.at',
      attachments: [
        {
          filename: 'Anmeldeformular_KidsCamp2024.pdf',
          path: applicationAttachementFile(req.body.children.length),
        },
        {
          filename: 'Medikamentengabe_KidsCamp2024.pdf',
          path: './api/Medikamentengabe_2024.pdf',
        },
        {
          filename: 'Medikamentengabe_ARZT.pdf',
          path: './api/Medikamentengabe-ARZT.pdf',
        },
        {
          filename: 'Packliste_KidsCamp.pdf',
          path: './api/Packliste_KidsCamp.pdf',
        },
      ],
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
