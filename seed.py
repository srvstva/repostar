from repostar import db
from repostar.models import User

user1 = User(username='codeflops', email='codeflops@gmail.com')
user1.set_password('codeflops')

db.session.add(user1)


admin = User(username='admin', email='admin@codeflops.com')
admin.set_password('admin')

db.session.add(admin)

db.session.commit()
