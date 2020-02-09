function flatten_array(arr = []) {
  // if arr is empty then return empty string from the function

  if (!arr || !arr.length) return 'Invalid Input'
  let modifyArray = []
  // arr.toString().split(',').map(number => parseInt(number))
  for (let index in arr) {
    let item = arr[index]
    if (Array.isArray(item)) {
      modifyArray = modifyArray.concat(flatten_array(item))
    } else {
      // this is the array contains
      modifyArray.push(item)
    }
  }

  return modifyArray
}

console.log(flatten_array([[1, 2, 3], 4, [5, [6, 7, [8, 9, 10]]]]))