class Humano {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    saludar() {
        console.log(`Hello, I'm ${this.nombre}`);
    }
}
