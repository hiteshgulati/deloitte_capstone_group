--1.	Generate Info of the cars which is of the type first owner and the year of car purchase is between 2016-2020 and the number of kms driven is less than 80,000
Select * from car_sales_transactions where owner = 'First Owner' and Year >2016 and Year <2020 and km_driven < 80000;

--2.	Generate Info of all the cars  whose average mileage is around 25 kmpl and year of car purchase is between 2018-2020 which has minimum seating of 4-5 and fuel type is diesel.
Select * from car_sales_transactions where mileage >'24 kmpl' and mileage<'25 kmpl' and Year >2018 and Year <2020 and seats < 6 and seats >3 and Fuel = 'Diesel';

--3.	Generate Info of all the cars which are not sold, and seller-type is individual or dealer and also which has been used for less than 60000 kms and year of car purchase is 2014-2020