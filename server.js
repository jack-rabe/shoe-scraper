const express = require('express')
const path = require('path')

const homeRoute = require('./routes/partioned')
const aboutRoute = require('./routes/about')
const brandsRoute = require('./routes/brands')
// middleware
const sortShoes = require('./middleware/sortShoes')
const renderPage = require('./middleware/renderPage')

const app = express()
const port = process.env.PORT || 3000

app.set('view engine', 'pug')
app.use(
  express.static(
    path.resolve(__dirname, 'node_modules/bootswatch/dist/journal')
  )
)
app.use(express.static(path.resolve(__dirname, 'images')))
app.use(express.static(path.resolve(__dirname, 'js')))

// parse request bodies
app.use(express.json())
// specify that there is no favicon
app.get('/favicon.ico', (_req, res) => res.status(204).end())

// define routes
app.use('/', homeRoute)
app.use('/about', aboutRoute)
app.use('/brands', brandsRoute)
// sort shoes from low -> high or vice versa if specified
app.use(sortShoes)
// render page w/ 52 shoes per page
app.use(renderPage)

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
