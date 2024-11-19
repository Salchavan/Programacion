// delcaracion de variable
/*palabra reservada*/function /*nombre*/sum (/*Argumentos*/na, nb){
return na + nb; //codigo
}

// usar funciones como argumentos de otra => callback
function a (){}
function b (a){}
b(a)

// crear variables dentro de otras y retornarlas
function aa (){
    function a (){}
    return a();
}

// asignar funciones a variables => expresion de funcion 
const a = function (){}

// propiedades y metodos
function a (){}
const obj = {};
a.call(obj);

// anidar funciones => nester functions
function a (){
    function b (){
        function c (){}
    } c()
    b()
} a()

// funciones dentro de objetos
const rocket = {
    name: "R12",
    launcheMessage: function launcheMessage (){
        console.log("launching");
    }
}
rocket.launcheMessage()

// funciones puras = el output es igual al input
/*side effects:
    - modificar variable globales
    - modificar paramertos
    - solicitudes HTTP
    - imprimir mensajes en la pantalla o la consola
    - obtener la hora actual
    - manipulacion del DOM
*/

// funcion pura
function a (a, b){
    return a + b;
}

// funcion inpura
function a (a, b){
    console.log("asdd");
    return a + b;
}

// arrow function estas son mas faciles de escribir y normalmente mas cortas
const a = (a, b) => {
    return a + b;
}
//  lexical binding
const a = {
    name: "tio ben",
    message: function (message){
        console.log(`${this.name} says: ${message}`);
    },
    messageArroy:  (message) => {
        console.log(`${this.name} says: ${message}`);
    }
}

// contexto de ejecusion y scope chain

const global = 1
function a (){
    const local = 2;
}

// closure
function outerFunction(){
    let outerVariable = "A";
    function innterFunction (){
        console.log(outerVariable);
    }
    return innterFunction()
}
const closureExample = outerFunction()
closureExample()

function createCounter(){
    let count = 0;
    return function(){
        count++;
        console.log(count)
    }
}

const counterA = createCounter()
counterA()
counterA()

const counterB = createCounter()
counterB()

function outer(){
    let message = "Hello, "
    function inner(name){
        console.log(message + name)
    }
    return inner()
}
const closureA = outer()
const closureB = outer()

closureA("Pedro")
closureB("Juan")