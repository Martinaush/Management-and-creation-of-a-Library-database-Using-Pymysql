CREATE DEFINER=`root`@`localhost` TRIGGER `orderlist_BEFORE_INSERT` BEFORE INSERT ON `orderlist` FOR EACH ROW BEGIN
	# We declare here two variables of interest
	DECLARE bookcopies INT;
	DECLARE ordnumber INT;
	# We store the value of the first variable
	# We store bookcopies from the same book the user has chosen
	SELECT quantityinstock INTO bookcopies
	FROM stocklist WHERE NEW.bookid = stocklist.bookid;
	# We store the orderid matching with the user's orderid
	SELECT IFNULL(max(orderid), 0)+1 INTO ordnumber FROM orderlist;
	# We create an if to check if there is disponibility for these books they requested
	IF NEW.quantity <= bookcopies THEN
		SET NEW.fulfilled = 1;
		UPDATE stocklist SET quantityinstock = bookcopies - NEW.quantity
		WHERE stocklist.bookid = NEW.bookid;
	ELSE
		INSERT INTO backorderlist (orderid, quantity) VALUES 
		(ordnumber, NEW.quantity);
		SET NEW.fulfilled = 0;
	END IF;
END