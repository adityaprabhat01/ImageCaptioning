import numpy as np

def beam_search(pred, k) :
    top_three_indexes, next_char_indices, probabilities, indexes, temp_i, temp_p  = [], [], [], [], [], []
    top_three = -np.array(sorted(-np.array(pred))[:3])
    
    for w in top_three :
        top_three_indexes.append(np.where(pred == w)[0][0])
        
    for i in range(k) :
        temp_p = pred[top_three_indexes[i]] * (-np.log(pred))
        top_three_temp = -np.array(sorted(-np.array(temp_p)))[:3]
        for w in top_three_temp :
            temp_i.append(np.where(temp_p == w)[0][0])
        indexes.append(temp_i)
        probabilities.append(top_three_temp)
        temp_i = []
        temp_p = []
    
    flatten_index = np.array(indexes).flatten()
    flatten_probabilities = np.array(probabilities).flatten()
    top = -np.array(sorted(-np.array(flatten_probabilities)))[:3]
    
    for w in top :
        for i in range(len(flatten_probabilities)) :
            if(w == flatten_probabilities[i]) :
                next_char_indices.append(flatten_index[i])
    return next_char_indices