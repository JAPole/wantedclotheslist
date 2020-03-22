from application import db


Oufit = db.Table(‘outfits’, 
            db.Column(‘top_id’, db.Integer, db.ForeignKey('Top.top.id'), nullable=False)
            db.Column(‘bottom_id’, db.Integer, db.ForeignKey('Bottom.bottom.id'), nullable=False))



class Tops(db.Model):
   
    __tablename__ = 'Top_Identity'
   
    top_id = db.Column(db.Integer, primary_key=True)
    style_oftop = db.Column(db.String(40), nullable=False)
    colour_oftop = db.Column(db.String(40), nullable=False)
    
    outfits = db.realtionship(‘Bottoms’,  secondary=Outfit, backref=db.backref(‘stylist’, lazy='dynamic'))


    #__repr__ prints to the screen
    
    def __repr__(self):

        return '<Top: {}>'.format(self.name)
                  ])
    

class Bottoms(db.Model):
    
    __tablename__ = 'Bottom_Identity'

    bottom_id = db.Column(db.Integer, primary_key=True)
    style_ofbottom = db.Column(db.String(40), nullable=False)
    colour_ofbottom = db.Column(db.String(40), nullable=False)
    


     #__repr__ prints to the screen
    
    def __repr__(self):

        return '<Bottom: {}>'.format(self.name)
                  ])


  
    
    
    def __repr__(self):
        return ''.join(['outfitID: ', str(self.id), '\r\n',
       
        )



