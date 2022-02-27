# Write your MySQL query statement below
select p.firstName, p.lastName, ad.city, ad.state 
from Person as p left join Address as ad ON p.personId = ad.personId
