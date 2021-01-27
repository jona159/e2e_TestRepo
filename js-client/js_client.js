// Set QUnit config autostart to false so that QUnit doesn't
// run on window load
QUnit.config.autostart = false;

// Initialize global variables 
var coll;
var proc;

// adjust path to backend here
//var url = 'https://earthengine.openeo.org'
var url = 'http://localhost:8080/api/v1'

/**
 * @desc This function connects to the backend and sets the number of collections and
 * processes to the global variables.
 */

function Data() {
	var connection = null;

			OpenEO.connect(url)
				.then(c => {
					connection = c;
					console.log(connection.capabilities());
					return connection.capabilities();

				})
				.then(capabilities => {
					console.log(capabilities.apiVersion());
					return connection.listCollections();
				})
				.then(collections => {
					coll = (collections.collections.length);
					console.log(coll);
					return connection.listProcesses();
				})
				.then(processes => {
					proc = (processes.processes.length);
					console.log(proc);
					return;
					
				})
				.catch(err => alert(err.message));;
}

/**
 * @desc This functions returns the number of collections
 * @returns {int} coll - the number of collections
 */
function checkColl(){
		return coll;
}

/**
 * @desc This functions returns the number of processes
 * @returns {int} proc - the number of processes
 */
function checkProc(){
	return proc;
}

/**
 * @desc This functions calls the Data from the backend and starts the
 * QUnit tests with a delay of 5 seconds.
 */
window.onload = function wait(){
	Data();
	setTimeout(() => {
		QUnit.start();
	}, 5000);
}


// QUnit Tests Collections
QUnit.test( "OpenEO JS Client - Collections", function (assert) {
	assert.notEqual((checkColl()), 0, 'number of collections should be greater that 0');
	assert.notEqual((checkColl()), 'hi', 'should be integer but string given');
	assert.notEqual((checkColl()), -5, 'number of collections can not be nagative');
})

// QUnit Tests Processes
QUnit.test( "OpenEO JS Client - Processes", function (assert) {
	assert.equal((checkProc()), 4, 'correct number of collections (4)');
	assert.notEqual((checkProc()), 'hi', 'should be integer but string given');
	assert.notEqual((checkColl()), -5, 'wrong number of collections given');
})
