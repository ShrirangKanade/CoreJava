package TNSIF_Core;
import java.util.*;
public class Hello {

	public static void main(String[] args) {
		System.out.println("Hello World");
		int sum=0,num,rem;
		Scanner sc = new Scanner(System.in);
		num = sc.nextInt();
		
		while(true)
		{ 
			rem = num%10;
			if (rem==0)
				break;
			sum=sum*10+rem;
			num =num/10;
		}
		System.out.println(sum);

	}
	
}
