const crypto = require('crypto');

const computeHash = (input) => {
    const hash = crypto.createHash('md5');
    hash.update(input);
    const md5sum = hash.digest('hex');
    return md5sum.substring(0,5)
}

input = "ckczppom"
counter = 1179460
while (computeHash(`${input}${counter}`) !== "000000") {
    counter++
}
console.log(counter)
