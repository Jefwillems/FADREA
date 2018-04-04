window.onload = function () {


};

document.addEventListener("DOMContentLoaded", function () {
    // Handler when the DOM is fully loaded
    const links = document.getElementById("desktop-nav").innerHTML;
    console.log(links);
    document.getElementById("mobile-nav").innerHTML = links;
    const elem = document.querySelector('.sidenav');
    const instance = M.Sidenav.init(elem, {});
});