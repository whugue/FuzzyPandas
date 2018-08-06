import sys
import utils
import pandas as pd
from fuzzywuzzy import fuzz
from multiprocessing import Pool


class Scorer:

	def __init__:
        self.score_cache = {}  # not sure if this is right way to do caching...

	def score_pair(self, row, keys, method):
	    '''
	    Score a pair of values based on given scoring function
	    '''
	    result = {}
	    sum_scores = 0

	    for i, key in enumerate(keys, start=1):

	        value1 = utils.convert_to_string(row[0][key])
	        value2 = utils.convert_to_string(row[1][key])

	        value_pair = tuple(sorted([value1, value2]))

	        if value_pair in self.score_cache:
	        	score = self.score_cache[value_pair]
	        else:
	        	score = method(value1, value2)
	        	self.score_cache[value_pair]

	        sum_scores += score
	        avg_score = sum_scores / i

            result['{col}_A'.format(col=key)] = row[key]
            result['{col}_B'.format(col=key)] = match_row[key]
            result['{col}_match_score'.format(col=key)] = score 
        
        result['match_score'] = avg_score

        return result


    def score(self, data1, data2, keys, method, processes):

        data = utils.cartesian_product(data1, data2)
    
        if processes:
            if processes > 1:
                pool = Pool(processes)
                results = [pool.apply(self.score_pair, args=(row, keys, method)) for row in data]

            else:
                results = [self.score_pair(row, keys, method) for row in data]
                
        else:
            results = [self.score_pair(row, keys, method) for row in data]

        return results