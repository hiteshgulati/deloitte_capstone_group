
from flask import Flask, render_template, request
import pickle
import pandas as pd
app = Flask(__name__,static_url_path='/static')

@app.route('/test')
def testroute():
    return "Hello World"

@app.route('/')
def index():
    return render_template("Welcome.html")

@app.route('/buycar', methods = ["GET","POST"])
def buycar():
    return render_template("buycar.html")

@app.route('/priceofcar', methods = ["GET","POST"])
def priceofcar():
    Data = pd.DataFrame(columns = ['Year', 'km_Driven', 'Seats', 'Mileage_float', 'Power',
       'Engine_cc', 'Fuel_Diesel', 'Fuel_LPG', 'Fuel_Petrol',
       'Seller_Type_Individual', 'Seller_Type_Trustmark Dealer',
       'Transmission_Manual', 'Owner_Fourth & Above Owner',
       'Owner_Second Owner', 'Owner_Test Drive Car', 'Owner_Third Owner',
       'City_Name_Aurangabad', 'City_Name_Bangalore', 'City_Name_Bhubaneshwar',
       'City_Name_Chennai', 'City_Name_Coimbatore', 'City_Name_Dehradun',
       'City_Name_Delhi', 'City_Name_Gangtok', 'City_Name_Hyderabad',
       'City_Name_Indore', 'City_Name_Jaipur', 'City_Name_Jamshedpur',
       'City_Name_Kochi', 'City_Name_Kolkata', 'City_Name_Ludhiana',
       'City_Name_Mangalore', 'City_Name_Mumbai', 'City_Name_Mysore',
       'City_Name_Nellore', 'City_Name_Noida', 'City_Name_Patna',
       'City_Name_Pune', 'City_Name_Ranchi', 'City_Name_Surat',
       'City_Name_Thrissur', 'City_Name_Vadodara', 'City_Name_Vellore',
       'City_Name_kanpur', 'Sold_Y', 'Brand_Ashok', 'Brand_Audi', 'Brand_BMW',
       'Brand_Chevrolet', 'Brand_Daewoo', 'Brand_Datsun', 'Brand_Fiat',
       'Brand_Force', 'Brand_Ford', 'Brand_Honda', 'Brand_Hyundai',
       'Brand_Isuzu', 'Brand_Jaguar', 'Brand_Jeep', 'Brand_Kia', 'Brand_Land',
       'Brand_Lexus', 'Brand_MG', 'Brand_Mahindra', 'Brand_Maruti',
       'Brand_Mercedes-Benz', 'Brand_Mitsubishi', 'Brand_Nissan', 'Brand_Opel',
       'Brand_Renault', 'Brand_Skoda', 'Brand_Tata', 'Brand_Toyota',
       'Brand_Volkswagen', 'Brand_Volvo'])
    Data.loc[len(Data.index)] = 0 
    Data.at[0,'Year'] = 2022
    Data.at[0,'km_Driven'] = request.form.get('kmDriven')
    Data.at[0,'Seats'] = request.form.get('seats')
    Data.at[0,'Mileage_float'] = request.form.get('mileage')
    Data.at[0,'Power']= request.form.get('power')
    Data.at[0,'Engine_cc'] = request.form.get('engine')
    if request.form.get('brand') != "Ambassador":
        brandstr = "Brand_" + request.form.get('brand')
        Data.at[0,brandstr]= 1
    if request.form.get('city') != "Ahmedabad":
        city_name = "City_Name_" + request.form.get('city')
        Data.at[0,city_name] = 1
    if request.form.get('fuel') != "CNG":
        fuel_type = "Fuel_" + request.form.get('fuel')
        Data.at[0,fuel_type] = 1
    if request.form.get('transmission') != "Automatic":
        transmission = "Transmission_" + request.form.get('transmission')
        Data.at[0,transmission] = 1
    if request.form.get('sellertype') != "Dealer":
        sellertype = "Seller_Type_" + request.form.get('sellertype')
        Data.at[0,sellertype] = 1
    if request.form.get('owner') != "First Owner":
        owner = "Owner_" + request.form.get('owner')
        Data.at[0,owner] = 1
    # print(Data.columns)
    with open('randommodel.pkl' , 'rb') as f:
        pred= pickle.load(f)
    # pred = pickle.load(open('randommodel.pkl','rb'))
    outcome = pred.predict(X=Data)
    print(outcome[0])
    # print("%%%%%")
    return render_template("price.html", price=round(outcome[0]))

if __name__ == "__main__":
    app.run(debug=True, port= 8000)