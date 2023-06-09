char nextGreatestLetter(char* letters, int lettersSize, char target){
    int i;

    for (i = 0; i < lettersSize; i++)
        if (letters[i] > target)
            return (letters[i]);
    return (*letters);
}