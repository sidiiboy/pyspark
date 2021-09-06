Q) input  [("a",1),("a",2),("b",1),("a",3),("b",2)]
	output ('a', (1, 2, 3)) ('b', (1, 2))

data=[("a",1),("a",2),("b",1),("a",3),("b",2)]
rdd=sc.parallelize(data)

r=rdd.groupByKey().collect()
for k,v in r:
    print(k,tuple(v))
