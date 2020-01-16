'use strict';
const http = require('http');
var os = require('os');
var ifaces = os.networkInterfaces();
var ip="";
var mac="";
Object.keys(ifaces).forEach(function (ifname) {
	var alias = 0;

	ifaces[ifname].forEach(function (iface) {
		if ('IPv4' !== iface.family || iface.internal !== false) {
			// skip over internal (i.e. 127.0.0.1) and non-ipv4 addresses
			return;
		}

		if (alias >= 1) {
			// this single interface has multiple ipv4 addresses
			console.log(ifname + ':' + alias, iface.address);
		} else {
			// this interface has only one ipv4 adress
			if(ip==""){
				ip=iface.address;
				mac=iface.mac;
			}
		}
	});
});
mac=mac.toUpperCase();
mac=mac.split(":").join("-")
ip=ip.split(".").join("-")
console.log('/actualizar/'+mac+"/"+ip);
http.get({
	hostname: 'cidsip.us.to',
	port: 80,
	path: '/actualizar/'+mac+"/"+ip,
	method: 'POST',
	body: JSON.stringify({
		mac:"123",
		ip:"123",
	}),
	agent: false  // Create a new agent just for this one request
}, (res) => {
  console.log(res.statusCode);
  res.on("data", function(chunk) {
    console.log("BODY: " + chunk);
  });
});
