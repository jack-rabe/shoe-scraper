const express = require('express')
const router = express.Router()

router.use((req, res) => {
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
    current_brand: shoeData.current_brand || 'All',
  }
  res.render('../views/pages/index', { data: result })
})

module.exports = router
