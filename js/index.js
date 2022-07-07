function setActiveLink() {
  const aboutLink = document.getElementById('about-link')
  const homeLink = document.getElementById('home-link')
  const current_path = window.location.href.split('/').pop() // get the final part of the url path

  if (current_path.includes('about')) aboutLink.classList.toggle('active')
  else homeLink.classList.toggle('active')
}

setActiveLink()
