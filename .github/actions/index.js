const { OpenEO } = require('@openeo/js-client');

OpenEO.connect("https://earthengine.openeo.org").then(function(con) {
  // Success
}).catch(function(error) {
  // Error
});

try {
  var con = await OpenEO.connect("https://earthengine.openeo.org");
  // Success
} catch (error) {
  // Error
}



var info = con.capabilities();
