// estructura de un objeto
const persona = {
    nombre: "raul", // key = value
    edad: "54",
    saludar(){ // metodo
        console.log("Hello world!")
    }
};

persona.sangre = "+A"; // agrego una key
persona.telefono = 234567876543;

// agrego un metodo
persona.caminar = () => { 
    console.log("*Caminando*")
};

persona.saludar(); // llamo al metodo
console.log(persona.edad) // imprimo la propiedad

delete persona.telefono;

// POO
// funcion constructora
function Auto(modelo, usado, motor){
    this.modeto = nombre;
    this.usado = usado;
    this.motor = motor;
};

// instancia
const auto1 = new Auto( "BMW T2", true, "V16 9,5L");

// agrega una propiedad global (no se agrega directamente a la funcion constructora, si no que lo agreaga a "prototipo")
Auto.prototype.suspension = "Buldozer g12";

// agrega a una propiedad en particular
Auto.autoConduccion = true;

// agrega un metodo
Auto.prototype.funcionGLE = function(){
    console.log("*Tira facha*")
};