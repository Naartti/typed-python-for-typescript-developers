# Typed Python For TypeScript Developers
I recently got a new job and went from the fantastic world of TypeScript into the unknowns of typed Python. I found out that typed Python is not as matur as TypeScript and decided to write down a small cheat sheet with some mapping between the two. I hope this summary will aid someone alike me, who's coming from TypeScript and wants to dive into typed Python.

# TL;DR

Create a venv virtual environment with Python 3.9 and install black and pylint. I'd recommend using VS Code with the Python plugin, Pylance language server and the `settings.json` as defined below - a nice dev environment is crucial!

Check out this git repo for exact setup for both TypeScript and typed Python used in this article.

[Cheat Sheet](https://www.notion.so/a7acfa0591d6480594f93617287e40b1)

# Setup

The most important part of getting sped up with typed Python is to have a proper development environment set up. It can be tempting to just use the globally installed Python version and install dependencies directly to it or via anaconda. I strongly advice against this since it will quickly get out of hand and version-conflict-hell across different project will appear. The following section will describe how we can safely set up a typed Python project.

## Don’t underestimate Python versions

The core mechanics of TypeScript has been largely intact for some time, so I never really had to worry about the version. Python on the other hand have just recently released some core features in version 3.9: `dict` (object) and `list` (array). In Python 3.8, these needed to be imported via the standard library `typing` as `Dict` and `List` (note the capitalisation). In this article, I’ll be using Python 3.9.

## No need to install a separate module, though you should

Unlike TypeScript, typing comes built into Python. The common types (`str`, `float`, `int`, `bool`, `dict`, `list`) are always available and the other types (e.g. `Tuple`, `Union`, `Optional`) are imported from the standard module `typing`.

```python
from typing import Tuple, Union
```

So, why should you install external packages? Because alike TypeScript, type hints does not come in the package. And without type hints, typing is pretty much useless. For typed Python, I’d recommend using [VS Code](https://code.visualstudio.com/) with the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) plugin, [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) as language server, [pylint](https://github.com/PyCQA/pylint) as linter and [black](https://black.readthedocs.io/en/stable/index.html) as code formatter.

Note that **you must** use a virtual environment when working in a Python project if you hold your sanity dear. This could be a virtual environment (like [venv](https://docs.python.org/3/tutorial/venv.html)), a docker image or a virtual environment inside a docker image. For smaller projects, I've used venv but for larger projects I use docker with the VS Code plugin [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

Below is a good starting point for VS Code settings to use with typed Python. If you want to go all in with the typing, switch `python.analysis.typeCheckingMode` to `"strict"`. It will be pretty brutal, especially for all the dependencies with missing type annotations.

```json
{
    "editor.formatOnSave": true,
    "editor.tabSize": 4,
    "python.pythonPath": "${workspaceFolder}/venv/bin/python3.9",
    "python.analysis.extraPaths": [
        "${workspaceFolder}/src",
    ],
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic"
}
```

## Where's the build?

There's no need to build typed Python into non-typed Python in order to run it. If your system have the same Python version then you're ready to go. No need to build, minify or compile anything.

# Let's see some code!

Enough of the setup, let's start coding! The upcoming sections will map syntax and common use cases in TypeScript and how the same scenario would be coded in typed Python.

## Variable type declaration

Alike TypeScript, typed Python does not need to declare types if they are initiated with a value. The type will be inferred.

```tsx
const name = 'Mattias'
const age = 28
const lovesCoding = true
const hobbies: string[] = []
const skills: Record<string, number> = {}
```

```python
name = "Mattias"
age = 28
loves_coding = True
hobbies: list[str] = []
skills: dict[str, float] = {}
```

## Type annotate the function parameters

For the most part, we only need to annotate the type for function parameters. When the return type is implied, we do not need to explicitly declare it.

```tsx
function greetAlt1(name: string) {
    return `Hello ${name}!`
}

const greetAlt2 = (name: string) => {
    return `Hello ${name}!`
}

const greetAlt3 = (name: string) => `Hello ${name}!`
```

```python
def greet(name: str):
    return f"Hello {name}"
```

In Python, there is another way to declare a function: `lambda`. This approach is mostly used when doing inline-logic, like in an list/dict-comprehension. The `lambda`-function is a bit more tricky to type and requires the `Callable` type from the `typing` lib. `Callable` takes two arguments. The first is a list of parameters and the second is the return type.

```python
from typing import Callable

greet_alt_2: Callable[[str], str] = lambda name: f"Hello {name}"
```

Sometimes it's nice to declare the return type; e.g. functions with multiple return statements can help us detect bugs if we mess up the return typing.

```tsx
const judgeMyAge = (age: number): string => {
    if (age < 5) {
        return "So cuuute!"
    }

    if (age < 18) {
        return "Wow, you have grown since last year!"
    }

    return "Welcome to adulthood!"
}
```

```python
def judge_my_age(age: int) -> str:
    if (age < 5):
        return "So cuuute!"

    if (age < 18):
        return "Wow, you have grown since last year!"

    return "Welcome to adulthood!"
```

Already, we have some leverage of the typing thanks to the type hints. Type declaring the function parameters also functions as a form of documentation.

If you do not get any type hints, make sure to add the `src`-path to your *.vscode/settings.json* under `python.analysis.extraPaths`.

### Optional function parameters

Alike `Callable`, the `Optional` type also needs to be imported from `typing`.

```tsx
const optinalFoo = (bar?: string) => {
    return bar ?? "No input"
}
```

```python
from typing import Optional

def optional_foo(bar: Optional[str]):
    return bar or "No input"
```

In TypeScript, `bar` would be `undefined` if not passed into the function. In Python, it is `None` (similar to TypeScript's `none`).

## Classes

Let's evaluate a class with a few different features. There are not that many type-specific behaviours in the python case. The only thing we need to do is to type the function parameters. The other syntax (like getter- & static decorators) is available in standard Python as well.

```tsx
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
```

```python
from typing import Optional

class Person():
    _id_counter = 0

    def __init__(self, name: str, age: Optional[int]):
        self._id = Person.get_id()
        self.name = name
        self.age = age or 0

    @staticmethod
    def get_id():
        Person._id_counter = Person._id_counter + 1
        return Person._id_counter

    @property
    def age_and_name(self):
        return f"{self.name} [{self.age}]" if self.age else self.name

    def rename(self, new_name: str):
        self.name = new_nam
```

Note that Python does not have private attributes but uses the naming convention of an underscore `_` to convey the intention of an private attribute or function. These can be read and changed from outside the class - but that is bad practise.

## Typed Dict

Closely related to typed classes, we have typed dictionaries. In typed Python the type is defined as a class, but used as a type.

```tsx
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
```

```python
from typing import TypedDict, Literal

class Movie(TypedDict):
    title: str
    release_year: int
    rating: Literal[1, 2, 3, 4, 5]
    comments: list[str]

m_1: Movie = {
    "title": "Star Wars: A New Hope",
    "release_year": 1977,
    "rating": 5,
    "comments": [],
}
```

What about the optional key `sequel`? Unfortunately, Python does not have a nice syntax like TypeScripts' `?`. We can use the `Optional` type, but that does not allow the key to be omitted; only the value is optional (can be `None`). We can get around this issue by adding a `total`-flag to our type class, but that will apply to all attributes and make every attribute optional.

```python
class Movie(TypedDict, total=False):
    title: str
    release_year: int
    rating: Literal[1, 2, 3, 4, 5]
    comments: list[str]
    sequel: Optional[str]
```

Setting the `total=False` flag will make all keys optional and will not show a warning when omitting e.g. `title`.

# Conclusion

There are many similarities between TypeScript and typed Python. If you are learning Python the step to typed Python is very small - but the gains are very large! Take the time to properly set up your dev environment and let the code formatter and linter do the job for you.