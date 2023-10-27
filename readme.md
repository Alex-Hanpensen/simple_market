Objective: To build a simple market simulator that can process orders and update the order book accordingly.

Skills Tested: Python programming, understanding of algorithms, and software design principles.

Estimated Time: 3-4 hours

Task Description:

Design the Order Class:

Create an Order class with attributes like order_id, timestamp, type (buy/sell), quantity, and price.
Design the Order Book:

Create an OrderBook class that maintains a list of buy and sell orders.
Implement methods to add, modify, and remove orders from the order book.
Order Matching Algorithm:

Implement a method in the OrderBook class to match orders.
The method should match the highest price buy order with the lowest price sell order.
If the order can’t be matched, it should be added to the order book.
Market Simulator:

Create a function to simulate the market.
It should generate random orders and pass them to the order book.
It should periodically match orders in the order book and print out the trades.
Testing:

Write unit tests to ensure your classes and methods are working as expected.
Deliverables:

Python script(s) with classes and functions implemented.
A text file explaining your design choices and any assumptions you made.
Unit tests and their results.