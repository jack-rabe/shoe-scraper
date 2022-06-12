const express = require('express')
const path = require('path')
const data = require('./data/adidas_shoes.json')

const app = express()
const port = 3000

// app.use(express.static(path.resolve(__dirname, 'public')));
app.use(express.static(path.resolve(__dirname, 'node_modules/bootswatch/dist/morph')));

app.get('/', (_req, res) => {
	res.sendFile(path.join(__dirname, '/index.html'));
})

app.get('/data', (_req, res) => {
	res.json(data)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
