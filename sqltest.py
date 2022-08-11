show
databases
create
database
ineuron
use
ineuron
create
table if not exists
bank_detail2(
    age
int,
job
varchar(30),
marital
varchar(30),
education
varchar(30),
`default`
varchar(30),
balance
varchar(30),
housing
varchar(30),
loan
varchar(30),
contact
varchar(30),
`day`
int,
`month`
varchar(30),
duration
int,
campaign
int,
pdays
int,
previous
varchar(30),
poutcome
varchar(30),
y
varchar(30))

show
tables
describe
bank_detail
insert in to
bank_detail
values(58, "management", "married", "tertiary", "no", 2143, "yes", "no", "unknown", 5, "may", 261, 1, -1, 0, "unknown",
       "no")
ALTER
TABLE
bank_detail
MODIFY
previous
int
describe
bank_detail
insert
into
bank_detail
values(58, "management", "married", "tertiary", "no", 2143, "yes", "no", "unknown", 5, "may", 261, 1, -1, 0, "unknown",
       "no")
select *
from bank_detail

insert
into
bank_detail
values(44, "technician", "single", "secondary", "no", 29, "yes", "no", "unknown", 5, "may", 151, 1, -1, 0, "unknown",
       "no")

insert
into
bank_detail
values(33, "entrepreneur", "married", "secondary", "no", 2, "yes", "yes", "unknown", 5, "may", 76, 1, -1, 0, "unknown",
       "no"),
(47, "blue-collar", "married", "unknown", "no", 1506, "yes", "no", "unknown", 5, "may", 92, 1, -1, 0, "unknown", "no"),
(33, "unknown", "single", "unknown", "no", 1, "no", "no", "unknown", 5, "may", 198, 1, -1, 0, "unknown", "no"),
(35, "management", "married", "tertiary", "no", 231, "yes", "no", "unknown", 5, "may", 139, 1, -1, 0, "unknown", "no"),
(28, "management", "single", "tertiary", "no", 447, "yes", "yes", "unknown", 5, "may", 217, 1, -1, 0, "unknown", "no"),
(
42, "entrepreneur", "divorced", "tertiary", "yes", 2, "yes", "no", "unknown", 5, "may", 380, 1, -1, 0, "unknown", "no"),
(58, "retired", "married", "primary", "no", 121, "yes", "no", "unknown", 5, "may", 50, 1, -1, 0, "unknown", "no"),
(43, "technician", "single", "secondary", "no", 593, "yes", "no", "unknown", 5, "may", 55, 1, -1, 0, "unknown", "no"),
(41, "admin.", "divorced", "secondary", "no", 270, "yes", "no", "unknown", 5, "may", 222, 1, -1, 0, "unknown", "no"),
(29, "admin.", "single", "secondary", "no", 390, "yes", "no", "unknown", 5, "may", 137, 1, -1, 0, "unknown", "no"),
(53, "technician", "married", "secondary", "no", 6, "yes", "no", "unknown", 5, "may", 517, 1, -1, 0, "unknown", "no"),
(58, "technician", "married", "unknown", "no", 71, "yes", "no", "unknown", 5, "may", 71, 1, -1, 0, "unknown", "no"),
(57, "services", "married", "secondary", "no", 162, "yes", "no", "unknown", 5, "may", 174, 1, -1, 0, "unknown", "no"),
(51, "retired", "married", "primary", "no", 229, "yes", "no", "unknown", 5, "may", 353, 1, -1, 0, "unknown", "no"),
(45, "admin.", "single", "unknown", "no", 13, "yes", "no", "unknown", 5, "may", 98, 1, -1, 0, "unknown", "no"),
(57, "blue-collar", "married", "primary", "no", 52, "yes", "no", "unknown", 5, "may", 38, 1, -1, 0, "unknown", "no"),
(60, "retired", "married", "primary", "no", 60, "yes", "no", "unknown", 5, "may", 219, 1, -1, 0, "unknown", "no"),
(33, "services", "married", "secondary", "no", 0, "yes", "no", "unknown", 5, "may", 54, 1, -1, 0, "unknown", "no"),
(28, "blue-collar", "married", "secondary", "no", 723, "yes", "yes", "unknown", 5, "may", 262, 1, -1, 0, "unknown",
 "no"),
(56, "management", "married", "tertiary", "no", 779, "yes", "no", "unknown", 5, "may", 164, 1, -1, 0, "unknown", "no"),
(32, "blue-collar", "single", "primary", "no", 23, "yes", "yes", "unknown", 5, "may", 160, 1, -1, 0, "unknown", "no"),
(25, "services", "married", "secondary", "no", 50, "yes", "no", "unknown", 5, "may", 342, 1, -1, 0, "unknown", "no"),
(40, "retired", "married", "primary", "no", 0, "yes", "yes", "unknown", 5, "may", 181, 1, -1, 0, "unknown", "no"),
(44, "admin.", "married", "secondary", "no", -372, "yes", "no", "unknown", 5, "may", 172, 1, -1, 0, "unknown", "no"),
(39, "management", "single", "tertiary", "no", 255, "yes", "no", "unknown", 5, "may", 296, 1, -1, 0, "unknown", "no")
select
age, job
from bank_detail

select *
from bank_detail where

age = 41
select
job, `default`
from bank_detail where

age = 41
select *
from bank_detail where

job = "retired" and balance > 100
select *
from bank_detail where

education = "primary" or balance < 100
select *
from bank_detail where

education = "primary" and balance < 100
select
distinct
job
from bank_detail

select *
from bank_detail order

by
age
select *
from bank_detail order

by
age
desc
select
count(*)
from bank_detail

select
sum(balance)
from

select
min(balance)
from bank_detail

select *
from bank_detail where

balance = (select min(balance)
from bank_detail)
select
marital, count(*)
from bank_detail group

by
marital
select *
from ineuron

use
ineuron
delimiter & &
create
procedure
sel_new_filters( in job1
varchar(30), in bal
int)
begin
select *
from bank_detail where

job = job1 and balance > bal;
end & &
use
db2
delimiter & &
create
procedure
sel_new_filters( in job1
varchar(30), in bal
int)
begin
select *
from bank_detail where

job = job1 and balance > bal;
end & &
call
sel_new_filters('retired', 100)
delimiter & &
create
procedure
sel_new_filters( in job1
varchar(30), in bal
int)
begin
select *
from bank_detail where

job = job1 and balance > bal;
end & &
use
inuron_courses
delimiter & &
create
pdelimiter & &
create
procedure
sel_new()
begin
select *
from employe

end & &
begin
select *
from bank_detail where

job = job1 and balance > bal;
end & &
delimiter & &
create
procedure
sel_new()
begin
select *
from employe;

end & &
call
sel_new()
use
ineuron
insert
into
bank_detailnew
select *
from bank_detailnew

alter
bank_detailnew
set
varchar
where
'default' = int
ALTER
TABLE
bank_detailnew
MODIFY
`month`
varchar(30)
insert
into
bank_detailnew
select *
from bank_detail

select *
from bank_detailnew

select
age, job, marital
from bank_detail inner

join
on
bank_detailnew
age = age
select
bank_detail.age, bank_detail.job, bank_detail.marital
from bank_detail inner

join
bank_detail2
on
bank_detail.age = bank_detail2.age
select
bank_detail.age, bank_detail.job, bank_detail.marital
from bank_detail left

join
bank_detail2
on
bank_detail.age = bank_detail2.age

select *
from bank_detail2

insert
into
bank_detail2
select *
from bank_detail where

age = 58
drop
database
db2