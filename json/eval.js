//An eval example of converting json text to javascript object
//this is not a recommended practice! use native json or
//3rd party lib.

var jsonString = '{"name":"chesney","dept" : "it"}';

var person = eval( '(' + jsonString + ')' );
//best practice use native json -
//var person = JSON.parse(jsonString);

console.log(person);
console.log(person.name);
