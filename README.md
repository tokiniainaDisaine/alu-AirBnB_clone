# AirBnB Clone - The Console

## Project Description

This is the first step towards building a full web application: an **AirBnB clone**. This project implements a command-line interpreter (console) to manage AirBnB objects. The console serves as the foundation for the subsequent projects, including HTML/CSS templating, database storage, API, and front-end integration.

The command interpreter allows you to:
- Create new objects (e.g., User, State, City, Place)
- Retrieve objects from a file or database
- Perform operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

This project emphasizes:
- **Object-Oriented Programming (OOP)** in Python
- **Serialization/Deserialization** of instances to JSON files
- **Command-line interface** development
- **Unit testing** with the `unittest` module
- **Data modeling** and class relationships

---

## Command Interpreter

The command interpreter is a custom shell that allows you to interact with the AirBnB objects through a command-line interface. It's similar to a basic Unix shell but is limited to specific use cases for managing the application's data.

### How to Start the Command Interpreter

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/alu-AirBnB_clone.git
   cd alu-AirBnB_clone
   ```

2. **Make sure you have Python 3 installed:**
   ```bash
   python3 --version
   ```

3. **Run the console in interactive mode:**
   ```bash
   ./console.py
   ```
   
   You should see the prompt:
   ```
   (hbnb)
   ```

4. **Run the console in non-interactive mode:**
   ```bash
   echo "help" | ./console.py
   ```

### How to Use the Command Interpreter

Once the console is running, you can use the following commands:

#### **Available Commands:**

| Command | Description | Syntax |
|---------|-------------|--------|
| `create` | Creates a new instance of a class | `create <ClassName>` |
| `show` | Prints the string representation of an instance | `show <ClassName> <id>` |
| `destroy` | Deletes an instance based on class name and id | `destroy <ClassName> <id>` |
| `all` | Prints all string representations of instances | `all` or `all <ClassName>` |
| `update` | Updates an instance based on class name and id | `update <ClassName> <id> <attribute> "<value>"` |
| `quit` | Exits the console | `quit` |
| `EOF` | Exits the console (Ctrl+D) | `EOF` |
| `help` | Displays help information | `help` or `help <command>` |

#### **Alternative Syntax:**

The console also supports an alternative syntax for certain commands:

- `<ClassName>.all()` - Retrieves all instances of a class
- `<ClassName>.count()` - Retrieves the number of instances of a class
- `<ClassName>.show(<id>)` - Retrieves an instance based on its ID
- `<ClassName>.destroy(<id>)` - Destroys an instance based on its ID
- `<ClassName>.update(<id>, <attribute name>, <attribute value>)` - Updates an instance
- `<ClassName>.update(<id>, <dictionary representation>)` - Updates an instance with a dictionary

---

## Examples

### Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create
Creates a new instance of BaseModel, saves it, and prints the id
Usage: create <ClassName>

(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907

(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2024, 1, 8, 10, 30, 0, 123456), 'updated_at': datetime.datetime(2024, 1, 8, 10, 30, 0, 123456)}

(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2024, 1, 8, 10, 30, 0, 123456), 'updated_at': datetime.datetime(2024, 1, 8, 10, 30, 0, 123456)}"]

(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 name "My First Model"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2024, 1, 8, 10, 30, 0, 123456), 'updated_at': datetime.datetime(2024, 1, 8, 10, 32, 15, 789012), 'name': 'My First Model'}

(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **

(hbnb) quit
$
```

### Non-Interactive Mode

```bash
$ echo "create BaseModel" | ./console.py
(hbnb) 49faff9a-6318-451f-87b6-910505c55907

$ echo "show BaseModel 49faff9a-6318-451f-87b6-910505c55907" | ./console.py
(hbnb) [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2024, 1, 8, 10, 30, 0, 123456), 'updated_at': datetime.datetime(2024, 1, 8, 10, 30, 0, 123456)}

$ echo "all" | ./console.py
(hbnb) ["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2024, 1, 8, 10, 30, 0, 123456), 'updated_at': datetime.datetime(2024, 1, 8, 10, 30, 0, 123456)}"]
```

### Alternative Syntax Examples

```bash
$ ./console.py
(hbnb) User.create()
246c227a-d5c1-403d-9bc7-6a47bb9f0f68

(hbnb) User.all()
["[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'created_at': datetime.datetime(2024, 1, 8, 10, 35, 0, 456789), 'updated_at': datetime.datetime(2024, 1, 8, 10, 35, 0, 456789)}"]

(hbnb) User.count()
1

(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'created_at': datetime.datetime(2024, 1, 8, 10, 35, 0, 456789), 'updated_at': datetime.datetime(2024, 1, 8, 10, 35, 0, 456789)}

(hbnb) User.update("246c227a-d5c1-403d-9bc7-6a47bb9f0f68", "first_name", "John")
(hbnb) User.update("246c227a-d5c1-403d-9bc7-6a47bb9f0f68", {'last_name': "Doe", 'age': 25})

(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'created_at': datetime.datetime(2024, 1, 8, 10, 35, 0, 456789), 'updated_at': datetime.datetime(2024, 1, 8, 10, 40, 22, 987654), 'first_name': 'John', 'last_name': 'Doe', 'age': 25}

(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
(hbnb) User.count()
0

(hbnb) quit
$
```

---

## Available Classes

The following classes are available in the console:

- **BaseModel** - The base class for all models
- **User** - Represents a user
- **State** - Represents a state/region
- **City** - Represents a city
- **Amenity** - Represents an amenity
- **Place** - Represents a place/property
- **Review** - Represents a review

---

## File Structure

```
alu-AirBnB_clone/
├── console.py              # Command interpreter
├── models/                 # Package containing all models
│   ├── __init__.py        # Initializes the models package
│   ├── base_model.py      # BaseModel class
│   ├── user.py            # User class
│   ├── state.py           # State class
│   ├── city.py            # City class
│   ├── amenity.py         # Amenity class
│   ├── place.py           # Place class
│   ├── review.py          # Review class
│   └── engine/            # Storage engine package
│       ├── __init__.py
│       └── file_storage.py # FileStorage class
├── tests/                 # Package containing all unit tests
│   ├── __init__.py
│   └── test_models/       # Tests for models
│       ├── __init__.py
│       ├── test_base_model.py
│       ├── test_user.py
│       ├── test_state.py
│       ├── test_city.py
│       ├── test_amenity.py
│       ├── test_place.py
│       ├── test_review.py
│       └── test_engine/
│           ├── __init__.py
│           └── test_file_storage.py
└── README.md              # This file
```

---

## Testing

All tests are located in the `tests` folder and use Python's `unittest` module.

### Run all tests:
```bash
python3 -m unittest discover tests
```

### Run tests for a specific module:
```bash
python3 -m unittest tests/test_models/test_base_model.py
```

### Run tests in non-interactive mode:
```bash
echo "python3 -m unittest discover tests" | bash
```

---

## Authors

- **Your Name** - [GitHub Profile](https://github.com/yourusername)

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgments

- ALU (African Leadership University) for the project requirements
- The Holberton School AirBnB project for inspiration
- All contributors and peers who provided feedback