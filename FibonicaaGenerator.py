import logging

# Set up logging
logging.basicConfig(filename='fibonacci.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FibonacciGenerator:
    def __init__(self, limit):
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("Limit must be a positive integer")
        self.limit = limit
        self.sequence = []

    def generate(self):
        logging.info('Starting to generate Fibonacci sequence up to %d', self.limit)
        try:
            self.sequence = [self.fibonacci(i) for i in range(self.limit)]
            logging.info('Successfully generated the Fibonacci sequence: %s', self.sequence)
        except Exception as e:
            logging.error('Error generating Fibonacci sequence: %s', e)
            raise

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

    def get_sequence(self):
        return self.sequence

if __name__ == "__main__":
    try:
        limit = int(input("Enter the number of Fibonacci numbers to generate: "))
        fib_generator = FibonacciGenerator(limit)
        fib_generator.generate()
        print(f"The first {limit} Fibonacci numbers are: {fib_generator.get_sequence()}")
    except ValueError as ve:
        logging.error('Invalid input: %s', ve)
        print(f"Error: {ve}")
    except Exception as e:
        logging.error('Unexpected error: %s', e)
        print(f"An unexpected error occurred: {e}")
