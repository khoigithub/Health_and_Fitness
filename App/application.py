import psycopg2

#Connecting to database
def connection():
    try:
        connection = psycopg2.connect(host="localhost", database="health_fitness", user="postgres", password="postgres", port="5432")
        cursor = connection.cursor()
        return connection, cursor
    except:
        print("Error connecting to Database!")

#main function
def main():
    print("Input your number (0 - 24):")
    print("0. To quit application")
    print("1. Add new Member")
    print("2. Update a member's info")
    print("3. Display a member's info")
    print("4. Display a member's dashboard")
    print("5. Add new Trainer")
    print("6. Schedule personal training")
    print("7. Cancel personal training")
    print("8. Display personal training session")
    print("9. Schedule group fitness class")
    print("10. Display fitness class")
    print("11. Trainer set available time")
    print("12. Display personal trainer available time")
    print("13. Trainer search for a Member's name")
    print("14. Add more room")
    print("15. Get all room")
    print("16. Delete a room")
    print("17. Add more equipment")
    print("18. Get all equipment")
    print("19. Delete an equipment")
    print("20. Update class schedule")
    print("21. Display class schedule")
    print("22. Get all bills")
    print("23. Delete a bill")
    print("24. Member pay the bill")
    

    while True:
        try: 
            options = int(input("What is your options: \n"))
            if options == 0:
                print("Quitting...")
                return
            elif options == 1:
                name = input("What is the member's name: \n")
                email = input("What is the member's email address: \n")
                phone = input("What is the member's phone number: \n")
               
                weight = input("What is your current weight (in lbs): \n")
                height = input("What is your current height (in cm): \n")
                
                new_weight = input("What is your new weight goals (in lbs): \n")    
                time = input("How long you think you can achieve that goals (in days): \n")

                staff_id = input("Who is the staff manage this member? \n")

                id = addMember(name, email, phone, weight, height, new_weight, time)
                addBill(id, 0, staff_id)
            elif options == 2:
                member_id = input("What is the member's id you want to update: \n")    
                name = input("What is the new name: \n")
                email = input("What is the new email: \n")
                phone = input("What is the new phone: \n")

                weight = input("What is your new weight (in lbs): \n")
                height = input("What is your new height (in cm): \n")

                new_weight = input("What is your new weight goals (in lbs): \n")    
                time = input("How long you think you can achieve that goals (in days): \n")

                updateMemberInfo(member_id, name, email, phone, weight, height, new_weight, time)
            elif options == 3:
                member_id = input("What is the member's id you want to display: \n")    

                displayInfo(member_id)
            elif options == 4:
                member_id = input("What is the member's id you want to display: \n")    

                displayDashboard(member_id)
            elif options == 5:
                trainer_name = input("What is the trainer's name: \n")
                available_date = input("What is the trainer's available date: \n")
                start_available_time = input("What is the trainer's start available time: \n")
                end_available_time = input("What is the trainer's end available time: \n")

                addTrainer(trainer_name, available_date, start_available_time, end_available_time)
            elif options == 6:
                member_id = input("What is the member's id that you want to schedule personal training: \n")
                trainer_id = input("What is the id of the trainer you want to schedule with? \n")
                date = input("Which date do you want to schedule (YYYY-MM-DD): \n")
                start_time = input("What start time do you want to schedule: \n")
                end_time = input("What end time do you want to schedule: \n")

                schedulePT(member_id, trainer_id, date, start_time, end_time)
            elif options == 7:
                member_id = input("What is the member's id that wants to cancel personal training: \n")
                trainer_id = input("What is the id of the trainer you want to cancel your training sessions with? \n")

                cancelPT(member_id, trainer_id)
            elif options == 8:
                
                displayPTSession()
            elif options == 9:
                member_id = input("What is the member's id that you want to schedule fitness class: \n")
                class_id = input("Which class do you want to attend: \n")

                scheduleFC(member_id, class_id)
            elif options == 10:
                
                displayFC()
            elif options == 11:
                id = input("What is the trainer's id you want to update available time: \n")
                date = input("What is your available date (YYYY-MM-DD): \n")
                start_time = input("What is the new start available time: \n")
                end_time = input("What is the new end available time: \n")

                updateAvailableTime(id, date, start_time, end_time)
            elif options == 12:

                displayPT()
            elif options == 13:
                name = input("What is the member's name you want to search: \n")

                searchByName(name)
            elif options == 14:
                name = input("What is the name of this room: \n")
                date = input("What is the booking date for the room (YYYY-MM-DD): \n")
                start_time = input("What is the start time for this room: \n")
                end_time = input("What is the end time for this room: \n")

                addRoom(name, date, start_time, end_time)
            elif options == 15:
                displayRooms()
            elif options == 16:
                room_id = input("What is the room's id that you want to delete: \n")

                deleteRoom(room_id)
            elif options == 17:
                name = input("What is the name of this equipment: \n")
                room_id = input("What is the room's id to book to maintain this equipment: \n")
                staff_id = input("Who is the staff responsible to maintain this equipment: \n")

                addEquipment(name, room_id, staff_id)
            elif options == 18:
                displayEquipment()
            elif options == 19:
                e_id = input("What is the equipment's id that you want to delete: \n")

                deleteEquipment(e_id)
            elif options == 20:
                class_id = input("Which class's id that you want to update schedule: \n")
                date = input("What is the new date for this class (YYYY-MM-DD): \n")
                start_time = input("What is the new start time for this class: \n")
                end_time = input("What is the new end time for this class: \n")

                updateClassSchedule(class_id, date, start_time, end_time)
            elif options == 21:
                displayClassSchedule()
            elif options == 22:
                displayBill()
            elif options == 23:
                bill_id = input("What is the bill's id that you want to delete: \n")

                deleteBill(bill_id)
            elif options == 24:
                bill_id = input("Who is the customer that wants to pay the bill: \n")

                payBill(bill_id)
            else:
                print("Invalid options, please try again")
            
        except:
            print("Error running loop")

