#  Creation of 3 indexes, one for each table

CREATE INDEX index1 on stocklist(bookid);

CREATE INDEX index2 on orderlist(orderid);

CREATE INDEX index3 on backorderlist(backorderid);