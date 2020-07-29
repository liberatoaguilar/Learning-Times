const {readFile} = require("fs");
const {readdirSync} = require("fs");
let regexp = new RegExp(process.argv[2]);
let files = [...process.argv].slice(3);

function checkSubDirs(dir) {
  for (let subfile of readdirSync(dir)) {
    readFile(dir+"/"+subfile, "utf8", (error, text) => {
      if (error) {
        if (error.code = "EISDIR") checkSubDirs(dir+"/"+subfile);
        else throw errow;
      }
      if (regexp.test(text)) console.log(dir+"/"+subfile);
    });
  }
}

for (let file of files) {
  readFile(file, "utf8", (error, text) => {
    if (error) {
      if (error.code == "EISDIR") {
        checkSubDirs(file);
      } else throw error;
    }
    if (regexp.test(text)) console.log(file);
  });
}
