const embed = (function () {
    const app = Object.create(null);
    app.init = function () {
        let body = document.querySelector('body');
        this.convertMedia(body.innerHTML, body);
    };

    app.convertMedia = function (html, body) {
        // const pattern1 = /(?:http?s?:\/\/)?(?:www\.)?(?:vimeo\.com)\/?(.+)/g;
        // const pattern2 = /(?:http?s?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)/g;
        // //const pattern3 = /([-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?(?:jpg|jpeg|gif|png))/gi;
        const ytPattern = /<p>embed:?([^<]*)<\/p>/g;

        if (ytPattern.test(html)) {
            const replacement = "<div class='yt-player' id='$1'></div>";
            html = html.replace(ytPattern, replacement);
            body.innerHTML = html;
            let allVideos = [].slice.call(document.querySelectorAll('.yt-player'));
            allVideos.forEach(el => {
                let id = el.id;
                console.log('replacing div with id:' + id);
                new YT.Player(id, {
                    height: '360',
                    width: '640',
                    videoId: id
                });
            });
        }
    };

    return app;
})();


// Load the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

function onYouTubeIframeAPIReady() {
    embed.init();
    // player = new YT.Player('ytplayer', {
    //     height: '360',
    //     width: '640',
    //     videoId: 'M7lc1UVf-VE'
    // });
}