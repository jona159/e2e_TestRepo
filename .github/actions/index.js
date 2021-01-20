const { OpenEO } = require('@openeo/js-client');

OpenEO.connect("https://earthengine.openeo.org").then(function(con) {
  // Success
}).catch(function(error) {
  // Error
});

async function tryConnect(){
try {
  var con = await OpenEO.connect("https://earthengine.openeo.org");
  // Success
} catch (error) {
  // Error
}}

tryConnect();

var info = con.capabilities();
