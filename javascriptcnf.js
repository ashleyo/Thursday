class Person {
    constructor(name, city) {
        this.name = name;
        this.city = city;
    }

    toString = () => `Person(name=${this.name}, city=${this.city})`;

}

person1 = Person("Alice", "New York");
console.log(person1) 
// #region BREAK

// Demonstration of the Person class
const person1 = new Person("Alice", "New York");
const person2 = new Person("Bob", "Los Angeles");

console.log(person1.toString());
console.log(person2.toString());

// A function to generate the arithmetic mean of an iterable ignoring non-numbers
function mean(iterable) {
    const numbers = iterable.filter(item => typeof item === 'number');
    return numbers.reduce((acc, val) => acc + val, 0) / numbers.length;
}

// The same code but defined as an arrow function and assigned to the variable mean2
const mean2 = (iterable) => {
    const numbers = iterable.filter(item => typeof item === 'number');
    return numbers.reduce((acc, val) => acc + val, 0) / numbers.length;
};

function add(a,b) {
    return a + b;
}

const add2 = (a,b) => a + b;



// Demo both give same result
console.log(mean([1, 2, 3, "four", 5]));
console.log(mean2([1, 2, 3, "four", 5]));

// #endregion
