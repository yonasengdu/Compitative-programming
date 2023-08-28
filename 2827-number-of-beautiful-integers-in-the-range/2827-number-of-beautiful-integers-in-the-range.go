func numberOfBeautifulIntegers(low int, high int, k int) int {

    beautiful := 0
  
    low = ((low - 1) / k + 1) * k
    for i := low; i <= high; i += k {
        if i%k == 0 {
            even, odd := 0, 0
            num := i
            
            for num >= 1 {
                div := (num % 10) % 2
                
                if div == 0 {
                    even++
                } else {
                    odd++
                }
                
                num /= 10
            }
            
            if even == odd && even != 0 {
                beautiful++
            }
            
            if i >= 100000000 {
                  return beautiful
                
            }
        }
    }
    
    return beautiful
}

    
