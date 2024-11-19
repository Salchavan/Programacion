let quantity = prompt("¿How many students are there?");
let totalStudents = [];

for (i = 0; i < quantity; i++) {
	totalStudents[i] = [prompt("Name of the student " + (i+1)),0];
}

const takePresence = (name,p)=>{
	let presence = prompt(name);
	if (presence == "p" || presence == "P") {
	    totalStudents[p][1]++;
	}
}

for (i = 0; i < 30; i++) {
	for (student in totalStudents) {
	takePresence(totalStudents[student][0],student);
	}
}

for (student in totalStudents) {
	let result = `${totalStudents[student][0]}:<br>
    ________Presences: <b>${totalStudents[student][1]}</b> <br>
    ________Absences: <b>${30 - totalStudents[student][1]} </b>`;
	if (30 - totalStudents[student][1] > 18) {
	result+= "<b style='color:red'>FAILED FOR EXCESSIVE FOULS</b><br><br>";
	} else {
	result+= "<br><br>"
	}
	document.write(result)
}
