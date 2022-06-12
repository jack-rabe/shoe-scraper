const express = require('express')
const path = require('path')
const data = require('./data/adidas_shoes.json')

const app = express()
const port = 3000

app.set('view engine', 'ejs');
app.use(express.static(path.resolve(__dirname, 'node_modules/bootswatch/dist/cyborg')));
app.use(express.static(path.resolve(__dirname, 'images')));

app.get('/', (_req, res) => {
	res.render('pages/index', {'data': data});
})

app.get('/data', (_req, res) => {
	res.json(data);
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
})
