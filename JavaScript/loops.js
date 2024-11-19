let listt = [1, 2, 3, 4]

// for comun
for (i = 0; i < listt; i++){
    console.log(listt[i]);
}

// for of (se peude usar siempre que haya una lista iterable)
for (number of listt){
    console.log(number)
}

let pokemon = {
    life: 10,
    atk: 5,
    def: 7,
}

// for in (se usa para objetos inumerables, como un objeto)
for (property in pokemon){
    console.log(`${property} : ${pokemon[property]}`)
}

let count = 10;
// while
while(count !== 0){
    console.log(count);
    count--;
}

// do while (primero ejecuta el codigo y despues evalua la condicion)
do {
    console.log(count);
    count--;
} while (count === 0);
