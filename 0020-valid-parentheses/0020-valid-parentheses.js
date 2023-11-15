var isValid = function (s) {
  if (s === "") {
    return false;
  }

  const set = new Set(["[", "{", "("]);
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const currentElement = s[i];

    if (set.has(currentElement)) {
      stack.push(currentElement);
    } else {
      if (stack.length === 0) {
        return false;
      }

      const lastElement = stack[stack.length - 1];

      if (
        (lastElement === "[" && currentElement === "]") ||
        (lastElement === "(" && currentElement === ")") ||
        (lastElement === "{" && currentElement === "}")
      ) {
        stack.pop();
      } else {
        return false;
      }
    }
  }

  return stack.length === 0;
};
