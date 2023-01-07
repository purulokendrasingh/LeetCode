class Solution {
	 public int distinctPrimeFactors(int[] nums) {
        Set<Integer> primes = new HashSet<>();
        for(int i : nums){
            primes.addAll(primeFactors(i));
        }
        
        return primes.size();
    }
    
    public static Set<Integer> primeFactors(int n){
        Set<Integer> primes = new HashSet<>();
    
        if (n == 2) {
          primes.add(2);
          return primes;
        }
        HashMap<Integer, Boolean> v = new HashMap<>();
        for (int i = 2; i * i <= n; i++) {
          while (n % i == 0) {
            if (!v.containsKey(i)) {
              primes.add(i);
              v.put(i, true);
            }
            n /= i;
          }
        }
        if (n > 2) {
          primes.add(n);
        }
        return primes;
    }
}