const { Router } = require('express')
const excel = require('exceljs')

const router = Router()

// Mock Users
const users = [{ name: 'Alexandre' }, { name: 'Pooya' }, { name: 'Sébastien' }]

/* GET users listing. */
router.get('/users', function (req, res, next) {
  res.json(users)
})

/* GET user by ID. */
router.get('/users/:id', function (req, res, next) {
  const id = parseInt(req.params.id)
  if (id >= 0 && id < users.length) {
    res.json(users[id])
  } else {
    res.sendStatus(404)
  }
})

router.post('/downloads/applications/excel', function (req, res, next) {
  const workbook = new excel.Workbook()
  const worksheet = workbook.addWorksheet('Anmeldungen')

  worksheet.columns = [
    { header: 'Vorname', key: 'first-name', width: 5 },
    { header: 'Nachname', key: 'last-name', width: 25 },
  ]
  worksheet.addRow(['Max', 'Mustermann'])

  res.setHeader(
    'Content-Type',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
  )
  res.setHeader(
    'Content-Disposition',
    'attachment; filename=' + 'tutorials.xlsx'
  )

  return workbook.xlsx.write(res).then(function () {
    res.status(200).end()
  })
})

module.exports = router
