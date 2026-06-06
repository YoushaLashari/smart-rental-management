-- Create the database
CREATE DATABASE smart_rental_db;

-- Connect to the new database
-- Run the following commands in smart_rental_db database:

-- Create Gadgets table
CREATE TABLE IF NOT EXISTS Gadgets (
    gadget_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price_per_day DECIMAL(10, 2),
    status VARCHAR(20) DEFAULT 'Available'
);

-- Create Rentals table
CREATE TABLE IF NOT EXISTS Rentals (
    rental_id SERIAL PRIMARY KEY,
    customer_id INT,
    gadget_id INT REFERENCES Gadgets(gadget_id),
    rental_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    return_date TIMESTAMP,
    total_cost DECIMAL(10, 2)
);

-- Insert sample gadgets
INSERT INTO Gadgets (name, description, price_per_day, status) VALUES
('Laptop', 'Dell XPS 15 Laptop', 50.00, 'Available'),
('Camera', 'Canon EOS DSLR', 30.00, 'Available'),
('Drone', 'DJI Phantom 4 Pro', 75.00, 'Available'),
('Gaming Console', 'PlayStation 5', 25.00, 'Available'),
('Headphones', 'Sony WH-1000XM4', 15.00, 'Rented');
