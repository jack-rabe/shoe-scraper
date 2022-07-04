const express = require('express')

const path = require('path')
const data = require('./data/merged_shoes.json')

const app = express()
const port = 3000

app.set('view engine', 'pug');
app.use(express.static(path.resolve(__dirname, 'node_modules/bootswatch/dist/darkly')));
app.use(express.static(path.resolve(__dirname, 'images')));
app.use(express.static(path.resolve(__dirname, 'js')));

// parse request bodies
app.use(express.json());

app.get('/', (_req, res) => {
	data.shoes.sort( (a, b) => {
		return a.price - b.price;
	});
	res.render('pages/index', {
		'data': data,
	});
})

app.get('/data', (req, res) => {
	let shoes = data['shoes'];
	let selectedBrands = req.query.brand;
  // ensure selectedBrands is an array
  if (typeof selectedBrands == 'string')
    selectedBrands = [selectedBrands]
  // split the selected brands w/ a space + comma
  prettyBrandsStr = selectedBrands.join(', ')

	shoes = shoes.filter( shoe => {
		return selectedBrands.includes(shoe.brand); 
	});
	result = {
		'shoes': shoes,
		'brands': data.brands,
		'current_brand': prettyBrandsStr,
		'count': shoes.length 
	}
	res.render('pages/index', {'data': result});
})

app.get('/about', (_req, res) => {
	res.render('pages/about');
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
})
