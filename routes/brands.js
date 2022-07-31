const express = require('express')
const router = express.Router()

router.get('/', (req, res, next) => {
  const data = require('../data/merged_shoes.json')
  let shoes = data['shoes']
  let selectedBrands = req.query.brand
  // ensure selectedBrands is an array
  if (typeof selectedBrands == 'string') selectedBrands = [selectedBrands]
  // split the selected brands w/ a space + comma
  const prettyBrandsStr = selectedBrands.join(', ')

  shoes = shoes.filter((shoe) => {
    return selectedBrands.includes(shoe.brand)
  })
  const result = {
    shoes: shoes,
    brands: data.brands,
    current_brand: prettyBrandsStr,
    count: shoes.length,
  }

  res.locals.shoeData = result
  next()
})

module.exports = router
