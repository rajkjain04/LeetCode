var isValid = function (s) {
  if (s === "") {
    return false;
  }

  const leftBrackets = new Set(["[", "{", "("]);
  const stack = [];
    
  for (let i = 0; i < s.length; i++) {
    const character = s[i];

    if (leftBrackets.has(character)) {
      stack.push(character);
    } else {
      if (stack.length === 0) {
        return false;
      }

      const lastElement = stack[stack.length - 1];
      if ((lastElement === "[" && character === "]") || (lastElement === "(" && character === ")") || (lastElement === "{" && character === "}")
      ) {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  return stack.length === 0;
};
