const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        let operationSuccess = true;
        if (operationSuccess) {
            resolve("Operation successful");
        } else {
            reject("Operation failed");
        }
    }, 2000);
});
promise.then((successMessage) => {
    console.log(successMessage);
});
promise.catch((errorMessage) => {
    console.log(errorMessage);
});