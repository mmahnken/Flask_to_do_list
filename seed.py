"""
seed.py
"""

import model

db = model.connect_db()
user_id = model.new_user(db, "chriszf@gmail.com", "securepassword", "Christian", "Fernandez")

new = model.new_user(db, "albymeono@gmail.com", "password", "Alby", "Meono")
print new 

task = model.new_task(db, "Complete this task list", user_id)
print task

task = model.new_task(db, "poop", user_id)
print task

get = get_user(db, "albymeono@gmail.com")
print get

complete = complete_task(db, 'poop')

log_in = authenticate(db, "albymeono@gmail.com", "password")
print log_in
 