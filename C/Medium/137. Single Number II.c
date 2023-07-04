/**
 * singleNumber - Find the non-duplicate number in the array
 * @nums: int array
 * @numsSize: size of array
 * 
 * Return: non-dupliate number
*/

int singleNumber(int* nums, int numsSize) {
    int count, ans;
    for (int i = 0; i < numsSize; i++)
    {
        count = 0;
        for (int j = 0; j < numsSize; j++)
            if (nums[i] == nums[j])
                count++;
        if (count == 1)
        {
            ans = nums[i];
            break;
        }
    }
    return (ans);
}
