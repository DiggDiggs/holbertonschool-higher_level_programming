#!/usr/bin/node

// its the 'add' part
function add(a,b) {
    return a + b;
}

const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);

const sum = add(firstInteger, secondInteger);
console.log('The addition is', sum);    