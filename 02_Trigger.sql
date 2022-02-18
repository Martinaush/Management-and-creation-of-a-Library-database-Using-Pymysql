CREATE DEFINER=`root`@`localhost` TRIGGER `orderlist_AFTER_DELETE` AFTER DELETE ON `orderlist` FOR EACH ROW BEGIN
	
    # This trigger will update the quantity of the books once the books have been returned by the user
    
    IF OLD.fulfilled = 1 THEN 
    
		UPDATE stocklist SET quantityinstock = OLD.quantity + quantityinstock WHERE OLD.bookid = stocklist.bookid;
    
    END IF;
END