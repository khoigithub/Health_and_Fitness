--Add Member
INSERT INTO Member(member_name, email, phone_number)
VALUES ('Tom', 'tom@gmail.com', '1111111111');
INSERT INTO Member(member_name, email, phone_number)
VALUES ('Cruise', 'cruise@gmail.com', '2838882222');
INSERT INTO Member(member_name, email, phone_number)
VALUES ('Kevin', 'kevin@gmail.com', '6130001111');
INSERT INTO Member(member_name, email, phone_number)
VALUES ('Hart', 'hart@gmail.com', '3439281922');

--Add Fitness Goals for Members
INSERT INTO Fitness_Goals(member_id, weight_goal, time_goal)
VALUES (1, 150.5, 10);
INSERT INTO Fitness_Goals(member_id, weight_goal, time_goal)
VALUES (2, 200, 20);
INSERT INTO Fitness_Goals(member_id, weight_goal, time_goal)
VALUES (3, 130, 30);
INSERT INTO Fitness_Goals(member_id, weight_goal, time_goal)
VALUES (3, 160, 60);

--Add Health Metrics for Members
INSERT INTO Health_Metrics(member_id, weight, height)
VALUES (1, 200, 180);
INSERT INTO Health_Metrics(member_id, weight, height)
VALUES (2, 170, 185);
INSERT INTO Health_Metrics(member_id, weight, height)
VALUES (3, 150, 155);
INSERT INTO Health_Metrics(member_id, weight, height)
VALUES (3, 150, 160);


--Add Trainers
INSERT INTO Trainer (
        trainer_name,
        available_date,
        start_available_time,
        end_available_time
    )
VALUES ('James', '2024-09-12', '13:00', '15:00');
INSERT INTO Trainer (
        trainer_name,
        available_date,
        start_available_time,
        end_available_time
    )
VALUES ('Bond', '2024-05-01', '8:00', '16:00');
INSERT INTO Trainer (
        trainer_name,
        available_date,
        start_available_time,
        end_available_time
    )
VALUES ('Alex', '2024-06-29', '12:00', '20:00');

--Add Staff
INSERT INTO Admistrative_Staff (staff_name)
VALUES ('Travis');
INSERT INTO Admistrative_Staff (staff_name)
VALUES ('John');
INSERT INTO Admistrative_Staff (staff_name)
VALUES ('Sam');

--Add group fitness class
INSERT INTO Group_Fitness_Class (class_name)
VALUES ('swimming');
INSERT INTO Group_Fitness_Class (class_name)
VALUES ('badminton');
INSERT INTO Group_Fitness_Class (class_name)
VALUES ('volleyball');
INSERT INTO Group_Fitness_Class (class_name)
VALUES ('soccer');

--Add manage
INSERT INTO Manage (member_id, staff_id)
VALUES (1, 1);
INSERT INTO Manage (member_id, staff_id)
VALUES (2, 1);
INSERT INTO Manage (member_id, staff_id)
VALUES (3, 2);

--Add attend
INSERT INTO Attend (class_id, member_id)
VALUES (1, 1);
INSERT INTO Attend (class_id, member_id)
VALUES (2, 1);
INSERT INTO Attend (class_id, member_id)
VALUES (1, 2);
INSERT INTO Attend (class_id, member_id)
VALUES (3, 3);

--Add schedule for those class
INSERT INTO Class_Schedule (
        class_date,
        class_id,
        staff_id,
        start_class_time,
        end_class_time
    )
VALUES ('2020-11-11', 1, 1, '13:00', '15:00');
INSERT INTO Class_Schedule (
        class_date,
        class_id,
        staff_id,
        start_class_time,
        end_class_time
    )
VALUES ('2020-10-10', 2, 2, '08:00', '12:00'); 

--Add Billing for Members
INSERT INTO Billing(member_id, staff_id, amount_due)
VALUES (1, 1, 0);
INSERT INTO Billing(member_id, staff_id, amount_due)
VALUES (2, 2, 0);
INSERT INTO Billing(member_id, staff_id, amount_due)
VALUES (3, 1, 0);
INSERT INTO Billing(member_id, staff_id, amount_due)
VALUES (3, 3, 0);

-- select * from member;
-- select * from trainer;
-- select * from Personal_Training_Session;
-- select * from fitness_goals;
-- select * from health_metrics;
-- select * from Group_Fitness_Class;
-- select * from Class_Schedule;
-- select * from Room_Booking;
-- select * from Equipment_Maintenance;
-- select * from Billing;
-- select * from Admistrative_Staff;
