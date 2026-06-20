*This activity has been created as part of the 42 curriculum by aspthiba, nmak*

## Description
This project is created with the purpose of taking a disordered list of integers, with optional flags, and sorting them using 2 stacks with the following commands:
- Push (pushes the top element to the other stack)
	- Push a {pa} (pushes from b to a)
	- Push b {pb} (pushes from a to b)
	- Push both {pp} (swaps the top elements between a and b)
- Swap (swaps the top 2 elements of a stack)
	- Swap a {sa} (swaps the top 2 elements of a)
	- Swap b {sb} (swaps the top 2 elements of b)
	- Swap both {ss} (swaps the top 2 elements of both stacks)
- Rotate (shift all elements in a stack up one, first element becomes the last)
	- Rotate a {ra} (rotate stack a)
	- Rotate b {rb} (rotate stack b)
	- Rotate both {rr} (rotate both stacks)
- Reverse rotate (shift all elements in a stack down one, last element becomes the first)
	- Reverse rotate a {rra} (reverse rotate stack a)
	- Reverse rotate b {rrb} (reverse rotate stack b)
	- Reverse rotate both {rrr} (reverse rotate both stacks)

This program uses a disorder calculation to adaptively determine the proper algorithm to use if other flags are not provided, selecting O(n^2) algorithm Insertion Sort if disorder is < 0.2, O(n sqrt(n)) algorithm Bucket Sort if disorder is >= 0.2 and < 0.5, and O(n log n) algorithm Radix Sort if disorder if >= 0.5.

The program tracks the type and amount of actions required to sort the list and prints them in the order they are executed. If the program is in Benchmark Mode (activated with flag `--bench`) it prints a block of text after the operations describing:
- The calculated disorder as a percentage
- The selected strategy (Adaptive, Simple, Medium, Complex) and the selected algorithm
- The total amount of operations
- a list of each operation and the amount of times it was used

The `--adaptive`, `--simple`, `--medium`, and `--complex` flags work by enforcing a specific selection method in the choosing of algorithms.
- `--adaptive` is the default mode, selecting based on disorder
- `--simple` always chooses the O(n^2) option, Insertion Sort
- `--medium` always chooses the O(n sqrt(n)) option, Bucket Sort
- `--complex` always chooses the O(n log n) option, Radix Sort

## Instructions
This project contains a Makefile with the rules: all, clean, fclean, and re. the project can be compiled with the 'make' command. it can be cleaned by the 'make fclean' command, and it can be recompiled by the 'make re' command.

Compiling this project using the Makefile creates a file `push_swap`, which can be used with the command `./push_swap (arguments)`

The push_swap program comes with the following strategy selector flags:
`--simple`, `--medium`, `--complex`, `--adaptive`, and `--bench`
These flags must be placed between `./push_swap` and the program arguments. The default selection is `--adaptive`.

## Resources
The [Makefile manual](https://www.gnu.org/software/make/manual/html_node/)

[This video](https://www.youtube.com/watch?v=AAwYzYkjNTg) to get familiarized with algorithms

[This blog](https://leofu890806.medium.com/push-swap-tutorial-fa746e6aba1e) for more infos on radix adaptation and bitwise operations

No AI was used in this project.

## Details
Insertion sort was selected after testing Bubble Sort and Shaker Sort. It was faster on small stacks and easier to adapt for the other algorithms.
Insertion sort works by “splitting” the list in two parts, sorted and unsorted and following these steps:
1. Taking the first element in the unsorted list
2. Swapping it with the previous element as long as it is bigger than the first element
3. Repeating steps 1 and 2 until the unsorted list is empty

Bucket sort was chosen for its compatability with the normalizer required for Radix Sort as well as Insertion sort, and thus was easiest to implement.
Bucket sort works by splitting the stack in approximately (n√n) buckets and following these steps:
1. Pushing every element to stack b
2. Sending every number in the range of the current bucket to stack a
3. Applying insertion sort to that bucket
4. Repeating steps 2 and 3 until stack b is empty

Radix sort was chosen for its ease of implementation after attempting to implement quicksort.
Radix sort functions by following these steps:
1. Normalize the numbers to remove negative integers and potentially reduce the length of the biggest number. This makes radix sort faster since it reads bits.
2. Read stack a and send every number (in binary) with a 0 at n position to stack b
3. Send back every element from stack b to stack a
4. Repeat steps 2 and 3 while incrementing n by 1 until n is the length of the biggest number in binary
