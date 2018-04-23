const embed = (function () {
    const app = Object.create(null);
    app.init = function () {
        let body = document.querySelector('body');

        body.innerHTML = this.convertMedia(body.innerHTML);
    };

    app.convertMedia = function (html) {
        const pattern1 = /(?:http?s?:\/\/)?(?:www\.)?(?:vimeo\.com)\/?(.+)/g;
        const pattern2 = /(?:http?s?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)/g;
        //const pattern3 = /([-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?(?:jpg|jpeg|gif|png))/gi;

        if (pattern1.test(html)) {
            const replacement = '<iframe width="420" height="345" src="//player.vimeo.com/video/$1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>';
            html = html.replace(pattern1, replacement);
        }


        if (pattern2.test(html)) {
            let replacement = '<iframe id="ytplayer" type="text/html" width="640" height="360"\n' +
                '  src="https://www.youtube.com/embed/$1?autoplay=0"\n' +
                '  frameborder="0"></iframe>';
            replacement = '<div class="article video">' + replacement + '</div>';
            html = html.replace(pattern2, replacement);
        }


        // if (pattern3.test(html)) {
        //     const replacement = '<a href="$1" target="_blank"><img class="sml" src="$1" /></a><br />';
        //     html = html.replace(pattern3, replacement);
        // }
        return html;
    };

    return app;
})();


embed.init();