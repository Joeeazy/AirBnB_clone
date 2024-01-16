# 0x00. AirBnB clone - The console

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General

* How to create a Python package = [Packages](https://intranet.alxswe.com/rltoken/Vn5hOrJ9IHds7we9udPnNg)

* How to create a command interpreter in Python using the cmd module = [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)

* What is Unit testing and how to implement it in a large project = [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)

* How to serialize and deserialize a Class

* How to write and read a JSON file

* How to manage datetime

* What is an UUID

* What is *args and how to use it [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)

* What is **kwargs and how to use it [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)


* How to handle named arguments in a function

# Files and Directories

models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.

tests directory will contain all unit tests.

console.py file is the entry point of our command interpreter.

models/base_model.py file is the base class of all our models. It contains common elements:

attributes: id, created_at and updated_at

methods: save() and to_json()

models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

# Storage

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)

Provide default value of any attribute

In the future, provide the same model behavior for file storage or database storage

# Steps

You won’t build this application all at once, but step by step.

Each step will link to a concept:

* The console

* create your data model

* manage (create, update, destroy, etc) objects via a console / command interpreter

* store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

# Installation

To Use the AIrBnB clone, clone the repository to your local machine and run the console.py file:

1. Clone the repository:

    ```bash
    git clone git clone https://github.com/Joeeazy/AirBnB_clone.git
    ```

2. Navigate to the project directory:

    ```bash
    cd AirBnB_clone
    ```

3. Run the console script:

    ```bash
    ./console.py
    ```
# Web static, what?
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

Create simple HTML static pages

 Style guide

* Fake contents

* No Javascript

* No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

[AirBnB clone](https://intranet.alxswe.com/concepts/74)
