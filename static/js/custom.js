function navResponsive() {
  const x = document.querySelector(".navbar");
  if (x.className === "navbar") x.className += " responsive";
  else x.className = "navbar";
}
