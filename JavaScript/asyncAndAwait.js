const url = 'https://pokeapi.co/api/v2/pokemon/';
const urls = ['https://pokeapi.co/api/v2/pokemon/1', 'https://pokeapi.co/api/v2/pokemon/2', 'https://pokeapi.co/api/v2/pokemon/3'];

// function fetchData () {
//   fetch(url)
//     .then(response => response.json())
//     .then(data => console.log(data))
//     .catch(error => console.log(error));
// }


async function fetchData() {
    try {
        let response = await fetch(url);
        let data = await response.json();
        console.log(data);
    } catch (error) {
        console.log(error);
    }
}

async function fetchNewData() {
    try {
        for await (let url of urls) {
            let response = await fetch(url);
            let data = await response.json();
            console.log(data);
        }
    } catch (error) {
        console.log(error);
    }
}


fetchNewData();
fetchData();