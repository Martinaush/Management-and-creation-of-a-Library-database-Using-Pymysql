CREATE DEFINER=`root`@`localhost` TRIGGER `orderlist_BEFORE_UPDATE` BEFORE UPDATE ON `orderlist` FOR EACH ROW BEGIN

	DECLARE quantit INT;
    
    SELECT quantityinstock INTO quantit FROM stocklist WHERE bookid = NEW.bookid;
    
    IF NEW.quantity > quantit THEN
		
        SET NEW.fulfilled = 0;
        
        UPDATE stocklist SET quantityinstock = quantityinstock + NEW.quantity WHERE bookid = NEW.bookid;
        
        INSERT INTO backorderlist (orderid, quantity) VALUES (NEW.orderid, NEW.quantity);
		
    
    END IF;
END