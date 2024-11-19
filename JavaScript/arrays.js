// array() o new array()
const a = Array(1, 5, 3);
const a = new Array(4, 58, 4);
const a = Array(15); // esto crea 15 posiciones vacias

// literal syntaxis
const a = [1, 5, 6];
const a = [];
const a = [
    1,
    false,
    "potato",
    {
        tu: "mama",
        tu: "hermana"
    }
    ["hola", "soy", "una", "lista", "dentro", "de", "otra", "lista"]
];
const b = a.length;

// mutabilidad
a.push("tangamandapio");

// inmutabilidad
const c = a.concat(["asssda", 123123]);

// chequear si es un array
const asdc = Array.isArray(a); // devuelve True o False

// exercise 
const a = [1, 2, 3, 4];
for(let i = 0; i < a.length; i++){
    sum += a[i];
    console.log(sum)
};

// push (modifica el array)
const b = a.push("tumamamemima");

// pop (modifica el array)
const b = a.pop();

// map (crea otro array)
const b = a.map(num => num * num);

// forEach (modifica el array, devuelve undefined)
const b = a.forEach(num => console.log(num));

// filter
const b = a.filter(number => number % 2 === 0);

// reduce (reduce un array a un solo valor)
let acum = 0
const b = a.reduce((acum, curr => acum + curr, 0))

// cuenta el numero de palabras repetidas
const b = a.reduce((acum, curr) => {
    if (acum[curr]){
        acum[curr]++;
    }else{
        acum[curr] + 1;   
    }
});

// find
const b = a.find(num => num > 2);

// findIndex
const b = a.findIndex(num => num > 2);

// slice (inmutable)
const b = a.slice(2); // desde

const b = a.slice(2, 4); // desde hasta

const b = a.slice(2, 6); // desde hasta el ultimo

const b = a.slice(-1); // desde

const b = a.slice(2, -1); // desde hasta el ultimo

// spread operator ...
const b = [...a]; // copia

const b = [...c, ...a] // combina

const b = [...a, 5, 3, 4] // agrega elemenotos

// pasar elementos a funciones
function sum(a, b, c){
    return a + c + b
}
const result = sum(...a)