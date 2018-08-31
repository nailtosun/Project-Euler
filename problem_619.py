import time
def fibonacci(k_th_list):
    fibonacci = [1,1,2,3,5]
    for i in range(k_th_list-len(fibonacci)):
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return fibonacci
def prime_number_list_generator(upper_bound):
    start_time = time.time()
    integer_list = [x for x in range(upper_bound+1)]
    counter = 0
    prime_numbers = []
    for i in range(1,upper_bound):
        start_time = time.time()
        for j in range (1,upper_bound):
            if i>=j and i%j == 0:
                counter = counter + 1
        if counter == 2:
            prime_numbers.append(i)
        counter = 0
    print("--- %s seconds ---" % (time.time() - start_time))
    return prime_numbers
def prime_factors_sum(input_number,prime_numbers):
    j=0
    carrier = []
    i_k = input_number
    while not i_k == 1:
        if i_k % prime_numbers[j] == 0:
            i_k = i_k/prime_numbers[j]
            carrier.append(prime_numbers[j])
        else:
            j = j + 1
    sum = 0
    for i in range(len(carrier)):
        sum = sum + carrier[i]
    return sum
def S(all_pairs,fibonacci,integer_list):
    sum = 0
    for i in range(len(integer_list)):
        if all_pairs[i][1] in fibonacci:
            sum = sum + i
    return sum
fibonacci = fibonacci(24)
prime_numbers = prime_number_list_generator(fibonacci[-1])
prime_factors_sum(fibonacci[-1],prime_numbers)
upper_bound = fibonacci[-1]
integer_list = [x for x in range(upper_bound+1)]
all_pairs = []
for i in range(2,upper_bound+1):
    s = prime_factors_sum(i,prime_numbers)
    pair = [i,s]
    all_pairs.append(pair)
    pair = []
sum = 0
fibonacci=fibonacci[1:]
s = []
for j in range(len(fibonacci)):
    for i in range(len(all_pairs)):
        if all_pairs[i][1] == fibonacci[j]:
            sum = sum + all_pairs[i][0]
    s.append(sum)
    sum = 0
for i in range(len(s)):
    sum = sum + s[i]