def getAllMembers():
    conn, cursor = connection()

    try:
        cursor.execute("SELECT * FROM Member")
        members = cursor.fetchall()
        for member in members:
            print(member)
    except:
        print("Error getting data from Member database")
    finally:
        cursor.close()
        conn.close()

def addMember(name, email, phone, weight, height, new_weight, time):
    conn, cursor = connection()

    try: 
        cursor.execute("INSERT INTO Member (member_name, email, phone_number) VALUES (%s, %s, %s)", (name, email, phone))
        cursor.execute("SELECT member_id FROM Member WHERE email = %s AND phone_number = %s", (email, phone))
        id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO Health_Metrics (member_id, weight, height) VALUES (%s, %s, %s)", (id, weight, height))
        cursor.execute("INSERT INTO Fitness_Goals (member_id, weight_goal, time_goal) VALUES (%s, %s, %s)", (id, new_weight, time))

        conn.commit()
        print("Sucessfully added new member")
        return id
    except:
        print("Error adding new member to Member database")
    finally:
        cursor.close()
        conn.close()

def updateMemberInfo(member_id, name, email, phone, weight, height, new_weight, time):
    conn, cursor = connection()

    try: 
        if name != "":
            cursor.execute("UPDATE Member SET member_name = %s WHERE member_id = %s", (name, member_id))
            conn.commit()
            print("Sucessfully update name!")
        if email != "":
            cursor.execute("UPDATE Member SET email = %s WHERE member_id = %s", (email, member_id))
            conn.commit()
            print("Sucessfully update email!")
        if phone != "":
            cursor.execute("UPDATE Member SET phone_number = %s WHERE member_id = %s", (phone, member_id))
            conn.commit()
            print("Sucessfully update phone!")
        if weight != "":
            cursor.execute("UPDATE Health_Metrics SET weight = %s WHERE member_id = %s", (weight, member_id))
            conn.commit()
            print("Sucessfully update new current weight!")
        if height != "":
            cursor.execute("UPDATE Health_Metrics SET height = %s WHERE member_id = %s", (height, member_id))
            conn.commit()
            print("Sucessfully update new current height!")
        if new_weight != "":
            cursor.execute("UPDATE Fitness_Goals SET weight_goal = %s WHERE member_id = %s", (new_weight, member_id))
            conn.commit()
            print("Sucessfully update new weight goal!")
        if time != "":
            cursor.execute("UPDATE Fitness_Goals SET time_goal = %s WHERE member_id = %s", (time, member_id))
            conn.commit()
            print("Sucessfully update new time goal!")
        
    except:
        print("Error updating to Member database")
    finally:
        cursor.close()
        conn.close()

def displayInfo(member_id):
    conn, cursor = connection()

    try:
        cursor.execute("SELECT * FROM Member WHERE member_id = %s", (member_id))
        member = cursor.fetchone()
        print(member)
    except:
        print("Error getting data from Member database")
    finally:
        cursor.close()
        conn.close()

