const { OpenEO } = require('@openeo/js-client');

var con = await OpenEO.connect("https://earthengine.openeo.org");

var info = con.capabilities();
