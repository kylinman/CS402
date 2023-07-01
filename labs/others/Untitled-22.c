// This is your sixth self-evaluated lab. Remember, you will need to submit the result of this lab to move on to the next module. 

// Estimated Time: 1hr

// Attempt: 1

// How to Pass: Run your lab successfully on your C compiler.

// What to Do：

// Step1-Use below program and create proper functions as declared:

#include <stdio.h>
/*global variable declaration */
int ag 100;
int sum(int a,int b);
int increaseval(int a,int b);
int main ()
/*local variable declaration in main function*/
int a 10;
int b 20;
int c=0;
printf("value of global variable ag in main()=%dn",ag);
printf ("value of a in main()%d n",a);
printf ("value of b in main()=%d\n",b);
c increaseval(a,b);
printf ("value of c in main()after increaseval()=%d\n",c);
c sum(a,b);
printf ("value of c in main()=%d\n",c);
return 0;

// Suggested Output-
value of global variable ag in main()=100
value of a in main ()10
value of b in main()=20
value of global variable ag in i
increaseval()=100
value of a in increaseval()
=110
value of b in increaseval()=120
value of c in main()after increaseval()=230
value of global variable ag in sum()=100
value of a in sum()=10
value of b in sum()=20
value of c in main()=30

// Submission: Submit your code as well as a screenshot of the output in a PDF file.  