const express = require('express')
const path = require('path')

const homeRoute = require('./routes/partioned')
const aboutRoute = require('./routes/about')
const brandsRoute = require('./routes/brands')
const renderPage = require('./middleware/renderPage.js')

const app = express()
const port = 3000

app.set('view engine', 'pug')
app.use(
  express.static(path.resolve(__dirname, 'node_modules/bootswatch/dist/darkly'))
)
app.use(express.static(path.resolve(__dirname, 'images')))
app.use(express.static(path.resolve(__dirname, 'js')))

// parse request bodies
app.use(express.json())

// define routes
app.use('/', homeRoute)
app.use('/about', aboutRoute)
app.use('/brands', brandsRoute)
// render page w/ 100 shoes per page
app.use(renderPage)

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
