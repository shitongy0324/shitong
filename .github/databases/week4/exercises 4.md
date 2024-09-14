## question 1
```sql
select country.name as "country name", airport.name as "airport name"
from country inner join airport on airport.iso_country = country.iso_country
where country.name = "Finland" and scheduled_service = "yes";
```
![img.png](img.png)
## question 2
```sql
select game.screen_name,airport.name
from game  inner join airport on airport.ident=game.location;
```
![img_1.png](img_1.png)
## question 3
```sql
select game.screen_name , country.name
from airport inner join game on game.location=airport.ident
inner join country on airport.iso_country = country.iso_country;
```
![img_2.png](img_2.png)
## question4
```sql
select airport.name , game.screen_name
from airport
left join game on airport.ident = game.location
where airport.name like '%Hels%'
order by screen_name desc;
```
![img_3.png](img_3.png)
## question 5
```sql
select goal.name , game.screen_name
from goal
left join goal_reached on goal.id = goal_reached.goal_id
left join game on goal_reached.game_id = game.id;
```
![img_4.png](img_4.png)