def displayDashboard(member_id):
    conn, cursor = connection()

    try: 
        fitness_goals_query = "SELECT TO_CHAR(weight_goal, '999.99'), time_goal FROM Fitness_Goals WHERE member_id = %s;"
        cursor.execute(fitness_goals_query, (member_id))
        fitness_goals = cursor.fetchone()
        print("\nFitness Goals:")
        print("The weight you want to achieve is (in lbs): ", fitness_goals[0])
        print("The time you want to achieve that weight is (in days): ", fitness_goals[1])

        health_stat = "SELECT TO_CHAR(weight, '999.99'), TO_CHAR(height, '999.99') FROM Health_Metrics WHERE member_id = %s;"
        cursor.execute(health_stat, (member_id))
        health = cursor.fetchone()
        print("\nYour health statistics:")
        print("Your current weight is: ", health[0])
        print("Your current height is: ", health[1])

    except:
        print("Error displaying dashboard!")
    finally:
        cursor.close()
        conn.close()

def addDashboard(member_id, weight, time):
    conn, cursor = connection()

    try: 
        check_query = """
            SELECT COUNT(*)
            FROM Fitness_Goals
            WHERE member_id = %s;
        """
        cursor.execute(check_query, (member_id))
        count = cursor.fetchone()[0]

        if count > 0:
            update_query = """
                UPDATE Fitness_Goals
                SET weight_goal = %s, time_goal = %s
                WHERE member_id = %s;
            """
            cursor.execute(update_query, (weight, time, member_id))
        else:
            insert_query = """
                INSERT INTO Fitness_Goals (member_id, weight_goal, time_goal)
                VALUES (%s, %s, %s);
            """
            cursor.execute(insert_query, (member_id, weight, time))
        conn.commit()
        print("Successfully ADD or UPDATE new fitness goals!")
    except:
        print("Error adding new goals database")
    finally:
        cursor.close()
        conn.close()

def schedulePT(member_id, trainer_id, date, start_time, end_time):
    conn, cursor = connection()

    try: 
        query = """
            SELECT TO_CHAR(available_date, 'YYYY-MM-DD'), TO_CHAR(start_available_time, 'HH24:MI'), 
            TO_CHAR(end_available_time, 'HH24:MI') FROM Trainer 
            WHERE trainer_id = %s
        """
        cursor.execute(query, (trainer_id))
        output = cursor.fetchone()
        a_date = output[0]
        s_time = output[1]
        e_time = output[2]

        if a_date != date:
            print("Trainer is not available on this date")
            return
        
        if start_time < s_time or end_time > e_time:
            print("Trainer is not available in this time range")
            return

        query = """
            SELECT COUNT(*)
            FROM Personal_Training_Session
            WHERE member_id = %s AND trainer_id = %s
        """

        cursor.execute(query, (member_id, trainer_id))
        output = cursor.fetchone()[0]
        if output > 0:
            update_query = """
                UPDATE Personal_Training_Session
                SET session_date = %s, start_session_time = %s, end_session_time = %s
                WHERE member_id = %s AND trainer_id = %s;
            """
            cursor.execute(update_query, (date, start_time, end_time, member_id, trainer_id))

        else:
            insert_query = """
                INSERT INTO Personal_Training_Session (member_id, trainer_id, session_date, start_session_time, end_session_time)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (member_id, trainer_id, date, start_time, end_time))

        updateAmount(member_id, 50, False)

        conn.commit()
        print("Successfully add new personal training session!")
    except:
        print("Error adding new goals database")
    finally:
        cursor.close()
        conn.close()

def cancelPT(member_id, trainer_id):
    conn, cursor = connection()

    try:
        cursor.execute("DELETE FROM Personal_Training_Session WHERE member_id = %s AND trainer_id = %s", (member_id, trainer_id))
        conn.commit()
        print("Successfully cancel training session with PT")
        updateAmount(member_id, 50, True)
    except:
        print("Error canceling training session")
    finally:
        cursor.close()
        conn.close()

def displayPTSession():
    conn, cursor = connection()

    try:
        query = """
            SELECT m.member_name, t.trainer_name, p.session_date, p.start_session_time, p.end_session_time
            FROM Member m
            JOIN Personal_Training_Session p ON p.member_id = m.member_id
            JOIN Trainer t ON t.trainer_id = p.trainer_id
        """
        cursor.execute(query)
        items = cursor.fetchall()
        for item in items:
            print(item)
    except:
        print("Error displaying PT Session")
    finally:
        cursor.close()
        conn.close()

def addTrainer(name, available_date, start_available_time, end_available_time):
    conn, cursor = connection()

    try: 
        query = """
            INSERT INTO Trainer (trainer_name, available_date, start_available_time, end_available_time) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, available_date, start_available_time, end_available_time))

        conn.commit()
        print("Sucessfully added new trainer")
        return id
    except:
        print("Error adding new trainer")
    finally:
        cursor.close()
        conn.close()

