const express = require('express')
const router = express.Router()

router.get('/', (req, res) => {
  const data = require('../data/merged_shoes.json')
  const start = parseInt(req.query.start)
  let some_shoes = data.shoes.slice(start, start + 100)
  const result = {
    shoes: some_shoes,
    brands: data.brands,
    count: some_shoes.length,
    total_count: data.shoes.length,
  }
  res.render('../views/pages/index', { data: result })
})

module.exports = router
