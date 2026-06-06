import psycopg2
from config import connection_string

# List of gadgets to add
gadgets = [
    ('Apple iPhone 13', 'Latest iPhone with 5G and Pro Camera', 40.00, 'Available'),
    ('Apple MacBook Pro 16-inch', 'Powerful laptop for professionals', 80.00, 'Available'),
    ('Bose QuietComfort 35 II', 'Premium noise-cancelling headphones', 20.00, 'Available'),
    ('Canon DSLR', 'Professional Canon DSLR Camera', 60.00, 'Available'),
    ('Canon EOS 5D Mark IV', 'Full-frame professional camera', 75.00, 'Rented'),
    ('Dell Laptop', 'Dell XPS high-performance laptop', 45.00, 'Available'),
    ('DJI Phantom 4 Pro', 'Professional drone with 4K camera', 85.00, 'Available'),
    ('Epson Projector', 'High-brightness presentation projector', 35.00, 'Available'),
    ('Fujifilm X-T4', 'Mirrorless digital camera', 65.00, 'Available'),
    ('Google Pixel 6', 'Google flagship smartphone', 38.00, 'Available'),
    ('GoPro Hero 9 Black', 'Action camera for adventure', 25.00, 'Available'),
    ('HP Spectre x360', 'Convertible premium laptop', 55.00, 'Available'),
    ('iPad Air', 'Powerful tablet device', 30.00, 'Available'),
    ('JBL Flip 5', 'Portable Bluetooth speaker', 18.00, 'Rented'),
    ('Logitech G Pro X', 'Professional gaming headset', 22.00, 'Available'),
    ('Microsoft Surface Pro 7', 'Tablet-laptop hybrid device', 50.00, 'Available'),
    ('Nikon D850', 'Professional DSLR camera', 70.00, 'Available'),
    ('Oculus Quest 2', 'VR headset for gaming', 40.00, 'Available'),
    ('Razer DeathAdder Elite', 'Professional gaming mouse', 15.00, 'Available'),
    ('Samsung Galaxy S22', 'Latest Samsung flagship phone', 42.00, 'Available'),
    ('Samsung QLED 65-inch', 'Premium 4K smart TV', 60.00, 'Available'),
    ('Sony A7 III', 'Full-frame mirrorless camera', 72.00, 'Available'),
]

try:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    
    # Clear existing gadgets
    cursor.execute("DELETE FROM Gadgets;")
    
    # Insert new gadgets
    for name, desc, price, status in gadgets:
        cursor.execute(
            "INSERT INTO Gadgets (name, description, price_per_day, status) VALUES (%s, %s, %s, %s)",
            (name, desc, price, status)
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    
    print(f"✅ Successfully added {len(gadgets)} gadgets to the database!")
    
except Exception as e:
    print(f"❌ Error: {e}")
