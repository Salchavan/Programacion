class App {
    constructor(name, version, downloads, score, weight) {
        this.name = name;
        this.version = version;
        this.downloads = downloads;
        this.score = score;
        this.weight = weight;
        this.open = false;
        this.installed = false;
    }
    installApp(){
        if (this.installed == false){
            alert("The app is installing...");
            this.installed = true;
        } else {
            alert("The app is already installed...");
        }
    }
    openApp(){
        if (this.open == false && this.installed == true){
            alert("The app is opening...");
            this.open = true;
        } else {
            alert("The app is not installed or is already open...");
        }
    }
    closeApp(){
        if (this.open == true && this.installed == true){
            alert("The app is closing...");
            this.open = false;
        } else {
            alert("The app is not installed or is already close...");
        }
    }
    uninstallApp(){
        if (this.installed == true){
            alert("The app is uninstalling...");
            this.installed = false;
        } else {
            alert("The app is not installed...");
        }     
    }
}
app1 = new App("Instagram", "1.15.133", "5465433646", "4.7", "80Mb");
app2 = new App("Youtube", "7.5.3", "523224654646", "4.9", "200Mb");
app3 = new App("Twitter", "3.1.23", "524654646", "4.2", "120Mb");

app1.installApp();
app1.openApp();
app1.closeApp();
app1.uninstallApp();

