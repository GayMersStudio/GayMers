
const loaded = []


function startVideo(el, src){
    if (!Hls.isSupported()) {
        return
    }

    if (loaded.includes(src)) {
        return
    }

    loaded.push(src)

    loader = el.querySelector(".loading")
    loader.classList.remove("hidden")

    video = el.querySelector("video")

    const hls = new Hls({
        maxBufferLength: 1,
        maxMaxBufferLength: 1
    })
    hls.loadSource(src)
    hls.attachMedia(video)
    video.addEventListener("loadeddata", () => {
        loader.classList.add("hidden")
    });
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
