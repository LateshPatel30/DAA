public class fibo {

    // Recursive method to calculate Fibonacci number
    static int fibRecursive(int n) {
        if (n <= 1)
            return n; // Base case
        return fibRecursive(n - 1) + fibRecursive(n - 2); // Recursive relation
    }

    // Iterative method to print Fibonacci series
    static void fibIterative(int n) {
        int a = 0, b = 1, c;

        System.out.print("Fibonacci Series (Iterative): ");
        System.out.print(a + " " + b + " ");

        for (int i = 2; i < n; i++) {
            c = a + b;
            System.out.print(c + " ");
            a = b;
            b = c;
        }
        System.out.println();
    }

    // Main method
    public static void main(String[] args) {
        int n = 10;

        // Iterative version
        fibIterative(n);

        // Recursive version
        System.out.print("Fibonacci Series (Recursive): ");
        for (int i = 0; i < n; i++) {
            System.out.print(fibRecursive(i) + " ");
        }
        System.out.println();
    }
}



