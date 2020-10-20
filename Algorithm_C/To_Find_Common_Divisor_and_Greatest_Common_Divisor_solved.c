#include <stdio.h>

// Finding Common Divisor and Greatest Common Divisor(Solved)
// SnapFlip20

int main(void)
{
	int num, answer;
	int num1 = 0; // bigger number
	int num2 = 0; // smaller number
	int gcd = 0;

	printf("Input two integers: ");
	scanf("%d %d", &answer, &num);

    if ((num == answer) && (num != 1)) // if num == answer and num != 1, num and answer are coprime numbers.
	{
		printf("%d and %d have common divisor: ", answer, num);

		for (int i = 1; i <= num; i++)
		{
			if (num % i == 0) printf("%d ", i);
		}

		printf(", so %d and %d are not coprime integers.\n", answer, num);
	}
	else
	{
		int min;
		int gcd = 1;
		int original_num = num;
		int original_answer = answer;

		if (num > answer) min = answer;
		else min = num;

		int i = 2;

		while (i <= min)
		{
			if ((answer % i == 0) && (num % i == 0))
			{
				answer /= i;
				num /= i;
				gcd *= i;

				if (num > answer) min = answer;
				else min = num;

				i = 1;
			}

			i++;
		}

		if (gcd == 1) // if coprime
		{
			printf("%d and %d are coprime integers.\n", original_answer, original_num);
		}
		else
		{
			printf("%d and %d have common divisor: ", original_answer, original_num);

			for (int i = 1; i <= gcd; i++)
			{
				if (gcd % i == 0) printf("%d ", i);
			}

			printf(", so %d and %d are not coprime integers.\n", original_answer, original_num);
		}
	}

	return 0;
}