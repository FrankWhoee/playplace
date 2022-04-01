import java.io.*;

public class DeterministicSelect
{

    //
    // Random number generator.
    //
    private java.util.Random rng;

    //
    // Counter class - used to hold comparison numbers.
    //
    private static class Counter
    {
	private int count;

	public Counter()
	{
	    count = 0;
	}

	public void increment()
	{
	    count++;
	}

	public int valueOf()
	{
	    return count;
	}
    }

    // 
    // generateVector - this method fills two arrays with random numbers
    //
    private void generateVectors(int[] array1, int[] array2) 
    {
	int size = array1.length;
        for(int i = 0; i < size; i++) {
	    array1[i] = array2[i] = rng.nextInt(100 * size);
        }
    }

    //
    // insertionSort -  use the insertionSort algorithm that sorts the portion
    // vector[first ... last] of vector and updates the number of comparisons made.
    //
    private void insertionSort(int[] vector, int first, int last, Counter comparisons)
    {
        for (int i = first + 1; i <= last; i++)
        {
            int index = i-1;
	    int elem = vector[i];

	    /*
	    ** Move element "elem" into position within the part of v we care about.
	    */
            while (index >= first && elem < vector[index])
	    {
	        vector[index + 1] = vector[index];
	        comparisons.increment();
	        index--;
	    }
	    vector[index+1] = elem;

	    /*
	    ** Adjust the number of comparisons.
	    */
	    if (index >= first)
	    {
	        comparisons.increment();
	    }
        }
    }

    //
    // A simple swap method.
    //
    private void swap(int[] A, int x, int y)
    {
        int tmp = A[x];
        A[x] = A[y];
        A[y] = tmp;
    }

    //
    // Now  the partition algorithm  of  quicksort, modified  to (1) count the
    // number of comparisons it  is making and  (2) take as an extra parameter
    // the position of the pivot to be used.
    //
    // This algorithm computes the Lesser and Greater vectors from our pseudo-
    // code as follows: it moves the elements in vector[first ... last] so
    // Lesser = vector[first ... mid-1], Greater = vector[mid+1 ... last] and
    // the pivot is A[mid]. The method returns the position "mid".
    //
    private int partition(int[] vector, int first, int last, int pivotPosition, Counter comparisons)
    {
        swap(vector, pivotPosition, last);
        int pivot = vector[last];
        int back = first - 1;

        for (int front = first; front < last; front++)
        {
	    comparisons.increment();
	    if (vector[front] <= pivot)
	    {
	        back++;
	        swap(vector, front, back); 
	    }
        }

        swap(vector, back+1, last);
        return back+1;
    }

    //
    // print - method to print an array (useful for debugging)
    //
    private void print(int[] vector)
    {
        for (int counter = 0; counter < vector.length; counter++) {
	    System.out.print(vector[counter] + " ");
        }
        System.out.println();
    }

    //
    // Randomized method to  find the kth  smallest element of  a vector. It
    // returns the position in the vector where the element was found.
    //
    private int randomizedQuickSelect(int[] vector, int first, int last, int k, Counter comparisons)
    {
        int n = last - first + 1;
        int p = first + (int)(rng.nextDouble() * n);

        int mid = partition(vector, first, last, p, comparisons);
        comparisons.increment();
        if(mid == k - 1){
            return mid;
        }else{
            comparisons.increment();
            if(mid > k - 1){
                return randomizedQuickSelect(vector, first, mid - 1, k, comparisons);            
            }else{
                return randomizedQuickSelect(vector, mid + 1, last, k, comparisons);            
            }
        }
    }
    
    //
    // Now the deterministic selection algorithm.
    //
    private int select(int[] vector, int first, int last, int k, Counter comparisons)
    {
        

        int n = last - first + 1;
        comparisons.increment();
        if(n >= 5){
            for(int i = first; i < n - 5; i += 5){
                insertionSort(vector, i, i + 4,comparisons);
                swap(vector, i+2, first + (int)((i - first)/5));
            }
            int m = (last - first)/10 + first + 1;
            int p = select(vector, first, first + (int)((last-first)/5), m, comparisons);
            int mid = partition(vector, first, last, p, comparisons);

            comparisons.increment();
            if(mid == k - 1){
                return mid;
            }else{
                comparisons.increment();
                if(mid > k - 1){
                    return select(vector, first, mid - 1, k, comparisons);            
                }else{
                    return select(vector, mid + 1, last, k, comparisons);            
                }
            }
            
        }else{
            insertionSort(vector, first, last, comparisons);
            return k - 1;
        }
        
    }
    
    //
    // Method runtests is really our main.
    //
    public void runtests(int size, int attempts) 
    {
        rng = new java.util.Random();
        int[] input1 = new int[size];
  	    int[] input2 = new int[size];
        int worst1 = 0;
        double average1 = 0;
        int worst2 = 0;
        double average2 = 0;
        for(int i = 0; i < attempts; i++){
            Counter c1 = new Counter();
            Counter c2 = new Counter();
            generateVectors(input1, input2);
	        int p1 = input1[randomizedQuickSelect(input1, 0, size - 1, (int)(size/2.0) + 1, c1)];
	        int p2 = input2[select(input2, 0, size - 1, (int)(size/2.0) + 1, c2)];
	        
	        // Sort input1 to find the actual median.
	        insertionSort(input1, 0, size - 1, new Counter());
	        int p3 = input1[(int)((size)/2)];
            // Stop program if output is incorrect.
            if(p1 != p3){
                System.out.println(p1);
	            System.out.println(p2);
	            System.out.println(p3);
                System.out.println("Incorrect output. RANDOM");
                return;
            }
            if(p2 != p3){
                System.out.println(p1);
	            System.out.println(p2);
	            System.out.println(p3);
                System.out.println("Incorrect output. SELECT");
                return;
            }
	        
            
	        if(c1.valueOf() > worst1){
	            worst1 = c1.valueOf();
	        }
	        if(c2.valueOf() > worst2){
	            worst2 = c2.valueOf();
	        }
	        average1 += c1.valueOf();
	        average2 += c2.valueOf();
        }
        average1 /= attempts;
        average2 /= attempts;
        // Printed to match LaTeX table format.
        System.out.println(size + " & " + worst1 + " & " + worst2 + " & " + average1 + " & " + average2 + " & " + Double.toString((average2/average1)).substring(0,3) + "\\\\");
        
        // Uncomment for desmos graphing
        //System.out.println("(" + size + "," + average1 + ")");
        //System.out.println("(" + size + "," + worst1 + ")");
        //System.out.println("(" + size + "," + average2 + ")");
        //System.out.println("(" + size + "," + worst2 + ")");
        
        // Human readable format printing
        //System.out.println("SIZE: " + size);
        //System.out.println("WorstRandom: " + worst1);
        //System.out.println("AvgRandom: " + average1 + "\n");
        //System.out.println("WorstSelect: " + worst2);
        //System.out.println("AvgSelect: " + average2 + "\n");

    }
    
    //
    // Main.
    //
    public static void main(String[] s)
    {
	DeterministicSelect obj = new DeterministicSelect();
	int attempts = 10;
    obj.runtests(10,attempts);
    obj.runtests(101,attempts);
    obj.runtests(501,attempts);
    obj.runtests(1001,attempts);
    obj.runtests(5001,attempts);
    obj.runtests(10001,attempts);
    obj.runtests(20001,attempts);
    obj.runtests(30001,attempts);
    obj.runtests(50001,attempts);
    obj.runtests(100000,attempts);
    
    
    }
}
