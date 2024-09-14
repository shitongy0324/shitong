# Exercises 3
## question 1
```sql
select * from goal;
```
![img_1.png](question1.png)
## question 2
```sql
select name from airport where iso_country = "FI";
```
![img_2.png](question2.png)
## question 3
```sql
 select name from airport where iso_country = "FI" order by name;
```
![img_3.png](question3.png)
## question 4
```sql
select name,type from airport where iso_country = "FI" order by type,name;
```
![img_4.png](question4.png)
## question 5
```sql
select name from country where name like 'F%';
```
![img.png](w3%20question5.png)
## question 6
```sql
select name from country where name like "%F%";
```
![img.png](question%206.png)
## question 7
```sql
select location from game where screen_name  = "Vesa"
```
![img.png](question%207.png)
## question 8
```sql
select co2_consumed from game where screen_name ="Ilkka";
```
![img.png](question%208.png)
## question 9
```sql
select distinct co2_budget from game;
```
![img.png](img.png)
## question 10
```sql
select screen_name ,co2_budget , co2_consumed,(@c02_left:=co2_budget - co2_consumed) as co2_left from game
where screen_name = "Ilkka";
```
![img_1.png](img_1.png)