# To Find Common Divisor and Greatest Common Divisor

---

## 두 수를 입력 받고 공약수와 최대공약수를 출력하는 프로그램(Fail)
* C언어 수업 도중 교수님께서 출제하신 문제의 일부입니다. 유클리드 호제법으로 접근해봤으나 결국 해결하지 못하였습니다. 아래의 코드가 제가 작성한 코드입니다. 참고로, 재귀함수는 아직 배우지 않아서 코드에 사용할 수 없었습니다.

---

```C
#include <stdio.h>

// Finding Common Divisor and Greatest Common Divisor
// SnapFlip20

int main(void)
{
	int num, answer;
	int num1 = 0; // bigger number
	int num2 = 0; // smaller number
	int gcd = 0;

	printf("Input two integers: ");
	scanf("%d %d", &answer, &num);

	if (num > answer)
	{
		num1 = num;
		num2 = answer;
	}
	else
	{
		num1 = answer;
		num2 = num;
	}

	while (1) // Euclidean algorithm(if num2 == 0, num1 and num2 are coprime integers.)
	{
		if (num2 == 1) // if coprime
		{
			printf("%d and %d are coprime integers.\n", answer, num);
			break;
		}
		if (num2 == 0) // else
		{
			gcd = num1; // set greatest common divisor as gcd
			
			printf("%d and %d have common divisor: ", answer, num);
			
			// gcd's divisors are same as common divisors
			for (int i = 1; i <= gcd; i++) // finding gcd
			{
				if (gcd % i == 0) printf("%d ", i);
			}

			printf(", so %d and %d are not coprime integers.\n", answer, num);

			break;
		}

		int change = num1;
		num1 = num2;
		num2 = change % num2;
	}

	return 0;
}
```
### Input-Output Example
```
ex 1)
Input two integers: 48 120
48 and 120 have common divisor: 1 2 3 4 6 8 12 24 , so 48 and 120 are not coprime integers.

ex 2)
Input two integers: 13 47
13 and 47 are coprime integers.
```

### Summary

* In 7st line, 'num' and 'answer' are integers.(in original problems, variable 'answer' is mutable.)
* In 16~25th line, compare 'num' and 'answer' and set num1 = max('num', 'answer'), num2 = min('num', 'answer')
* In 27~54th line(while loop), run Euclidean algorithm 

---

## 느낀 점
* PS 스타일의 문제를 항상 Python으로만 풀다가 C언어로 풀어보니 적응이 잘 안되는 것 같습니다.(특히 Big Integer를 다루는 부분들...) 이 코드도 '결과만 제대로 내뱉게 하자!'는 생각으로 무작정 작성한 코드인데, C언어 문법에 대한 숙지도가 낮다 보니 코드가 많이 지저분해진 것 같습니다. 결국 유클리드 호제법은 접어두고 이중 반복문을 사용해 문제를 해결하기로 했습니다.
