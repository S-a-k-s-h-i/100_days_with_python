def Remove_empty(tup):
    tuples=[t for t in tup if t]
    print(tuples)

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
Remove_empty(tuples)