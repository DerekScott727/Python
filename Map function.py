def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]     ##This applies the double function to each element in the sequence list
doubled = map[(double, sequence)   ##This is another way of doing that, using the 'map' keyword it tells python to use the double function against the entirety of the sequence list


