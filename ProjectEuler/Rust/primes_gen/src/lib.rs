use cpython::{py_fn, py_module_initializer, PyResult, Python};

// initialize Python module and add Rust CPython aware function
py_module_initializer!(
    rust_primes_generator_lib,
    initrust_primes_generator_lib,
    PyInit_rust_primes_generator_lib,
    |py, m | {
        m.add(py, "__doc__", "Prime generator module implemented in Rust")?;
        m.add(
            py,
            "primes_generator_cpython",
            py_fn!(py, primes_generator_cpython(max: usize)
            )
        )?;
        Ok(())
    }
);

/// generate list of primes with length @max and get the last one
fn primes(max: usize)->i32{
    let mut primes = vec![2];
    let mut count = 2;
    loop{
        count += 1;
        if primes.len() < max{
            if primes.iter().all(|p| count % p != 0) {primes.push(count);}
            
            continue;
        }
        
        if primes.len() == max{
            break;
        }
    }
    primes[max-1]
}

///fn main() {
///    println!("{:?}", primes(10001));
///}

/// Rust-CPython aware function
fn primes_generator_cpython(_: Python, max: usize) -> PyResult<i32> {
    let _gil = Python::acquire_gil();
    let generator = primes(max);
    Ok(generator)
}