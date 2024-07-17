import random
import tracemalloc
import resource

# Lista de 100 enteros
lista_100 = [random.randint(1, 1000) for _ in range(100)]
# Lista de 300 enteros
lista_300 = [random.randint(1, 1000) for _ in range(300)]
# Lista de 500 enteros
lista_500 = [random.randint(1, 1000) for _ in range(500)]

def quicksort(array):
    if len(array) < 2:
        return array    # Base case: arrays with 0 or 1 element are already sorted.
    else:
        pivot = array[0]    # Recursive case
        less = [i for i in array[1:] if i <= pivot] # Sub-array of all the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot]   # Sub-array of all the elements greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)

def main():
    # Start tracing memory allocations
    tracemalloc.start()

    # Get memory usage before algorithm
    mem_before = tracemalloc.get_traced_memory()[0]

    # Measure CPU time
    start_cpu = resource.getrusage(resource.RUSAGE_SELF).ru_utime
    
    # Algorithm Execution
    result = quicksort(lista_500.copy())  # Use a copy to not affect original list
    
    end_cpu = resource.getrusage(resource.RUSAGE_SELF).ru_utime

    # Get memory usage after algorithm
    mem_after = tracemalloc.get_traced_memory()[0]

    # Stop tracing memory allocations
    tracemalloc.stop()

    # Calculate CPU time
    cpu_time = end_cpu - start_cpu

    # Calculate memory used by the algorithm
    memory_used = (mem_after - mem_before) / (1024 * 1024)  # Convert to MiB

    print(f"CPU time: {cpu_time:.6f} seconds")
    print(f"Memory used by algorithm: {memory_used:.6f} MiB")

if __name__ == "__main__":
    main()