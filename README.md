# 0x00. AirBnB clone - The console

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General

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

# Storage

Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)

Provide default value of any attribute

In the future, provide the same model behavior for file storage or database storage


[AirBnB clone](https://intranet.alxswe.com/concepts/74)
