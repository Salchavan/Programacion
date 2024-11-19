
class SubjectMathematics {
    constructor(professor, students) {
        this.professor = professor
        this.students = students
    }
    showInfo() {
        alert(`Professor: ${this.professor}--  Student: ${this.students}`);
    }
}
class SubjectPhysics {
    constructor(professor, students) {
        this.professor = professor
        this.students = students
    }
    showInfo() {
        alert(`Professor: ${this.professor} -- Student: ${this.students}`);
    }
}
class SubjectChemistry {
    constructor(professor, students) {
        this.professor = professor
        this.students = students;
    }
    showInfo() {
        alert(`Professor: ${this.professor} -- Student: ${this.students}`);
    }
}
chemistry = new SubjectChemistry("Saucedo", ["alan", "juan", "cofla", "josue"]);
mathematics = new SubjectMathematics("barie", ["juan", "alosno", "fernadez", "cofla"]);
physics = new SubjectPhysics("conte", ["juan", "pedro", "dominguez", "facundo"]);

chemistry.showInfo();
mathematics.showInfo();
physics.showInfo();