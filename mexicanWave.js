function wave(str){
    let results = [];
    let count = 0;
    let len = str.split('').length;
    while(count <= (len-1)){
    let strRR = str.split('').map((x,index)=>{ 
    return index==count ? x.toUpperCase() : x
    })
    count++
    newWrd = strRR.join('')
      if(/[A-Z]/.test(newWrd)){
      results.push(newWrd)
     }
    }
    return results;
    }

console.log(wave('hello'))
console.log(wave('codewars'))
console.log(wave('good morning'))
console.log(wave('map'))