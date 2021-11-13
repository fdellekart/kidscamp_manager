const { Router } = require('express')
const excel = require('exceljs')

const router = Router()

function excelRowsFromApplications(applications) {
  applications = Object.values(applications)
  return applications.map((app) => {
    return [
      app.child.firstName,
      app.child.lastName,
      app.child.age,
      app.parent.firstName + ' ' + app.parent.lastName,
      app.parent.mail,
    ]
  })
}

router.post('/downloads/applications/excel', function (req, res, next) {
  const workbook = new excel.Workbook()
  const worksheet = workbook.addWorksheet('Anmeldungen')

  worksheet.columns = [
    { header: 'Vorname', key: 'firstName', width: 25 },
    { header: 'Nachname', key: 'lastName', width: 25 },
    { header: 'Alter', key: 'age', width: 25 },
    { header: 'Erziehungsberechtiger', key: 'parent', width: 25 },
    { header: 'Mail', key: 'mail', width: 25 },
  ]

  const rows = excelRowsFromApplications(req.body)

  worksheet.addRows(rows)

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