def scheduleFC(member_id, class_id):
    conn, cursor = connection()
    try:
        query = """
            SELECT COUNT(*)
            FROM Attend
            WHERE member_id = %s AND class_id = %s
        """

        cursor.execute(query, (member_id, class_id))
        output = cursor.fetchone()[0]

        if output == 0:
            query = """
                INSERT INTO Attend (member_id, class_id)
                VALUES (%s, %s)
            """
            cursor.execute(query, (member_id, class_id))
            conn.commit()
            print("Successfully schedule fitness class!")
            updateAmount(member_id, 100, False)
    except:
        print("Error adding new goals database")
    finally:
        cursor.close()
        conn.close()

def displayFC():
    conn, cursor = connection()

    try:
        query = """
            SELECT m.member_name, f.class_name 
            FROM Member m
            JOIN Attend a ON m.member_id = a.member_id
            JOIN Group_Fitness_Class f ON f.class_id = a.class_id
        """
        cursor.execute(query)
        items = cursor.fetchall()
        for item in items:
            print(item)
    except:
        print("Error display schedule for fitness class")
    finally:
        cursor.close()
        conn.close()

def updateAvailableTime(id, date, start_time, end_time):
    conn, cursor = connection()
    try: 
        query = """
            UPDATE Trainer SET start_available_time = %s, end_available_time = %s, 
            available_date = %s 
            WHERE trainer_id = %s;
            """
        cursor.execute(query, (start_time, end_time, date, id))
        conn.commit()
        print("Successfully update available time!")
    except:
        print("Error searching new members")
    finally:
        cursor.close()
        conn.close()

def displayPT():
    conn, cursor = connection()

    try: 
        cursor.execute("SELECT * FROM Trainer")
        trainers = cursor.fetchall()
        for trainer in trainers:
            print(trainer)
    except:
        print("Error displaying trainers available time")
    finally:
        cursor.close()
        conn.close()

def searchByName(name):
    conn, cursor = connection()
    
    try: 
        if name == "":
            getAllMembers()
            return
        cursor.execute("SELECT * FROM Member WHERE member_name = %s;", (name,))

        members = cursor.fetchall()

        if members:
            for member in members:
                print(member)
        else:
            print("No member found with name:", members)
    except Exception as e:
        print(e)
        print("Error searching members")
    finally:
        cursor.close()
        conn.close()

def addRoom(name, date, start_time, end_time):
    conn, cursor = connection()

    try: 
        cursor.execute("INSERT INTO Room_Booking (room_name, booking_date, start_time, end_time) VALUES (%s, %s, %s, %s)", (name, date, start_time, end_time))
        conn.commit()
        print("Sucessfully added new room")
    except:
        print("Error adding new room")
    finally:
        cursor.close()
        conn.close()

def displayRooms():
    conn, cursor = connection()

    try: 
        cursor.execute("SELECT * FROM Room_Booking")
        rooms = cursor.fetchall()
        for room in rooms:
            print(room)
    except:
        print("Error displaying all room")
    finally:
        cursor.close()
        conn.close()

def deleteRoom(room_id):
    conn, cursor = connection()

    try: 
        cursor.execute("DELETE FROM Room_Booking WHERE room_id = %s", (room_id))
        conn.commit()
        print("Sucessfully delete room!")
    except:
        print("Error deleting room")
    finally:
        cursor.close()
        conn.close()

def addEquipment(name, room_id, staff_id):
    conn, cursor = connection()

    try: 
        cursor.execute("INSERT INTO Equipment_Maintenance (equipment_name, staff_id, room_id) VALUES (%s, %s, %s)", (name, staff_id, room_id))
        conn.commit()
        print("Sucessfully added new equipment")
    except Exception as e:
        print(e)
        print("Error adding new equiment")
    finally:
        cursor.close()
        conn.close()

