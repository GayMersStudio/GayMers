
function tabSwitch(tab, isOn){
    divider = tab.querySelector("span")

    if (isOn){
        divider.classList.remove("hidden")

        tab.classList.remove("text-base-content/60")
        tab.classList.add("mt-3")
        tab.classList.add("text-base-content")
    } else {
        divider.classList.add("hidden")

        tab.classList.add("text-base-content/60")
        tab.classList.remove("mt-3")
        tab.classList.remove("text-base-content")
    }
}

function activateTab(el, callback){
    document.querySelectorAll(".tab").forEach(tab => {tabSwitch(tab, false)})

    tabSwitch(el, true)
}
