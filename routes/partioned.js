const express = require('express')
const router = express.Router()

router.get('/', (_req, res, next) => {
  const data = require('../data/merged_shoes.json')
  res.locals.shoeData = data
  next()
})

module.exports = router
