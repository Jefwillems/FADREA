document.addEventListener("DOMContentLoaded", function () {
    let links = Array.prototype.slice.call(document.querySelectorAll(".nav-row-container a"));
    links = links.map(e => {
        let li = document.createElement('li');
        li.appendChild(e);
        return li;
    });
    let mob = document.getElementById("mobile-nav");
    links.forEach(e => {
        mob.appendChild(e);
    });
    const elem = document.querySelector('.sidenav');
    const instance = M.Sidenav.init(elem, {});
});