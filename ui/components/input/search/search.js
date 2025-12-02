
async function searchGames(el){
    try {
        const response = await fetch(BASE_API_URL + `search?query=${el.value}`, {
            method: "GET",
            credentials: "include"
        })

        const data = await response.json()

        console.log(data.tags)

    } catch (error) {
        
    } finally {

    }
}
