# a basic solution with if
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:  
        list = []
        
        for i in range(1, n+1):
            if i%15==0:
                list.append("FizzBuzz")
            elif i%5==0:
                list.append("Buzz")
            elif i%3==0:
                list.append("Fizz")
            else:
                list.append(str(i))
            
        return list

# a solution with list comprehension
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [str(i) * (i % 3 != 0 and i % 5 != 0) + "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) for i in range(1, n + 1)]
      
# a solution with customized def
class Solution:
    
    def fillList(self, n):
        if n%15==0:
            return "FizzBuzz"
        elif n%5==0:
            return "Buzz"
        elif n%3==0:
            return "Fizz"
        else:
            return str(n)
    
    def fizzBuzz(self, n: int) -> List[str]:
        list = []
        for i in range(1, n+1):
            list.append(self.fillList(i))
        return list
        

# In comparison with Java
class Solution {
    public String fillList(int n){
        if(n%15==0) return "FizzBuzz";
        else if(n%3==0) return "Fizz";
        else if(n%5==0) return "Buzz";
        else return Integer.toString(n);
    }
    
    public List<String> fizzBuzz(int n) {
        List<String> res = new ArrayList<String>();
        for(int i=1; i<=n; i++){
            res.add(fillList(i));
        }
        return res;
    }
}
