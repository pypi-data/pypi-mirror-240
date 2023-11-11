import dendropy as dp

num_taxa = 1000

t = dp.simulate.treesim.birth_death_tree(birth_rate=1.0,
                                         death_rate=0.5,
                                         num_extant_tips=num_taxa)

print(t)