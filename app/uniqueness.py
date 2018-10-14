def check_uniqueness():
    class Unique(object): 
    def __init__(self, column, session, message="Already exists."): 
     self.column = column 
     self.session = session 
     self.message = message 

    def __call__(self, form, field): 
     if field.data == field.object_data: 
      return # Field value equals to existing value. That's ok. 
     model = self.column.class_ 
     query = model.query.filter(self.column == field.data).exists() 
     if self.session.query(query).scalar(): 
      raise ValidationError(self.message) 

class Register(Form): 
    email = EmailField('Email', [Unique(User.email, db.session)]) 

class Register(Form): 
    email = EmailField('Email', [Unique(User.email)]) 

