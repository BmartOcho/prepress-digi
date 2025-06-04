var doc = app.activeDocument;
var ab = doc.artboards[0];
var rect = ab.artboardRect;

var widthPts = rect[2] - rect[0];
var heightPts = rect[1] - rect[3];

var widthIn = widthPts / 72;
var heightIn = heightPts / 72;

var commonTrims = {
    "8.5x11": [8.5, 11],
    "5x7": [5, 7],
    "4x6": [4, 6]
};

var matchedTrim = "Unknown";
for (var key in commonTrims) {
    var dims = commonTrims[key];
    if (Math.abs(widthIn - dims[0]) < 0.1 && Math.abs(heightIn - dims[1]) < 0.1) {
        matchedTrim = key;
        break;
    }
}

var fullPath = doc.fullName.fsName;
var newPath = fullPath.replace(/\.ai$/i, "_PrintReady.pdf");

var pdfOptions = new PDFSaveOptions();
doc.saveAs(new File(newPath), pdfOptions);

$.writeln("Width: " + widthIn.toFixed(2) + " in");
$.writeln("Height: " + heightIn.toFixed(2) + " in");
$.writeln("Trim Match: " + matchedTrim);
$.writeln("Saved As: " + newPath);

// Optional: close doc if you want full hands-free
// doc.close(SaveOptions.DONOTSAVECHANGES);
