// Working on IE11, FireFox, Chrome & Safari

history.pushState(null, document.title, location.href);
window.addEventListener('popstate', function (event) {
    history.pushState(null, document.title, location.href);
});
