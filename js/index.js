function sort_by_price(shoe_array) {
	shoe_array.sort( (a, b) => {
		a.price < b.price
	});
}

function filter_by_brand(shoe_array, brand) {
	shoe_array.filter( (el) => {
		el.brand == brand
	});
}
