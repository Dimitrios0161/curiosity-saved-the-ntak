import rust_primes_generator_lib
import argparse

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('n', type=int, help='N-th prime to compute')
# Parse the argument
args = parser.parse_args()

def compute_Nst_prime(n):
    """ Compute n-th prime with Rust."""
    return rust_primes_generator_lib.primes_generator_cpython(n)

print(compute_Nst_prime(args.n - 1))





