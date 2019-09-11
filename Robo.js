//var input = require('fs').readFileSync('/dev/stdin', 'utf8');
//var lines = input.split('\n'); 
//replace with the correct archive path

//Using placeholders variables

lines = `FFTT`;
//
lines.split(``);
total = 0
for (i= 0; i<lines.length; i++){
    if (lines[i] == `F`){total += 1}
    if (lines[i] == `T`){total -= 1}
}
console.log(total);