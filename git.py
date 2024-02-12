def sum_numbers(numbers):
    result = 0
    for number in numbers:
        if number > 0:
            result += number
    return result


if __name__ == "__main__":
    print(sum_numbers([5, 10, -5, 15]))
