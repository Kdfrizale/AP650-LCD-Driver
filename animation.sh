#! /bin/bash
#Simple Example to have a rolling text display


COUNTER = 5
until [ $COUNTER -lt 10 ]; do

	python lcd_parse.py 1 helloo
	sleep .23
	python lcd_parse.py 1 ohello
	sleep .23
	python lcd_parse.py 1 oohell
	sleep .23
	python lcd_parse.py 1 loohel
	sleep .23
	python lcd_parse.py 1 lloohe
	sleep .23
	python lcd_parse.py 1 ellooh
	sleep .23
	python lcd_parse.py 1 helloo
	let  $COUNTER = $COUNTER -1
done
