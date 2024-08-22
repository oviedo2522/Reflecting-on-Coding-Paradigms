Activity: Reflecting on Coding Paradigms

In this activity, we will get a chance to express what we've learned so far in regards to the paradigms of Functional and Object-Oriented Programming in Python. The activity will be completed in a few distinct stages. The first step will consist of implementing a solution to a problem for each coding style. Once a solution that adheres to the coding paradigm has been implemented, there are several questions to answer. These questions pertain to how and why the coding paradigm in question helps us solve the problem. When answering these questions, it may be helpful to envision an interview setting. The final part of the activity consists of a writing prompt to reflect on the past two modules, and your personal impressions of them.

Getting Started

Create a Replit named Reflecting on Coding Paradigms using the Python template. Do your work and write your answers for the following prompts in the generated main.py file. For the thought prompts, write your answers as comments. As you work through the prompts, be sure to add comments titling what section each solution is for.

Functional Prompt

Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

Remember, when writing in a functional style: Keep variables immutable Write only pure functions Remember, functions may be higher order Once a functional solution to this problem has been implemented, answer the following questions. How does this solution ensure data immutability? Is this solution a pure function? Why or why not? Is this solution a higher order function? Why or why not? Would it have been easier to solve this problem using a different programming style? Why in particular is functional programming a helpful paradigm when solving this problem?

Object Oriented Prompt

Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. Define a repair() method that will update the condition of the podracer to "repaired". Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2. Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed". Once an Object Oriented solution has been implemented, answer the following questions: How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply) Encapsulation Abstraction Inheritance Polymorphism Would it have been easier to implement a solution to this problem using a different coding style? Why or why not? How in particular did Object Oriented Programming assist in the solving of this problem?

Reflection

Take some time now to think about the lessons we've just covered. Prompting questions have been provided, but reflections do not need to be limited to only their answers.

Is one of these coding paradigms "better" than the other? Why or why not? Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why? Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming? Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?

Solution

Use this link if you get stuck or need to check your work.

Acceptance Criteria
When scrolling through your Replit, it should be easy to tell what section your solutions belong to with commented titles. When running your Replit, there should be no errors displayed in the console. If there are errors you could not solve, comment out the lines throwing errors and explain what steps you used to try and fix them. Make sure your thought question answers are commented out. Given an array of integers in random order, running it through your pure function solution should sort it in ascending order. Given a pod created from your defined Podracer class, running pod.repair() and printing the pod.condition afterwards should display "repaired" in the console. Given another new_pod created from your defined AnakinsPod class with a max_speed of 2, running new_pod.boost() and printing the new_pod.max_speed afterwards should display "4". Given a third_pod created from your defined SebulbasPod class, running third_pod.flame_jet() and printing the third_pod.condition afterwards should display "thrashed" in the console. Before submitting, make sure you do a self review of your code, check for formatting, spelling, and include comments in your code.

Make sure to submit your Replit link on the submission page.
