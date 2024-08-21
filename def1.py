# 소수 판별 함수
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
#2. 에라토스테네스의 체 (특정 범위 내의 많은 소수를 한 번에 찾아야 하는 상황에서 매우 유용한 알고리즘)
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)  # n까지의 수를 소수로 가정
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:  # i가 소수라면
            for j in range(i*i, n + 1, i):  # i의 배수를 False로 표시
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i]]