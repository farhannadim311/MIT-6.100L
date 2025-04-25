This repository holds all the Problem Sets I solved as I took MIT's [6.100L: Introduction to Computer Science and Programming Using Python (Fall 2022)](https://ocw.mit.edu/courses/6-100-introduction-to-computer-science-and-programming-in-python-fall-2022/).

---

## 🧩 PSET 1

We had to write a script which can determine, based on your income and other factors, the number of months it will take for you to save up for a down payment for a house. We also had to find the optimal interest rate in which we could afford the down payment of a house within three years.

**Learning Outcomes –**
- Introduction to control flow in Python
- Formulating a computational solution to a problem
- Exploring bisection search

---

## 🕹️ PSET 2

I had to recreate the popular hangman game in Python. Read a list of words from a file, created helper functions, and simulated a full hangman game against the computer. Implemented a hint functionality in the game as well which can give the user a letter of the word in exchange for number of attempts.

**Learning Outcomes –**
- Writing and calling functions in Python
- Using loop mechanisms to repeat a computational process until a condition is reached

---

## 📊 PSET 3

I had to write a program that analyzes and compares two text files using word and letter frequency statistics. It calculates similarity scores, identifies the most frequent words, and computes TF-IDF values to evaluate word significance across multiple documents.

**Learning Outcomes –**
- Using dictionaries to efficiently store, update and manage data
- Exploring and understanding various data analytics approaches such as TF-IDF

---

## 🌲 PSET 4

This problem set focused on **recursion**, **tree data structures**, and **encryption using one-time pads**. It was divided into three parts:

- **Part A:** Involved working with binary trees. I used a `Node` class to construct and traverse trees recursively. Implemented a function to calculate the height of a tree and created a generalized heap validator that could check for both min-heaps and max-heaps using a comparator function.

- **Part B:** Introduced object-oriented programming in Python. I built a message encryption system using ASCII character shifting and implemented encryption via one-time pads. This involved writing classes for `Message`, `PlaintextMessage`, and `EncryptedMessage` with appropriate class methods for shifting, applying pads, and encrypting text.

- **Part C:** Extended the encryption logic to decrypt messages when given multiple possible one-time pads. I implemented a method to try all pads and determine which one yields the most valid English words, using a provided dictionary and helper functions. This part concluded with decrypting a hidden story.

**Learning Outcomes –**
- Practicing recursion through tree traversal and manipulation
- Implementing class hierarchies with inheritance and encapsulation
- Applying character encoding principles using ASCII values
- Strengthening understanding of encryption/decryption fundamentals
- Performing brute-force decryption using heuristic scoring with real words


# 📦 PSET 5

## Overview
This project was completed as part of MIT's 6.100L (Introduction to Computer Science and Programming Using Python).  
The assignment focused on using libraries to manipulate images, simulate different types of colorblindness, and extract hidden images through steganography techniques.  
It involved working with pixel-level data, matrix transformations, and bit manipulation.

## Features
- Simulated red, green, and blue colorblindness effects via matrix transformations.
- Converted images to pixel lists and reconstructed images from manipulated pixel data.
- Extracted hidden black-and-white and RGB images embedded in the least significant bits (LSBs).
- Rescaled hidden images to enhance contrast and visibility.
- Watermarked processed images automatically with custom text.

## Skills Used
- Python
- PIL (Pillow) for image processing
- NumPy for matrix operations
- Bit manipulation (binary operations without explicit binary conversion)
- Modular software design
- Pixel-level image data handling

## Learning Outcomes
- Gained hands-on experience using external Python libraries (Pillow and NumPy) to solve real-world problems.
- Strengthened understanding of image representation and pixel manipulation techniques.
- Practiced matrix multiplication and binary arithmetic for transforming and extracting data.
- Learned the fundamentals of steganography by recovering hidden images.
- Applied modular coding practices for clean, extensible, and testable Python code.
