import stats

def main():
    numbers = [3, 2, 5, 6, 5, 2, 2, 7]
    
    try:
        print(f"Mean: {stats.mean(numbers)}")
        print(f"Median: {stats.median(numbers)}")
        print(f"Mode: {stats.mode(numbers)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
