## question 1
```sql
update game
set  location = (select ident from airport where name = "Nottingham Airport"), co2_consumed = co2_consumed+500
where screen_name = "Vesa";

select * from game;
```
![img_10.png](img_10.png)