class Phone {
    constructor(color, weight, screenResolution, cameraResolution,ramMemory) {
        this.color = color;
        this.weight = weight;
        this.screenResolution = screenResolution;
        this.cameraResolution = cameraResolution;
        this.ramMemory = ramMemory;
        this.on = false;
    }
    turnOn_turnOff(){
        if (this.on == false){
            alert("The phone is turning on...");
            this.on = true;
        } else {
            alert("The phone is turning off...");
            this.on = false;
        }
    }
    restart(){
        if (this.on == true){
            alert("The phone is restarting...");
        } else {
            alert("The phone is turn off...");
        }
    }
    takePicture(){
        if (this.on == true){
            alert("The phone is taking a picture...");
        } else {
            alert("The phone is turn off...");
        }       
    }
    recordVideo(){
        if (this.on == true){
            alert("The phone is recording a video...");
        } else {
            alert("The phone is turn off...");
        }
    }
}

class UltraPhone extends Phone{
    constructor(color, weight, screenResolution, cameraResolution, ramMemory, extraCamera){
        super (color, weight, screenResolution, cameraResolution,ramMemory);
        this.extraCamera = extraCamera
    }
    recordSlowVideo(){
        alert("The phone is recording a slow video...");
    }
    facialRecognition(){
        alert("The phone is making a facial recognition...");
    }

}

phone1 = new Phone("red", "500g", "1080px", "48mpx", "2Gb");
phone2 = new Phone("black", "400g", "1260px", "55mpx", "3Gb");
phone3 = new Phone("blue", "700g", "720px", "20mpx", "1Gb");
ultraPhone1 = new UltraPhone("dark blue", "350g", "1560px", "80mpx", "4Gb", "55Mpx")
ultraPhone2 = new UltraPhone("dark red", "375g", "2116px", "90mpx", "6Gb", "60Mpx")

phone1.turnOn_turnOff();
phone1.takePicture();
phone1.recordVideo();
phone1.restart();
ultraPhone1.recordSlowVideo();
ultraPhone2.facialRecognition();