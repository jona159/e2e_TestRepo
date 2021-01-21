// Import the JS client
const { OpenEO } = require('@openeo/js-client');
const core = require('@actions/core')

const url = "https://earthengine.openeo.org"; // Insert the openEO server URL here
let connection = null;

console.log('URL: ' + url);
console.log('Client Version: ' + OpenEO.clientVersion());

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
		console.log('Number of supported collections: ' + collections.collections.length);
		return connection.listProcesses();
	})
	.then(processes => {
		if (processes.processes.length = 1){
			core.setFailed('Nicht die korrekte Anzahl der Prozesse', 1)}
		console.log('Number of supported processes: ' + processes.processes.length);
	})
	.catch(err => console.error(err.message));
