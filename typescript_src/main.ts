// Typing function parameters (keep return type implicit)
function greet(name: string) {
    return `Hello ${name}!`
}

const greetAlt2 = (name: string) => {
    return `Hello ${name}!`
}

const greetAlt3 = (name: string) => `Hello ${name}!`

// Typing function return parameters
const judgeMyAge = (age: number): string => {
    if (age < 5) {
        return "So cuuute!"
    }

    if (age < 18) {
        return "Wow, you have grown since last year!"
    }

    return "Welcome to adulthood!"
}

// Optional function parameter
const optinalFoo = (bar?: string) => {
    return bar ?? "No input"
}

// Classes
class Human {
    nrOfLegs = 2
}

class Person {
    private static idCounter = 0
    readonly id!: number
    name!: string
    age!: number

    constructor(name: string, age?: number) {
        this.id = Person.getId()
        this.name = name
        this.age = age ?? 0
    }

    private static getId() {
        return Person.idCounter++
    }

    get ageAndName() {
        return this.age ? `${this.name} [${this.age}]` : this.name
    }

    rename(newName: string) {
        this.name = newName
    }
}

// Typed dict
type Movie = {
    title: string
    releaseYear: number
    rating: 1 | 2 | 3 | 4 | 5
    comments: string[]
    sequel?: string
}

let m1: Movie = {
    title: "Star Wars: A New Hope",
    releaseYear: 1977,
    rating: 5,
    comments: [],
}