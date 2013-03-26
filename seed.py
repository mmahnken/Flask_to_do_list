"""
seed.py
"""

import model

db = model.connect_db()
user_id = model.new_user(db, "chriszf@gmail.com", "securepassword", "Christian", "Fernandez")

new = model.new_user(db, "albymeono@gmail.com", "password", "Alby", "Meono")
print new 

task = model.new_task(db, "Win at life", "Alby", "Meono")
print task

get = model.get_user(db, "albymeono@gmail.com")
print get

complete = model.complete_task(db, 'poop')

log_in = model.authenticate(db, "albymeono@gmail.com", "password")
print log_in

completed_lawblog = model.complete_task(db, 2)

done = model.get_tasks(db,10)
print "You have completed %s" % done

one_tASK = model.get_task(db, 13)
print one_tASK
 