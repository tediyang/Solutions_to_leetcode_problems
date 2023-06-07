#include <stdio.h>


int minFlips(int a, int b, int c) {

	int flip = 0;

	while (a != 0 || b != 0 || c != 0) {
		/* Get the bit value for the current int*/
		char a_ =  (a & 1) + '0';
		char b_ = (b & 1) + '0';
		char c_ = (c & 1) + '0';

		while ((a_ | b_) != c_) {
			/* if c == '1' then we only have to flip either a or b 
			   but if c == '0' we have to check either a or b to flip */
			if (c_ == '1') {
				flip++;
				a_ = '1';
			}
			if (c_ == '0' && a_ == '1')
			{
				flip++;
				a_ = '0';
			}
			if (c_ == '0' && b_ == '1') {
				flip++;
				b_ = '0';
			}
		}

		/* then we use right shift to change the values*/
		a >>= 1;
		b >>= 1;
		c >>= 1;
	}
	return flip;
}
