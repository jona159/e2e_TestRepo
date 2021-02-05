// Import the JS client
const { OpenEO } = require('@openeo/js-client');

//const url = "https://earthengine.openeo.org"; // Insert the openEO server URL here
const url = "http://0.0.0.0:80/api/v1"
let connection = null;

// initialize global variables
var coll;
var proc;

console.log('URL: ' + url);
console.log('Client Version: ' + OpenEO.clientVersion());

/**
 * @desc This function connects to the backend and sets the number of collections and
 * processes to the global variables.
 */
function Data(){
OpenEO.connect(url)
	.then(c => {
		connection = c;
		return connection.capabilities();
	})
	.then(capabilities => {
		console.log('Server Version: ' + capabilities.apiVersion());
		return connection.listCollections();
	})
	.then(collections => {
		coll = (collections.collections.length);
		console.log('Number of supported collections: ' + collections.collections.length);
		return connection.listProcesses();
	})
	.then(processes => {
		proc = (processes.processes.length);
		console.log('Number of supported processes: ' + processes.processes.length);
	})
	.catch(err => console.error(err.message));
}

/**
 * @desc This functions calls the Data from the backend and checks
 * the correct number of collections and processes and throws an error if 
 * the number is not equal to the expected number.
 */
function wait(){
	Data();
	setTimeout(() => {
	if (coll < 0) {
	   throw new Error('Number of collections must be at least 1');
			   }
	else if (proc != 4){
		   throw new Error('Given number of processes does not match the expected number');
	   }
	}, 10000);
}
		   
wait();
