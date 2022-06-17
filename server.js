const express = require('express')

const path = require('path')
const data = require('./data/merged_shoes.json')

const app = express()
const port = 3000

app.set('view engine', 'pug');
app.use(express.static(path.resolve(__dirname, 'node_modules/bootswatch/dist/cyborg')));
app.use(express.static(path.resolve(__dirname, 'images')));
app.use(express.static(path.resolve(__dirname, 'js')));

// parse request bodies
app.use(express.json());

app.get('/', (_req, res) => {
	res.render('pages/index', {
		'data': data,
	});
})

app.get('/data', (req, res) => {
	shoes = data['shoes'];
	brand = req.query.brand;

	shoes = shoes.filter( shoe => {
		return shoe.brand == brand; 
	});
	result = {
		'shoes': shoes,
		'brands': data.brands,
		'current_brand': brand,
		'count': shoes.length 
	}

	res.render('pages/index', {'data': result});
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
})
