create database hotel_rev_insights_db;

use hotel_rev_insights_db;


select *from dim_date;

ALTER TABLE dim_date
RENAME COLUMN `mmm yy` TO mmm_yy,
RENAME COLUMN `week no` TO week_no;

ALTER TABLE dim_date
MODIFY COLUMN date date,
modify column mmm_yy varchar(20),
MODIFY COLUMN week_no varchar(15),
MODIFY COLUMN day_type varchar(20);

alter table dim_date
add primary key(date);




select *from dim_hotels;

alter table dim_hotels
modify column property_id int,
modify column property_name varchar(50),
modify column category varchar(30),
modify column city varchar(50);

alter table dim_hotels
add primary key(property_id);


select *from dim_rooms;

alter table dim_rooms
modify column room_id varchar(20),
modify column room_class varchar(30);


alter table dim_rooms
add primary key(room_id);

select *from fact_aggregated_bookings;

alter table fact_aggregated_bookings
modify column property_id int,
modify column check_in_date date,
modify column room_category varchar(20),
modify column successful_bookings int,
modify column capacity int;

alter table fact_aggregated_bookings
add constraint fk_fact_aggregated_bookings_property_id
foreign key(property_id) references dim_hotels(property_id);




alter table fact_aggregated_bookings
modify property_id int,
modify check_in_date date,
modify room_category varchar(255),
modify successful_bookings int,
modify capacity int;


alter table fact_aggregated_bookings
add constraint fk_fact_aggregated_bookings_room_id
foreign key(room_category) references dim_rooms(room_id);


alter table fact_aggregated_bookings
add constraint fk_fact_aggregated_bookings_check_in_date
foreign key(check_in_date) references dim_date(date);


select *from fact_bookings;

alter table fact_bookings
modify column booking_id varchar(30),
modify column property_id int,
modify column  booking_date date,
modify column check_in_date date,
modify column checkout_date date,
modify column no_guests int,
modify column room_category varchar(50),
modify column booking_platform varchar(60),
modify column  ratings_given int,
modify column  booking_status varchar(60),
modify column  revenue_generated float,
modify column  revenue_realized float;



alter table fact_bookings
add constraint fk_fact_bookings_property_id
foreign key(property_id) references dim_hotels(property_id);

alter table fact_bookings
add constraint fk_fact_bookings_room_id
foreign key(room_category) references dim_rooms(room_id);

alter table fact_bookings
add constraint fk_fact_bookings_check_in_date
foreign key(check_in_date) references dim_date(date);



SELECT DISTINCT room_category
FROM fact_bookings;