def displayEquipment():
    conn, cursor = connection()

    try: 
        query = """
            SELECT e.equipment_name, r.room_name, a.staff_name
            FROM Equipment_Maintenance e 
            JOIN Room_Booking r ON e.room_id = r.room_id
            JOIN Admistrative_Staff a ON a.staff_id = e.staff_id 
        """
        cursor.execute(query)
        equipments = cursor.fetchall()
        for e in equipments:
            print(e)
    except:
        print("Error displaying all equipment")
    finally:
        cursor.close()
        conn.close()

def deleteEquipment(e_id):
    conn, cursor = connection()

    try: 
        cursor.execute("DELETE FROM Equipment_Maintenance WHERE maintenance_id = %s", (e_id))
        conn.commit()
        print("Sucessfully delete Equipment!")
    except:
        print("Error deleting equipment")
    finally:
        cursor.close()
        conn.close()

def updateClassSchedule(class_id, date, start_time, end_time):
    conn, cursor = connection()
    try: 
        if date != "":
            query = """
                UPDATE Class_Schedule
                SET class_date = %s
                WHERE class_id = %s 
            """
            cursor.execute(query, (date, class_id))
            conn.commit()
            print("Sucessfully update class date!")
        if start_time != "":
            query = """
                UPDATE Class_Schedule
                SET start_class_time = %s
                WHERE class_id = %s 
            """
            cursor.execute(query, (start_time, class_id))
            conn.commit()
            print("Sucessfully update start time for the class!")
        if end_time != "":
            query = """
                UPDATE Class_Schedule
                SET end_class_time = %s
                WHERE class_id = %s 
            """
            cursor.execute(query, (end_time, class_id))
            conn.commit()
            print("Sucessfully update end time for the class!")
        conn.commit()
    except:
        print("Error schedule new fitness class")
    finally:
        cursor.close()
        conn.close()

def displayClassSchedule():
    conn, cursor = connection()

    try: 
        query = """
            SELECT g.class_name, c.class_date, c.start_class_time, c.end_class_time, a.staff_name
            FROM Class_Schedule c 
            JOIN Group_Fitness_Class g ON g.class_id = c.class_id
            JOIN Admistrative_Staff a ON a.staff_id = c.staff_id
        """
        cursor.execute(query)
        conn.commit()
        schedules = cursor.fetchall()
        for s in schedules:
            print(s)
    except:
        print("Error displaying class schedule!")
    finally:
        cursor.close()
        conn.close()

def addBill(member_id, amount, staff_id):
    conn, cursor = connection()

    try: 
        cursor.execute("INSERT INTO Billing (member_id, amount_due, staff_id) VALUES (%s, %s, %s)", (member_id, amount, staff_id))
        conn.commit()
        print("Sucessfully added new bill")
    except:
        print("Error adding new bill")
    finally:
        cursor.close()
        conn.close()

def displayBill():
    conn, cursor = connection()

    try: 
        query = """
            SELECT m.member_name, b.amount_due, a.staff_name
            FROM Billing b 
            JOIN Member m ON m.member_id = b.member_id
            JOIN Admistrative_Staff a ON a.staff_id = b.staff_id
        """
        cursor.execute(query)
        conn.commit()
        bills = cursor.fetchall()
        for bill in bills:
            print(bill)
    except:
        print("Error displaying all bill")
    finally:
        cursor.close()
        conn.close()

def deleteBill(bill_id):
    conn, cursor = connection()

    try: 
        cursor.execute("DELETE FROM Billing WHERE billing_id = %s", (bill_id))
        conn.commit()
        print("Sucessfully delete bill!")
    except:
        print("Error deleting bill")
    finally:
        cursor.close()
        conn.close()

def updateAmount(member_id, amount, cancel):
    conn, cursor = connection()

    try: 
        query = """
            SELECT amount_due
            FROM Billing
            WHERE member_id = %s
        """
        cursor.execute(query, (member_id))
        amount_due = cursor.fetchone()[0]
        if not cancel:
            amount_due += amount
            query = """
                UPDATE Billing
                SET amount_due = %s
                WHERE member_id = %s 
            """
            cursor.execute(query, (amount_due, member_id))
        else:
            amount_due -= amount
            query = """
                UPDATE Billing
                SET amount_due = %s
                WHERE member_id = %s 
            """
            cursor.execute(query, (amount_due, member_id))
        conn.commit()
        print("Successfully update bill!")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def payBill(bill_id):
    conn, cursor = connection()

    try: 
        cursor.execute("UPDATE Billing SET amount_due = 0 WHERE billing_id = %s", (bill_id))
        conn.commit()
        print("Sucessfully paid the bill!")
    except:
        print("Error paying the bill")
    finally:
        cursor.close()
        conn.close()

main()




