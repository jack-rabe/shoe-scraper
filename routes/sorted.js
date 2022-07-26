const express = require('express')
const router = express.Router()

router.get('/', (_req, res) => {
  const data = require('../data/merged_shoes.json')
  data.shoes.sort((a, b) => {
    return a.price - b.price
  })
  res.render('pages/index', {
    data: data,
  })
})

module.exports = router
