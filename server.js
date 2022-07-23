const express = require('express')

const path = require('path')
const data = require('./data/merged_shoes.json')

const app = express()
const port = 3000

// define routes
const aboutRoute = require('./routes/about')
app.use('/about', aboutRoute)
const allShoesRoute = require('./routes/allShoes')
app.use('/all', allShoesRoute)

app.set('view engine', 'pug')
app.use(
  express.static(path.resolve(__dirname, 'node_modules/bootswatch/dist/darkly'))
)
app.use(express.static(path.resolve(__dirname, 'images')))
app.use(express.static(path.resolve(__dirname, 'js')))

// parse request bodies
app.use(express.json())

app.get('/', (_req, res) => {
  data.shoes.sort((a, b) => {
    return a.price - b.price
  })
  res.render('pages/index', {
    data: data,
  })
})

app.get('/some', (req, res) => {
  const start = parseInt(req.query.start)
  let some_shoes = data.shoes.slice(start, start + 100)
  const result = {
    shoes: some_shoes,
    brands: data.brands,
    count: some_shoes.length,
    total_count: data.shoes.length,
  }
  res.render('pages/index', { data: result })
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
