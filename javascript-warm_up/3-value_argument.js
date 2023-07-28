#!/usr/bin/node
const argv = reqire('process').argv;

if (argv[2] === undefined) {
    console.log('No argument');
} else {
    console.log(argv[2]);
}