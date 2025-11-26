
const loaded = []


function startVideo(el, src){
    if (!Hls.isSupported()) {
        return
    }

    if (loaded.includes(src)) {
        return
    }

    loaded.push(src)

    video = el.querySelector("video")

    const hls = new Hls()
    hls.loadSource(src)
    hls.attachMedia(video)
}


function playVideo(el){
    video = el.querySelector("video")
    video.classList.add("show")
    video.play()
}

function pauseVideo(el){
    video = el.querySelector("video")
    video.classList.remove("show")
    video.pause()
}
