//Use native json functions instead of eval
//to convert json to js objects
var client =  {"id":"53","desc":"Roberts"}; //js obj
var text = JSON.stringify(client); //convert obj to json
var myObject = JSON.parse(text); //convert json to js obj
console.log(myObject);
console.log(myObject.id);
console.log(myObject.desc);
