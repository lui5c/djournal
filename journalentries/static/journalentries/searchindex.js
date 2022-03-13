// get the search bar
let searchbar =  document.getElementById("searchbar")
let searchContainer = document.getElementById("search")
let results = document.getElementById("results")
let allContentNodes = document.querySelectorAll('entrywrapper')

searchbar.addEventListener("input", handleInput)

function clearResults(){
    while (results.firstChild){results.removeChild(results.firstChild)}
}

function displayResultsFor(input){
    allContentNodes.forEach((node) => {
    })
}

function handleInput(e){
    // if no terms, remove results
    if (e.target.value == ""){clearResults()}
    else {
        displayResultsFor(e.target.value())
    }
}

