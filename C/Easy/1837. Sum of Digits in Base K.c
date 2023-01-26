//#include <stdio.h>

int sumBase(int n, int k)
{
    int result = 0;

    while (n >= k)
    {
        result += n % k; 
        n = n / k;
    }

    result += n;
    return (result); 
}

int main(void)
{
    int case1 = sumBase(34, 6);
    printf("%d\n", case1);
    int case2 = sumBase(42, 2);
    printf("%d\n", case2);
    int case3 = sumBase(10, 10);
    printf("%d\n", case3);
}
