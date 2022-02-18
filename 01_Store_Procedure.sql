CREATE DEFINER=`root`@`localhost` PROCEDURE `waiting_list`(
	IN numberbook INT,
    OUT PEOPLE INT
)
BEGIN

	DECLARE availability INT;
    
	DECLARE done TINYINT DEFAULT FALSE;
    
    # Auxiliary variables to do the loop
    
    DECLARE ordernumber INT;
    
    DECLARE booknumber INT;
    
    DECLARE totalbooks INT;
    
    DECLARE indicator INT;
    
    DECLARE cursor1 CURSOR FOR SELECT orderid, bookid, quantity, fulfilled FROM orderlist;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    SELECT quantityinstock INTO availability FROM stocklist WHERE stocklist.bookid = numberbook;
    
	# Looping all over backorderlist to choose the next one if any waiting for the book
    
    OPEN cursor1;
    
    updateloop:LOOP
    
		FETCH NEXT FROM cursor1 INTO ordernumber, booknumber, totalbooks, indicator;
    
		IF done THEN
        
			LEAVE updateloop;
            
		ELSE
        
            IF booknumber = numberbook THEN 
            
				IF indicator = 0 AND totalbooks <= availability THEN
					
					UPDATE stocklist SET quantityinstock = quantityinstock - totalbooks WHERE stocklist.bookid = numberbook;
						
					UPDATE orderlist SET fulfilled = 1 WHERE orderlist.orderid = ordernumber;
						
					DELETE FROM backorderlist WHERE backorderlist.orderid = ordernumber;
                    
                    SET PEOPLE = PEOPLE + 1;
                    
				END IF;
                
			END IF;

		END IF;
        
	END LOOP;
        
    
    
    
    
END