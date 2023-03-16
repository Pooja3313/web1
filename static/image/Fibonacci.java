class Fibonacci{
    void printFibonacci() {
       int fibArray[] = new int[10];
       int a = 0;
       int b = 1;
       fibArray[0] = a;
       fibArray[1] = b;
       int c;
       for(int i=2;i<10;i++) {
           c = a+b;
           fibArray[i] = c;
           a = b;
           b = c;
       }
       for(int i=0;i<10;i++) {
        if(Integer.parseInt(Thread.currentThread().getName())%2==0 && (i%2==0))
        {
            [1:34 PM, 11/12/2022] Sorathiya Pooja D:  System.out.println("Thread " +Thread.currentThread().getName()+" "+fibArray[i]);
            try{
                wait();
            }catch(Exception e) {}
        }
        else if(Integer.parseInt(Thread.currentThread().getName())%2!=0 && (i%2!=0))
        {
            System.out.println("Thread " +Thread.currentThread().getName()+" "+fibArray[i]);
        }
     }
   }
}

public class FibonacciUsingThread {

    public static void main(String[] args) throws Exception {
        Fibonacci f = new Fibonacci();
        Thread t1 = new Thread(()->
        {
            f.printFibonacci();
        });
        Thread t2 = new Thread(()->
        {
            f.printFibonacci();
        });
        t1.setName("0");
        t2.setName("1");
        t1.start();
        t1.join();
        t2.start();
    }
}
