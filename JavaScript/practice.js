let n = 12 * 10 ** 100;
let l = [n];
let c = 0
console.log(`Operacion Nº 0: ${n}`);

while(n !== 1){
    c++;
    if(n % 2 === 1){
        n = (n * 3) + 1;
    } else if(n % 2 === 0){
        n = n / 2;
    } else{
        break;
    }
    console.log(`Operacion Nº ${c}: ${n}`);
    l.push(n);
}
console.log(l);
console.log(`El proceso duro ${c} aoperaciones`)
