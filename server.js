const express = require('express')
const path = require('path')
const data = require('./data/merged_shoes.json')

const app = express()
const port = 3000

app.set('view engine', 'pug');
app.use(express.static(path.resolve(__dirname, 'node_modules/bootswatch/dist/cyborg')));
app.use(express.static(path.resolve(__dirname, 'images')));
app.use(express.static(path.resolve(__dirname, 'js')));

app.get('/', (_req, res) => {
	res.render('pages/index', {'data': data});
})

app.get('/data', (_req, res) => {
	shoes = data['shoes'];
	shoes = shoes.filter( shoe => {
		return shoe.brand == 'nike'
	});
	result = {
		'shoes': shoes,
		'brands': ['nike'],
		'count': shoes.length 
	}

	res.render('pages/index', {'data': result});
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
})
