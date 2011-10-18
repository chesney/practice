//Either use native json functions or 3rd party json
//library / framework. Never use eval to convert json
//text to js objects, it is a huge security risk.
//eval parses any valid javascript code and executes it.
//This opens the door for malicious content to be injected
//into js objects

//Array example
var clients =  {"clients":[
  {"id":"53","desc":"Roberts"},
  {"id":"54","desc":"Jones"},                                                  {"id":"55","desc":"Malan"}
  ]}; //js obj with clients array

var text = JSON.stringify(clients); //convert obj to json

var myObject = JSON.parse(text); //convert json to js obj

console.log(myObject,'myObject with clients[]');

console.log(myObject.clients[0].id); //array start @ 0

console.log(myObject.clients[0].desc);
