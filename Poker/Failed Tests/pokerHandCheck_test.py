#Writer: Abraham Ludlam
#Function: This file tests to make sure that eval5 and eval7 do not return a score if given an invalid hand. As both evaluation functions lack this functionality, this test will fail. If further development is done, both eval functions would need to implement some sort of invalid hand rejection functionality.  
#Version: Uses Pytest 3.10.1

from poker import *

#This test is to make sure two pairs beats as single pair. Here, pairs of 2's and 3's beats a pair of Aces
def test_eval7SameCard():
	player1 = ('2s', '2s', 'Tc', '3d', '2h', '7h', '8d' )
	assert eval7(player1) == '', "No score should be given for a hand with 2 or more of the same card"

#This test is to make sure a three of a kind beats a hand with 2 pairs. Here three 5's beats two pairs of 2's and 3's
def test_eval5SameCard():
	player1 = ('2s', '2s', 'Tc', '3d', '2h')
	assert eval5(player1) == '', "No score should be given for a hand with 2 or more of the same card"

