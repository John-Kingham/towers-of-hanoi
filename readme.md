# Codecademy - Computer Science Career Path - Towers of Hanoi 
## Description
A small project based on the towers of [Hanoi game](https://en.wikipedia.org/wiki/Tower_of_Hanoi).

## Goal
To practice using stacks and the basic features of Python.

## Rules of the game
- The game starts with a stack of different sized disks, ordered from largest (on the bottom) to smallest (on the top)
- The objective of the game is to move the disks to form a new stack
- Only one disk can be moved at a time
- Each move consists of taking the upper disk from one stack and using it to start a new stack, or placing it on top of an existing stack
- Up to three stacks are allowed at any one time
- Larger disks cannot be placed on top of smaller disks

## Implementation

### Version 1.0
The three stacks will be implemented as instances of a Stack class, with the typical behaviour of a stack (push, pop, peek).
The game is written entirely in a single `main` function.

### Version 2.0
Version 1.0 was written entirely in a single `main` function, which mixes together the game code and the user interface code. This is a bad idea because I may want to change the interface at some point, to give the game a desktop GUI or a web interface.

This version separates out the game code from the current terminal interface code.

I've also added unit tests and also used the Black Formatter extension.