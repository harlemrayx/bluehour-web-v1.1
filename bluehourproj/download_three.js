const fs = require('fs');
const https = require('https');

// Ensure directory exists
if (!fs.existsSync('js')) {
    fs.mkdirSync('js');
}

const file = fs.createWriteStream("js/three.min.js");
// Using unpkg which has a stable URL structure
const url = "https://unpkg.com/three@0.152.0/build/three.min.js";

console.log(`Downloading ${url}...`);

const request = https.get(url, function (response) {
    if (response.statusCode === 302 || response.statusCode === 301) {
        // Handle redirect
        const newUrl = response.headers.location;
        console.log(`Redirecting to ${newUrl}...`);
        https.get(newUrl, function (res) {
            res.pipe(file);
            file.on('finish', function () {
                file.close(() => console.log("Download completed from redirect."));
            });
        });
    } else if (response.statusCode !== 200) {
        console.error(`Failed to download: ${response.statusCode}`);
        process.exit(1);
    } else {
        response.pipe(file);
        file.on('finish', function () {
            file.close(() => {
                console.log("Download completed.");
            });
        });
    }
}).on('error', function (err) {
    console.error(`Error downloading file: ${err.message}`);
    process.exit(1);
});
