from flask import Flask, render_template, request, redirect, url_for
import oracledb
from datetime import datetime
from datetime import datetime


app = Flask(__name__)

# Database connection setup
def get_db_connection():
    dsn = oracledb.makedsn('prophet.njit.edu', '1521', 'course')
    conn = oracledb.connect(user='sm3457', password='DMSD-project1', dsn=dsn)
    return conn

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/select_table')
def select_table():
    return render_template('select_table.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        
        name = request.form['name']
        data = request.form['data']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO your_table (name, data) VALUES (:name, :data)", [name, data])
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/read')
def read_animal():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animal")
    data = cursor.fetchall()
    conn.close()
    return render_template('read.html', data=data)

@app.route('/read_building')
def read_building():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM building")
    data = cursor.fetchall()
    conn.close()
    return render_template('read_building.html', data=data)

@app.route('/read_hourlyrate')
def read_hourlyrate():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hourlyrate")
    data = cursor.fetchall()
    conn.close()
    return render_template('read_hourlyrate.html', data=data)

@app.route('/read_revenuetype')
def read_revenuetype():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM revenuetype")
    data = cursor.fetchall()
    conn.close()
    return render_template('read_revenuetype.html', data=data)

@app.route('/read_employee')
def read_employee():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    data = cursor.fetchall()
    conn.close()
    return render_template('read_employee.html', data=data)

@app.route('/read_animalcarespecialist')
def read_animalcarespecialist():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animalcarespecialist")
    data = cursor.fetchall()
    conn.close()
    return render_template('read_animalcarespecialist.html', data=data)

@app.route('/read_species')
def read_species():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM species")
    data = cursor.fetchall()
    conn.close()
    return render_template('read_species.html', data=data)

@app.route('/read_caresfor')
def read_caresfor():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM caresfor")
    data = cursor.fetchall()
    conn.close()
    return render_template('read_caresfor.html', data=data)

@app.route('/read_enclosure')
def read_enclosure():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM enclosure")
    data = cursor.fetchall()
    conn.close()
    return render_template('read_enclosure.html', data=data)

@app.route('/read_revenueevents')
def read_revenueevents():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM revenueevents")
    data = cursor.fetchall()
    conn.close()
    return render_template('read_revenueevents.html', data=data)

@app.route('/read_veterinarian')
def read_veterinarian():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM veterinarian")
    data = cursor.fetchall()
    conn.close()
    return render_template('read_veterinarian.html', data=data)

@app.route('/insert_data', methods=['GET', 'POST'])
def insert_data():
    selected_table = request.args.get('table')
    
    if request.method == 'POST':
        
        if selected_table == 'employee':
            E_ID = request.form.get('E_ID')
            Job_Type = request.form.get('Job_Type')
            Mint = request.form.get('Mint')
            Last = request.form.get('Last')
            Street = request.form.get('Street')
            City = request.form.get('City')
            State = request.form.get('State')
            Zip = request.form.get('Zip')
            H_ID = request.form.get('H_ID')
            FIRST_NAME = request.form.get('FIRST_NAME')
            Start_date_unformatted = request.form.get('Start_date')
            Start_date = datetime.strptime(Start_date_unformatted, "%Y-%m-%d")

        
            print(f"Received data")

            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {selected_table} (E_ID, Start_date, Job_Type, Mint, Last, Street, City, State, Zip, H_ID, FIRST_NAME) VALUES (:E_ID, :Start_date, :Job_Type, :Mint, :Last, :Street, :City, :State, :Zip, :H_ID, :FIRST_NAME)"
            print(f"Executing query: {query}")
            cursor.execute(query, [E_ID, Start_date , Job_Type, Mint, Last, Street, City, State, Zip, H_ID, FIRST_NAME])
            conn.commit()
            conn.close()
            return redirect(url_for('select_table'))
            
            

        
        elif selected_table == 'hourlyrate':

            H_ID = request.form.get('H_ID')
            RATE = request.form.get('RATE')

            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {selected_table} (H_ID, RATE) VALUES (:H_ID, :RATE)"
            cursor.execute(query, [H_ID, RATE])
            conn.commit()
            conn.close()
            return redirect(url_for('select_table'))
    
        
        
        elif selected_table == 'building':
            B_ID = request.form.get('B_ID')
            NAME = request.form.get('NAME')
            TYPE = request.form.get('TYPE')

            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {selected_table} (B_ID, NAME, TYPE) VALUES (:B_ID, :NAME, :TYPE)"
            cursor.execute(query, [B_ID, NAME, TYPE])
            conn.commit()
            conn.close()
            return redirect(url_for('select_table'))
        
        elif selected_table == 'revenuetype':
                RID = request.form.get('RID')
                NAME = request.form.get('NAME')
                TYPE = request.form.get('TYPE')
                PER_DAY = request.form.get('PER_DAY')
                ADULT_PRICE = request.form.get('ADULT_PRICE')
                SENIOR_PRICE = request.form.get('SENIOR_PRICE')
                PRODUCT = request.form.get('PRODUCT')
                B_ID = request.form.get('B_ID')

                conn = get_db_connection()
                cursor = conn.cursor()
                query = f"INSERT INTO {selected_table} (RID, NAME, TYPE, PER_DAY, ADULT_PRICE, SENIOR_PRICE, PRODUCT, B_ID) VALUES (:RID, :NAME, :TYPE, :PER_DAY, :ADULT_PRICE, :SENIOR_PRICE, :PRODUCT, :B_ID)"
                cursor.execute(query, [RID, NAME, TYPE, PER_DAY, ADULT_PRICE, SENIOR_PRICE, PRODUCT, B_ID])
                conn.commit()
                conn.close()
                return redirect(url_for('select_table'))
        
        elif selected_table == 'animalcarespecialist':
                E_ID = request.form.get('E_ID')
                S_ID = request.form.get('S_ID')

                conn = get_db_connection()
                cursor = conn.cursor()
                query = f"INSERT INTO {selected_table} (E_ID, S_ID) VALUES (:E_ID, :S_ID)"
                cursor.execute(query, [E_ID, S_ID])
                conn.commit()
                conn.close()
                return redirect(url_for('select_table'))

        elif selected_table == 'species':
            S_ID = request.form.get('S_ID')
            NAME = request.form.get('NAME')
            AVERAGE_FOOD_COST = request.form.get('AVERAGE_FOOD_COST')

            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {selected_table} (S_ID, NAME, AVERAGE_FOOD_COST) VALUES (:S_ID, :NAME, :AVERAGE_FOOD_COST)"
            cursor.execute(query, [S_ID, NAME, AVERAGE_FOOD_COST])
            conn.commit()
            conn.close()
            return redirect(url_for('select_table'))

        elif selected_table == 'caresfor':
            E_ID = request.form.get('E_ID')
            S_ID = request.form.get('S_ID')

            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {selected_table} (E_ID, S_ID) VALUES (:E_ID, :S_ID)"
            cursor.execute(query, [E_ID, S_ID])
            conn.commit()
            conn.close()
            return redirect(url_for('select_table'))
        elif selected_table == 'enclosure':
            EN_ID = request.form.get('EN_ID')
            SQFT = request.form.get('SQFT')
            B_ID = request.form.get('B_ID')

            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {selected_table} (EN_ID, SQFT, B_ID) VALUES (:EN_ID, :SQFT, :B_ID)"
            cursor.execute(query, [EN_ID, SQFT, B_ID])
            conn.commit()
            conn.close()
            return redirect(url_for('select_table'))
        elif selected_table == 'revenueevents':
            #R_DATE = request.form.get('R_DATE')
            REVENUE = request.form.get('REVENUE')
            TICKETS_SOLD = request.form.get('TICKETS_SOLD')
            S_ID = request.form.get('S_ID')
            RID = request.form.get('RID')
            R_date_unformatted = request.form.get('Start_date')
            R_DATE = datetime.strptime(R_date_unformatted, "%Y-%m-%d")

            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {selected_table} (R_DATE, REVENUE, TICKETS_SOLD, S_ID, RID) VALUES (:R_DATE, :REVENUE, :TICKETS_SOLD, :S_ID, :RID)"
            cursor.execute(query, [R_DATE, REVENUE, TICKETS_SOLD, S_ID, RID])
            conn.commit()
            conn.close()
            return redirect(url_for('select_table'))
            
        elif selected_table == 'veterinarian':
            E_ID = request.form.get('E_ID')
            A_ID = request.form.get('A_ID')

            conn = get_db_connection()
            cursor = conn.cursor()
            query = f"INSERT INTO {selected_table} (E_ID, A_ID) VALUES (:E_ID, :A_ID)"
            cursor.execute(query, [E_ID, A_ID])
            conn.commit()
            conn.close()
            return redirect(url_for('select_table'))

    return render_template('insert_data.html', table=selected_table)

@app.route('/select_record_to_modify', methods=['GET', 'POST'])
def select_record_to_modify():
    if request.method == 'POST':
        selected_table = request.form.get('table')
        primary_key_column = request.form.get('primary_key_column')
        primary_key_value = request.form.get('primary_key_value')
        return redirect(url_for('modify_record', 
                                table=selected_table, 
                                pk_col=primary_key_column, 
                                pk_val=primary_key_value))

    return render_template('select_record_to_modify.html', tables=['employee', 'hourlyrate', 'revenuetype', ...])  # Add all table names here



@app.route('/modify_record', methods=['GET', 'POST'])
def modify_record():
    selected_table = request.args.get('table')
    primary_key_column = request.args.get('pk_col')
    primary_key_value = request.args.get('pk_val')

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Employee table
        if selected_table == 'employee':
            e_id = request.form.get('E_ID')
            #start_date = request.form.get('START_DATE')
            job_type = request.form.get('JOB_TYPE')
            mint = request.form.get('MINT')
            last = request.form.get('LAST')
            street = request.form.get('STREET')
            city = request.form.get('CITY')
            state = request.form.get('STATE')
            zip_code = request.form.get('ZIP')
            h_id = request.form.get('H_ID')
            first_name = request.form.get('FIRST_NAME')
            start_date_unformatted = request.form.get('start_date_unformatted')
            start_date = datetime.strptime(start_date_unformatted, "%Y-%m-%d")

            # Convert the start_date from string to a datetime object
            #start_date = datetime.strptime(start_date, "%Y-%m-%d")

            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Update query
            cursor.execute("""
                UPDATE employee
                SET START_DATE = :start_date, JOB_TYPE = :job_type, MINT = :mint, LAST = :last,
                    STREET = :street, CITY = :city, STATE = :state, ZIP = :zip, H_ID = :h_id, FIRST_NAME = :first_name
                WHERE E_ID = :e_id
                """, {
                    'start_date': start_date, 
                    'job_type': job_type, 
                    'mint': mint, 
                    'last': last, 
                    'street': street, 
                    'city': city, 
                    'state': state, 
                    'zip': zip_code, 
                    'h_id': h_id, 
                    'first_name': first_name, 
                    'e_id': e_id
                })
            #record = cursor.fetchone()
            conn.commit()
            #return redirect(url_for('modify_employee',  table=selected_table, pk_col=primary_key_column, pk_val=primary_key_value))

            # HourlyRate table
        elif selected_table == 'hourlyrate':
            # Process form data for hourlyrate table
            h_id = request.form.get('H_ID')
            rate = request.form.get('RATE')

            conn = get_db_connection()
            cursor = conn.cursor()

            # Update query
            cursor.execute("""
                UPDATE hourlyrate
                SET RATE = :rate
                WHERE H_ID = :h_id
                """, {
                    'rate': rate,
                    'h_id': h_id
                })

            conn.commit()

         # RevenueType table
        elif selected_table == 'revenuetype':
            # Process form data for revenuetype table
            rid = request.form.get('RID')
            name = request.form.get('NAME')
            type = request.form.get('TYPE')
            per_day = request.form.get('PER_DAY')
            adult_price = request.form.get('ADULT_PRICE')
            senior_price = request.form.get('SENIOR_PRICE')
            product = request.form.get('PRODUCT')
            b_id = request.form.get('B_ID')

            conn = get_db_connection()
            cursor = conn.cursor()

            # Update query
            cursor.execute("""
                UPDATE revenuetype
                SET NAME = :name, TYPE = :type, PER_DAY = :per_day, ADULT_PRICE = :adult_price,
                    SENIOR_PRICE = :senior_price, PRODUCT = :product, B_ID = :b_id
                WHERE RID = :rid
                """, {
                    'name': name,
                    'type': type,
                    'per_day': per_day,
                    'adult_price': adult_price,
                    'senior_price': senior_price,
                    'product': product,
                    'b_id': b_id,
                    'rid': rid
                })

            conn.commit()
        elif selected_table == 'animal':
            # Process form data for animal table
            a_id = request.form.get('A_ID')
            status = request.form.get('STATUS')
            birth_year = request.form.get('BIRTH_YEAR')
            s_id = request.form.get('S_ID')
            e_id = request.form.get('E_ID')
            b_id = request.form.get('B_ID')

            conn = get_db_connection()
            cursor = conn.cursor()

            # Update query
            cursor.execute("""
                UPDATE animal
                SET STATUS = :status, BIRTH_YEAR = :birth_year, S_ID = :s_id, E_ID = :e_id, B_ID = :b_id
                WHERE ANIMAL_ID = :animal_id
                """, {
                    'status': status,
                    'birth_year': birth_year,
                    's_id': s_id,
                    'e_id': e_id,
                    'b_id': b_id,
                    'animal_id': a_id
                })

            conn.commit()
            
        elif selected_table == 'animalcarespecialist':
            # Process form data for animalcarespecialist table
            e_id = request.form.get('E_ID')
            s_id = request.form.get('S_ID')

            conn = get_db_connection()
            cursor = conn.cursor()

            # Update query
            cursor.execute("""
                UPDATE animalcarespecialist
                SET E_ID = :e_id, S_ID = :s_id
                WHERE ID = :id
                """, {
                    'e_id': e_id,
                    's_id': s_id,
                })

            conn.commit()

        elif selected_table == 'caresfor':
            # Process form data for caresfor table
            e_id = request.form.get('E_ID')
            s_id = request.form.get('S_ID')

            conn = get_db_connection()
            cursor = conn.cursor()

            # Update query
            cursor.execute("""
                UPDATE caresfor
                SET E_ID = :e_id, S_ID = :s_id
                WHERE ID = :id
                """, {
                    'e_id': e_id,
                    's_id': s_id,
                })

            conn.commit()

        elif selected_table == 'building':
            # Process form data for building table
            b_id = request.form.get('B_ID')
            name = request.form.get('NAME')
            type = request.form.get('TYPE')

            conn = get_db_connection()
            cursor = conn.cursor()

            # Update query
            cursor.execute("""
                UPDATE building
                SET NAME = :name, TYPE = :type
                WHERE B_ID = :b_id
                """, {
                    'name': name,
                    'type': type,
                    'b_id': b_id
                })

            conn.commit()
        elif selected_table == 'enclosure':
            # Process form data for enclosure table
            en_id = request.form.get('EN_ID')
            sqft = request.form.get('SQFT')
            b_id = request.form.get('B_ID')

            conn = get_db_connection()
            cursor = conn.cursor()

            # Update query
            cursor.execute("""
                UPDATE enclosure
                SET SQFT = :sqft, B_ID = :b_id
                WHERE EN_ID = :en_id
                """, {
                    'sqft': sqft,
                    'b_id': b_id,
                    'en_id': en_id
                })

            conn.commit()
        elif selected_table == 'revenueevents':
            # Process form data for revenueevents table
            #r_date = request.form.get('R_DATE')
            revenue = request.form.get('REVENUE')
            tickets_sold = request.form.get('TICKETS_SOLD')
            s_id = request.form.get('S_ID')
            rid = request.form.get('RID')
            R_date_unformatted = request.form.get('R_DATE')
            R_DATE = datetime.strptime(R_date_unformatted, "%Y-%m-%d")

            conn = get_db_connection()
            cursor = conn.cursor()

            # Update query
            cursor.execute("""
                UPDATE revenueevents
                SET R_DATE = :R_DATE, REVENUE = :revenue, TICKETS_SOLD = :tickets_sold, S_ID = :s_id
                WHERE RID = :rid
                """, {
                    'r_date': R_DATE,
                    'revenue': revenue,
                    'tickets_sold': tickets_sold,
                    's_id': s_id,
                    'rid': rid
                })

            conn.commit()
        elif selected_table == 'revenuetype':
            # Process form data for revenuetype table
            rid = request.form.get('RID')
            name = request.form.get('NAME')
            type = request.form.get('TYPE')
            per_day = request.form.get('PER_DAY')
            adult_price = request.form.get('ADULT_PRICE')
            senior_price = request.form.get('SENIOR_PRICE')
            product = request.form.get('PRODUCT')
            b_id = request.form.get('B_ID')

            conn = get_db_connection()
            cursor = conn.cursor()

            # Update query
            cursor.execute("""
                UPDATE revenuetype
                SET NAME = :name, TYPE = :type, PER_DAY = :per_day, ADULT_PRICE = :adult_price, SENIOR_PRICE = :senior_price, PRODUCT = :product, B_ID = :b_id
                WHERE RID = :rid
                """, {
                    'name': name,
                    'type': type,
                    'per_day': per_day,
                    'adult_price': adult_price,
                    'senior_price': senior_price,
                    'product': product,
                    'b_id': b_id,
                    'rid': rid
                })

            conn.commit()
        elif selected_table == 'species':
            # Process form data for species table
            s_id = request.form.get('S_ID')
            name = request.form.get('NAME')
            average_food_cost = request.form.get('AVERAGE_FOOD_COST')

            conn = get_db_connection()
            cursor = conn.cursor()

            # Update query
            cursor.execute("""
                UPDATE species
                SET NAME = :name, AVERAGE_FOOD_COST = :average_food_cost
                WHERE S_ID = :s_id
                """, {
                    'name': name,
                    'average_food_cost': average_food_cost,
                    's_id': s_id
                })

            conn.commit()

        return render_template('modify_record.html', table=selected_table, pk_col=primary_key_column, pk_val=primary_key_value,)  
        #     # Process form data for revenuetype table
        #     pass    

        # # Other tables
        # # elif selected_table == 'another_table':
        #     # Process form data for another_table
        #     # pass

        # conn.commit()
        # return redirect(url_for('select_record_to_modify'))

    # Fetch the current record to pre-fill the form
    # cursor.execute(f"SELECT * FROM {selected_table} WHERE ID = :id", [record_id])
    # record = cursor.fetchone()
    
    conn.close()

    return render_template('modify_record.html', table=selected_table, pk_col=primary_key_column, pk_val=primary_key_value,)  

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selected_table = request.form.get('table')
        primary_key_column = request.form.get('primary_key_column')
        primary_key_value = request.form.get('primary_key_value')
        return redirect(url_for('view_record', 
                                table=selected_table, 
                                pk_col=primary_key_column, 
                                pk_val=primary_key_value))

    return render_template('home.html', tables=['employee', 'hourlyrate', 'revenuetype', 'animal', 'building', 'animalcarespecialist', 'species', 'caresfor', 'enclosure', 'revenueevents', 'veterinarian'])  # Add all table names here

@app.route('/select_record_page', methods=['GET', 'POST'])
def select_record_page():
    if request.method == 'POST':
        selected_table = request.form.get('table')
        primary_key_column = request.form.get('primary_key_column')
        primary_key_value = request.form.get('primary_key_value')
        return redirect(url_for('view_record', 
                                table=selected_table, 
                                pk_col=primary_key_column, 
                                pk_val=primary_key_value))

    return render_template('select_record_page.html', tables=['employee', 'hourlyrate', 'revenuetype', 'animal', 'building', 'animalcarespecialist', 'species', 'caresfor', 'enclosure', 'revenueevents', 'veterinarian'])  # Add all table names here

@app.route('/view_record')
def view_record():
    selected_table = request.args.get('table')
    primary_key_column = request.args.get('pk_col')
    primary_key_value = request.args.get('pk_val')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {selected_table} WHERE {primary_key_column} = :pk_val", [primary_key_value])
    record = cursor.fetchone()
    conn.close()

    return render_template('view_record.html', record=record, table=selected_table)

@app.route('/daily_revenue_report', methods=['GET', 'POST'])
def daily_revenue_report():
    if request.method == 'POST':
        date = request.form['date']
        #date_formatted = date.strftime("%Y-%m-%d")
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # SQL Query to fetch revenue by source for the given day
        query = """
        SELECT 
            rt.Name AS RevenueSource,
            SUM(re.Revenue) AS TotalRevenue,
            re.R_Date
        FROM 
            RevenueEvents re
        JOIN 
            RevenueType rt ON re.RID = rt.RID
        WHERE 
            TRUNC(re.R_Date) = TO_DATE(:selected_date, 'YYYY-MM-DD')
        GROUP BY 
            rt.Name, re.R_Date
        ORDER BY 
            rt.Name
        """
        cursor.execute(query, {'selected_date': date})
        revenue_data = cursor.fetchall()
        conn.close()

        return render_template('daily_revenue_report.html', revenue_data=revenue_data, date=date)

    return render_template('daily_revenue_report_form.html')

@app.route('/animal_population_report')
def animal_population_report():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Conceptual SQL Query (this is a simplified version and needs to be tailored to your specific database schema and requirements)
    query = """
    SELECT 
        sp.NAME AS SpeciesName, 
        an.STATUS, 
        COUNT(an.A_ID) AS TotalAnimals, 
        SUM(sp.AVERAGE_FOOD_COST) AS TotalFoodCost,
        SUM(hr.RATE * 40 * 4) AS TotalCareCost  -- Assuming 40 hours per week, 4 weeks per month
    FROM 
        Animal an
    JOIN 
        Species sp ON an.S_ID = sp.S_ID
    LEFT JOIN 
        ANIMALCARESPECIALIST acs ON an.E_ID = acs.E_ID
    LEFT JOIN 
        VETERINARIAN vet ON an.E_ID = vet.E_ID
    LEFT JOIN 
        Employee emp ON (acs.E_ID = emp.E_ID OR vet.E_ID = emp.E_ID)
    LEFT JOIN 
        HOURLYRATE hr ON emp.H_ID = hr.H_ID
    GROUP BY 
        sp.NAME, an.STATUS
    """
    cursor.execute(query)
    report_data = cursor.fetchall()
    conn.close()

    return render_template('animal_population_report.html', report_data=report_data)

@app.route('/top_attractions', methods=['GET', 'POST'])
def top_attractions():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        conn = get_db_connection()
        cursor = conn.cursor()

        # Your provided SQL query with placeholders for the dates
        query = """
        SELECT 
            rt.RID, SUM(re.Revenue) AS TotalRevenue
        FROM 
            revenuetype rt
        JOIN 
            Revenueevents re ON rt.RID = re.RID
        WHERE 
            re.R_Date BETWEEN TO_DATE(:start_date, 'YYYY-MM-DD') AND TO_DATE(:end_date, 'YYYY-MM-DD')
        GROUP BY 
            rt.RID
        ORDER BY 
            TotalRevenue DESC
        FETCH FIRST 3 ROWS ONLY
        """
        cursor.execute(query, {'start_date': start_date, 'end_date': end_date})
        top_attractions_data = cursor.fetchall()
        conn.close()

        return render_template('top_attractions_report.html', top_attractions_data=top_attractions_data, start_date=start_date, end_date=end_date)

    return render_template('top_attractions.html')

@app.route('/best_revenue_days', methods=['GET', 'POST'])
def best_revenue_days():
    if request.method == 'POST':
        month = request.form['month']
        year = request.form['year']
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL Query to fetch top 5 revenue days for the given month
        query = """
        SELECT 
            TRUNC(re.R_DATE, 'DD') AS Day,
            SUM(re.REVENUE) AS TotalRevenue
        FROM 
            RevenueEvents re
        WHERE 
            TO_CHAR(re.R_DATE, 'YYYY-MM') = :selected_month
        GROUP BY 
            TRUNC(re.R_DATE, 'DD')
        ORDER BY 
            TotalRevenue DESC
        FETCH FIRST 5 ROWS ONLY
        """
        selected_month = f'{year}-{month}'  # Format the month and year into 'YYYY-MM'
        cursor.execute(query, {'selected_month': selected_month})
        best_days_data = cursor.fetchall()
        conn.close()

        return render_template('best_revenue_days_report.html', best_days_data=best_days_data, month=month, year=year)

    return render_template('best_revenue_days.html')

@app.route('/average_revenue', methods=['GET', 'POST'])
def average_revenue():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL Query to compute average revenue
        query = """
        SELECT 
            b.NAME AS AttractionName, 
            b.TYPE AS AttractionType, 
            AVG(re.REVENUE) AS AverageRevenue,
            SUM(re.TICKETS_SOLD) AS TotalAttendance
        FROM 
            RevenueEvents re
        JOIN 
            RevenueType rt ON re.RID = rt.RID
        JOIN 
            Building b ON rt.B_ID = b.B_ID
        WHERE 
            re.R_DATE BETWEEN TO_DATE(:start_date, 'YYYY-MM-DD') AND TO_DATE(:end_date, 'YYYY-MM-DD')
        GROUP BY 
            b.NAME, b.TYPE
        """
        cursor.execute(query, {'start_date': start_date, 'end_date': end_date})
        revenue_data = cursor.fetchall()
        conn.close()

        return render_template('average_revenue_report.html', revenue_data=revenue_data, start_date=start_date, end_date=end_date)

    return render_template('average_revenue.html')




if __name__ == '__main__':
    app.run(debug=True)

