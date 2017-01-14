#!/usr/bin/env node
noble = require('noble');

var status = false;
var address = process.argv[2];

if (!address) {
    console.log('Usage "./reader.py <sensor mac address>"');
    process.exit();
}

function hexToInt(hex) {
    var num, maxVal;
    if (hex.length % 2 !== 0) {
        hex = "0" + hex;
    }
    num = parseInt(hex, 16);
    maxVal = Math.pow(2, hex.length / 2 * 8);
    if (num > maxVal / 2 - 1) {
        num = num - maxVal;
    }

    return num;
}

noble.on('stateChange', function(state) {
    status = (state === 'poweredOn');
});

noble.on('discover', function(peripheral) {
    if (peripheral.address == address) {
        var data = peripheral.advertisement.manufacturerData.toString('hex');
        console.log(Math.min(100,parseInt(data.substr(14, 2),16)));
        noble.stopScanning();
        process.exit();
    }
});

noble.on('scanStop', function() {
    noble.stopScanning();
});

setTimeout(function() {
    noble.stopScanning();
    noble.startScanning();
}, 1000);
