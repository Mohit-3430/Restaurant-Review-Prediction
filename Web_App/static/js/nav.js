const currentLocation = location.href
const navItem = document.querySelectorAll('.nav-link')
console.log(navItem[0].className)

for (let i = 0; i < 3; i++) {
    if (navItem[i] == currentLocation) {
        navItem[i].className += " active"
    }
}