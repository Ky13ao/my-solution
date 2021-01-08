function round(n, digits) {
  return Math.round(n / (10 ** digits)) * 10 ** digits
}
function minDiff(n, a, b) {
  return (Math.abs(n - a) < Math.abs(n - b)) ? a : b
}
function findNumber(n) {
  if (n < 10) {
    return n;
  }
  let nums = n.toString().split('');
  for (let i = 1; i < nums.length; i++) {
    if (nums[i - 1] == nums[i]) continue;
    if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1]) {
      const d = nums.length - i;
      return minDiff(n, round(n + 0.5, d - 1), round(n + 0.5, d - 2));
    }
    if (nums[i - 1] > nums[i] && nums[i] < nums[i + 1]) {
      const d = nums.length - i;
      return minDiff(n, round(n, d), round(n, d - 1));
    }
  }
  return n
}