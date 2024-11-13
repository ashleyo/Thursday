class Person:

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __repr__(self):
        return f"Person(name={self.name}, city={self.city})"


# Demonstration of the Person class
if __name__ == "__main__":

    person1 = Person("Alice", "New York")
    person2 = Person("Bob", "Los Angeles")


    print(person1)
    print(person2)


# region Break


# A function to generate the arithmetic mean of  an iterable ignoring non numbers
def mean(iterable):
    numbers = [item for item in iterable if isinstance(item, (int, float))]
    return sum(numbers) / len(numbers)

# The same code but defined as a lambda function and assigned to the variable mean2
mean2 = lambda iterable: sum(
    [item for item in iterable if isinstance(item, (int, float))]
) / len([item for item in iterable if isinstance(item, (int, float))])

# Demo both give same result
if __name__ == "__main__":
    print(mean([1, 2, 3, "four", 5]))
    print(mean2([1, 2, 3, "four", 5]))

# endregion
