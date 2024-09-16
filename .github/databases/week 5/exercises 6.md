## question 1
```sql
SELECT max(airport.elevation_ft) as "max(elevation_ft)"
from airport;
```
![img.png](img.png)
## question 2  
```sql
SELECT continent,count(iso_country)
from country
group by continent;
```
![img_1.png](img_1.png)
## question 3
```sql
select screen_name, count(*)
from game, goal_reached
where id = game_id
group by screen_name;
```
![img_2.png](img_2.png)
## question 4
```sql
select screen_name
from game
where co2_consumed in(
select min(co2_consumed)
from game
);
```
![img_3.png](img_3.png)
## question 5
```sql
select country.name ,count(*)
from country,airport
where airport.iso_country=country.iso_country
group by airport.iso_country
order by count(*) desc
limit 50;
```
![img_4.png](img_4.png)
## question 6
```sql
select country.name
from country,airport
where airport.iso_country=country.iso_country
group by airport.iso_country
having count(*)>1000;
```
![img_5.png](img_5.png)
## question 7  
```sql
select name
from airport
where elevation_ft=(select max(elevation_ft) from airport);
```
![img_6.png](img_6.png)
## question 8
```sql
select country.name
from airport,country
where elevation_ft=(select max(elevation_ft) from airport)and airport.iso_country=country.iso_country;
```
![img_7.png](img_7.png)
## question 9
```sql
select count(*)
from game, goal_reached
where id = game_id and screen_name="Vesa"
group by screen_name;
```
![img_8.png](img_8.png)
## question 10
```sql
select name
from airport
where latitude_deg in(
select min(latitude_deg)
from airport
);
```
![img_9.png](img_9.png)