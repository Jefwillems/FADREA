document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("mobile-nav").innerHTML = document.getElementById("desktop-nav").innerHTML;
    const elem = document.querySelector('.sidenav');
    const instance = M.Sidenav.init(elem, {});
});