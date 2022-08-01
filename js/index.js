// allows user to navigate from one page of shoes to the next or previous
function enablePageNavigation() {
  const nextPage = document.getElementById('page-forward')
  const previousPage = document.getElementById('page-back')
  // all links to a specific shoe page (e.g. page 1 or page 10)
  const specificLinks = document.querySelectorAll('.specific-link')
  const shoeNumberTag = document.getElementById('shoe_number')
  const numberShoes = parseInt(shoeNumberTag.textContent.match('\\d+')[0])

  if (getCurrentStart() + 100 > numberShoes)
    nextPage.parentNode.classList.add('disabled')
  if (getCurrentStart() - 100 < 0)
    previousPage.parentNode.classList.add('disabled')

  nextPage.onclick = () => {
    const startIdx = getCurrentStart() + 100
    // disable link if on the first page
    const queryString = new URLSearchParams(window.location.search)
    queryString.set('start', startIdx)
    window.location.search = queryString.toString()
  }
  previousPage.onclick = () => {
    const startIdx = getCurrentStart() - 100
    const queryString = new URLSearchParams(window.location.search)
    queryString.set('start', startIdx)
    window.location.search = queryString.toString()
  }

  let specificStartIdx = 0
  const queryString = new URLSearchParams(window.location.search)
  const startIdx = parseInt(queryString.get('start'))
  for (const link of specificLinks) {
    queryString.set('start', specificStartIdx)
    link.href = `?${queryString.toString()}`
    // show which page is currently selected
    if (startIdx == specificStartIdx) link.parentNode.classList.add('active')
    specificStartIdx += 100
  }
}

// get the start index of the current page of shoes from the url
function getCurrentStart() {
  const queryString = new URLSearchParams(window.location.search)
  let startIdx = parseInt(queryString.get('start'))
  if (isNaN(startIdx)) startIdx = 0
  return startIdx
}

// display which page the user is currently on in the navbar
function setActiveLink() {
  const aboutLink = document.getElementById('about-link')
  const homeLink = document.getElementById('home-link')
  const current_path = window.location.href.split('/').pop() // get the final part of the url path

  if (current_path.includes('about')) aboutLink.classList.toggle('active')
  else homeLink.classList.toggle('active')
}

// add invisible cards to keep cards in the final row at a normal size
function normalizeFinalRow() {
  const x = document.querySelectorAll('.card-group')
  const lastGroup = x[x.length - 1]
  let num_cards = lastGroup.querySelectorAll('.card').length
  while (num_cards < 4) {
    const new_node = document.createElement('div')
    new_node.classList.add('card')
    new_node.classList.add('m-1')
    new_node.style.backgroundColor = 'var(--bs-body-bg)'
    new_node.style.border = 'none'
    lastGroup.appendChild(new_node)
    num_cards++
  }
}

setActiveLink()
enablePageNavigation()
normalizeFinalRow()
