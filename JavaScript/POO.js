// sintaxis
class Persona{
    constructor(nombre, edad){
        this.nombre = nombre;
        this.edad = edad;

    }
    saludar(){
        console.log(`Hola! soy ${this.nombre}`)
    }
}

// herencia
class Carpintero extends Persona{
    constructor(nombre, edad, experiancia){
        super(nombre, edad)
        this.experiancia = experiancia
    }
    saludar(){
        console.log(`Hola! soy ${this.nombre}, soy un carpintero`)
    }
    serruchar(){
        console.log(`Ese telefono parece carpintero, porque hace rin, porque hace rin`)
    }
}

const persona1 = new Perro("max", 17, "14 años");

persona1.saludar();

persona1.caminar = function(){
    console.log(`${this.name} camina felizmente`)
};

persona1.prototype.clavar = function(){
    console.log(`${this.name} clava un clavo`)
}