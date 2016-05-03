import time
# import StringIO

start_time = time.time()

# import network class from Network.py

from clustergrammer import Network
net = Network()

net.load_file('txt/rc_two_cats.txt')
# net.load_file('txt/missing_values.txt')
# net.load_file('txt/example_tsv.txt')
# net.load_file('txt/col_categories.txt')
# net.load_file('txt/mat_cats.tsv')
# net.load_file('txt/mat_1mb.txt')
# net.load_file('txt/mnist.txt')
# net.load_file('txt/sim_mat_4_cats.txt')
# net.load_file('txt/number_names.txt')

# # filtering rows and cols by sum 
# net.filter_sum('row', threshold=20)
# net.filter_sum('col', threshold=30)

# # quantile normalize to normalize cell lines
# net.normalize(axis='row', norm_type='qn')


# # take zscore
# net.normalize(axis='col', norm_type='zscore', keep_orig=True)

# # only keep most differentially expressed genes
net.filter_N_top('row', 200, rank_type='var')
# net.filter_N_top('col', 100, rank_type='var ')

# filter for rows that contain num_occur values above threshold (abs value)
# net.filter_threShold('col', threshold=2, num_occur=3)
# net.filter_threshold('row', threshold=100, num_occur=200)

# net.swap_nan_for_zero()
  
views = ['N_row_sum', 'N_row_var']

net.make_clust(dist_type='cos',views=views , dendro=True,
               sim_mat=True, filter_sim=0.1, calc_cat_pval=True)

# net.produce_view({'N_row_sum':10,'dist':'euclidean'})

net.write_json_to_file('viz', 'json/mult_view.json', 'no-indent')
net.write_json_to_file('sim_row', 'json/mult_view_sim_row.json', 'no-indent')
net.write_json_to_file('sim_col', 'json/mult_view_sim_col.json', 'no-indent')

elapsed_time = time.time() - start_time

print('\n\nelapsed time')
print(elapsed_time)
