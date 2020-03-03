import java.util.Random;

class BankAccount{
    private String accountNumber; 
    private double checkingBalance; 
    private double savingsBalance; 
    private static int numberOfAccounts;
    private static double totalAmountInAccount;


// create constructor 
public BankAccount(){
    generateNewAccountNumber();
}

public String getAccountNumber(){
    return accountNumber;
}

private String generateNewAccountNumber(){
    String numbers = "0123456789";
    String newAccountNumber = "";

    Random rand = new Random();

    for (int i = 0; i < 5; i++){
        int num = numbers.charAt(rand.nextInt(10));
        newAccountNumber += num; 
    }
    
    accountNumber = newAccountNumber; 

    return newAccountNumber;
}

public void setCheckingBalance(double checkingBalance){
    this.checkingBalance = checkingBalance;
}

public double getCheckingBalance(){
    System.out.println("The checking balance for this account is : $" + this.checkingBalance);
    return this.checkingBalance;
}

public void setSavingsBalance(double savingsBalance){
    this.savingsBalance = savingsBalance;
}

public double getSavingsBalance(){
    System.out.println("The savings balance for this account is : $" + this.savingsBalance);
    return this.savingsBalance;

}

public void depositChecking(double checkingBalance){
    this.setCheckingBalance(checkingBalance);
    totalAmountInAccount += checkingBalance;
}

public void depositSavings(double savingsBalance){
    this.setSavingsBalance(savingsBalance);
    totalAmountInAccount += savingsBalance;
}

public double total(){
    totalAmountInAccount = savingsBalance + checkingBalance;
    return totalAmountInAccount;
}

public void withdrawalChecking(int amount){
    if (getCheckingBalance() < Double.valueOf(amount)){
        System.out.println("You don't have enought money to take out more money.");
    } 
    else{
        setCheckingBalance(getCheckingBalance() - Double.valueOf(amount));

    }
}

public void withdrawalSavings(int amount){
    if (getSavingsBalance() < Double.valueOf(amount)){
        System.out.println("You don't have enought money to take out more money.");
    } 
    else{
        this.setSavingsBalance(this.getSavingsBalance() - Double.valueOf(amount));
    }

}
}

public class BankAccountTest{
    public static void main(String[] args){

        BankAccount account1 = new BankAccount();
        
        System.out.println("The bank account number for this account is : " + account1.getAccountNumber());
        account1.getCheckingBalance();
        account1.getSavingsBalance();
        account1.depositChecking(100);
        account1.depositSavings(1000);
        account1.withdrawalChecking(100);
        System.out.println(account1.getCheckingBalance());
        account1.withdrawalSavings(75);
        System.out.println(account1.getSavingsBalance());
        account1.total();
        System.out.println("The total amount in both the checking and savings accounts for this account is : $" + account1.total());
        
   }
}