const express = require('express')
const router = express.Router()

router.use((req, res, next) => {
  const sortDirection = req.query.sort

  if (sortDirection) {
    const shoeData = res.locals.shoeData
    shoeData.shoes.sort((a, b) => {
      return a.price - b.price
    })
    // reverse sort if sorting high to low
    if (sortDirection == 'high') shoeData.shoes.reverse()
  }

  next()
})

module.exports = router
