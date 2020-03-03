import java.util.*;

class PrintX{
    public static void main(String args[]){
        int n;
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number: ");
        n = scan.nextInt();
        scan.close();
        for(int i=0;i<2*n-1;i++){
            for(int j=0;j<2*n-1;j++){
                if(i==j || j==(2*n-2)-i) System.out.print('*');
                else System.out.print(' ');
            }
            System.out.println("");
        }
    }
}