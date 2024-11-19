const usersDatabase=[
    {
        username:"andres",
        password:"123"
    },
    {
        username:"caro",
        password:"456"
    },
    {
        username:"mariana",
        password:"789"
    }
];
    
const usersTimeline=[
    {
        username:"estefany",
        timeline:"Me encata Javascript!"
    },
    {
        username:"caro",
        timeline:"Bebeloper es lo mejor!"
    },
    {
        username:"mariana",
        timeline:"A mi me gusta más el café que el té"
    },
    {
        username:"andres",
        timeline:"Yo hoy no quiero trabajar"
    }
];

let user = prompt("Ingrese su usuario");
let password = prompt("Ingrese su contraseña");

function isUserValid(user, password) {
    for (let i = 0; i < usersDatabase.length; i++) {
        if (user === usersDatabase[i].username && password === usersDatabase[i].password) {
            alert("Bienvenido de nuevo " + user + "!!!\n" + "timeline: ---" + usersTimeline[i].timeline + "---");
            break;
        }
    }
    alert("Usuario y/o contraseña incorrectos");
    return false;
}


isUserValid(user, password);
