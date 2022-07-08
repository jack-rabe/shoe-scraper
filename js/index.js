// allows user to navigate from one page of shoes to the next or previous
function enablePageNavigation() {
  const nextPage = document.getElementById('page-forward')
  const previousPage = document.getElementById('page-back')
  // all links to a specific shoe page (e.g. page 1 or page 10)
  const specificLinks = document.querySelectorAll('.specific-link')

  nextPage.onclick = () => {
    const startIdx = getCurrentStart() + 100
    window.location.href = `/some?start=${startIdx}`
  }
  previousPage.onclick = () => {
    const startIdx = getCurrentStart() - 100
    window.location.href = `/some?start=${startIdx}`
  }

  let specificStartIdx = 0
  for (const link of specificLinks) {
    link.href = `/some?start=${specificStartIdx}`
    specificStartIdx += 100
  }
}

// get the start index of the current page of shoes from the url
function getCurrentStart() {
  const url = window.location.href
  const target = 'start='
  const start_idx = url.indexOf(target)
  let start_value = url.substring(start_idx + target.length)

  return parseInt(start_value)
}

// display which page the user is currently on in the navbar
function setActiveLink() {
  const aboutLink = document.getElementById('about-link')
  const homeLink = document.getElementById('home-link')
  const current_path = window.location.href.split('/').pop() // get the final part of the url path

  if (current_path.includes('about')) aboutLink.classList.toggle('active')
  else homeLink.classList.toggle('active')
}

setActiveLink()
enablePageNavigation()
