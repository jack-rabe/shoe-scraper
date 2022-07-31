const express = require('express')
const path = require('path')

const homeRoute = require('./routes/partioned')
const aboutRoute = require('./routes/about')
const brandsRoute = require('./routes/brands')

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
app.use((req, res) => {
  const shoeData = res.locals.shoeData
  let start = parseInt(req.query.start)
  // start at 0 index by default
  if (!start) start = 0
  const someShoes = shoeData.shoes.slice(start, start + 100)
  const result = {
    shoes: someShoes,
    brands: shoeData.brands,
    count: someShoes.length,
    total_count: shoeData.shoes.length,
  }
  res.render('../views/pages/index', { data: result })
})

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
