## question 1
```sql
SELECT name 
FROM airport inner join country on airport.iso_country=country.iso_country
where airport.name like "Satsuma%";
```
![img_6.png](img_6.png)
## question 2
```sql
select name from airport
where iso_country in (
    select iso_country
    from country
    where name = "Monaco"
    );
```
![img_5.png](img_5.png)
## question 3
```sql
SELECT game.screen_name
from game
where id in (
    select goal_reached.game_id
    from goal_reached
    where goal_reached.goal_id in (
        select id
        from goal
        where name = "CLOUDS"
        )
    );
```
![img_7.png](img_7.png)
## question 4  
```sql
SELECT name
from country
where iso_country not in (
    select iso_country from airport
    );
```
![img_9.png](img_9.png)
## question 5  
```sql
SELECT name
from goal
where id not in (
    select goal_id from goal_reached
    );
```
![img_8.png](img_8.png)