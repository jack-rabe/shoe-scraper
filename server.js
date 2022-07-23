const express = require('express')
const path = require('path')

const aboutRoute = require('./routes/about')
const allShoesRoute = require('./routes/allShoes')
const someBrandsRoute = require('./routes/someBrands')
const homeRoute = require('./routes/home')

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
app.use('/about', aboutRoute)
app.use('/all', allShoesRoute)
app.use('/someBrands', someBrandsRoute)
app.use('/', homeRoute)

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
