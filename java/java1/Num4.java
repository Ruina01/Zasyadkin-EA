public class Num4 {
    public static void main(String[] args){
            String name = "G";
            String password = "3333";
            if ((name.equals(args[0]) && password.equals(args[1])) || (name.equals(args[1]) && password.equals(args[0]))) {
                System.out.println("Dobro pozhalovat");
            } else {
                System.out.println("Login i parol ne raspoznan. Dostup zaprezhen");
            }

        }
    }

