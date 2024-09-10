-- Lab 11.2 https://docs.google.com/document/d/1MwGskOyAAa0tESULbTVfMc8iUbpVrHzj/edit

set @transaction_value = 2;
select * from sales where transaction_value > @transaction_value;
