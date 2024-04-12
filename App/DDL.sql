DROP TABLE IF EXISTS Admistrative_Staff CASCADE;
DROP TABLE IF EXISTS Manage CASCADE;
DROP TABLE IF EXISTS Personal_Training_Session CASCADE;
DROP TABLE IF EXISTS Fitness_Goals CASCADE;
DROP TABLE IF EXISTS Health_Metrics CASCADE;
DROP TABLE IF EXISTS Attend CASCADE;
DROP TABLE IF EXISTS Room_Booking CASCADE;
DROP TABLE IF EXISTS Equipment_Maintenance CASCADE;
DROP TABLE IF EXISTS Class_Schedule CASCADE;
DROP TABLE IF EXISTS Group_Fitness_Class CASCADE;
DROP TABLE IF EXISTS Billing CASCADE;
DROP TABLE IF EXISTS Trainer CASCADE;
DROP TABLE IF EXISTS Member CASCADE;
CREATE TABLE Member (
    member_id SERIAL PRIMARY KEY,
    member_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20)
);
CREATE TABLE Trainer (
    trainer_id SERIAL PRIMARY KEY,
    trainer_name VARCHAR(100) NOT NULL,
    available_date DATE,
    start_available_time TIME,
    end_available_time TIME
);
CREATE TABLE Personal_Training_Session (
    session_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Member(member_id) ON DELETE CASCADE,
    trainer_id INT REFERENCES Trainer(trainer_id) ON DELETE CASCADE,
    session_date DATE,
    start_session_time TIME,
    end_session_time TIME
);
CREATE TABLE Group_Fitness_Class (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(100) NOT NULL
);
CREATE TABLE Attend (
    attend_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Member(member_id) ON DELETE CASCADE,
    class_id INT REFERENCES Group_Fitness_Class(class_id) ON DELETE CASCADE
);
CREATE TABLE Fitness_Goals (
    goal_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Member(member_id) ON DELETE CASCADE,
    weight_goal DECIMAL,
    time_goal INT
);
CREATE TABLE Health_Metrics (
    metric_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Member(member_id) ON DELETE CASCADE,
    weight DECIMAL,
    height DECIMAL
);
CREATE TABLE Room_Booking (
    room_id SERIAL PRIMARY KEY,
    room_name VARCHAR(100) NOT NULL,
    booking_date DATE,
    start_time TIME,
    end_time TIME
);
CREATE TABLE Admistrative_Staff (
    staff_id SERIAL PRIMARY KEY,
    staff_name VARCHAR(100) NOT NULL
);
CREATE TABLE Equipment_Maintenance (
    maintenance_id SERIAL PRIMARY KEY,
    equipment_name VARCHAR(100) NOT NULL,
    staff_id INT REFERENCES Admistrative_Staff(staff_id) ON DELETE CASCADE,
    room_id INT REFERENCES Room_Booking(room_id) ON DELETE CASCADE
);
CREATE TABLE Class_Schedule (
    class_schedule_id SERIAL PRIMARY KEY,
    class_id INT REFERENCES Group_Fitness_Class(class_id) ON DELETE CASCADE,
    staff_id INT REFERENCES Admistrative_Staff(staff_id) ON DELETE CASCADE,
    class_date DATE,
    start_class_time TIME,
    end_class_time TIME
);
CREATE TABLE Billing (
    billing_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Member(member_id) ON DELETE CASCADE,
    staff_id INT REFERENCES Admistrative_Staff(staff_id) ON DELETE CASCADE,
    amount_due INT
);
CREATE TABLE Manage(
    manage_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES Member(member_id) ON DELETE CASCADE,
    staff_id INT REFERENCES Admistrative_Staff(staff_id) ON DELETE CASCADE
);