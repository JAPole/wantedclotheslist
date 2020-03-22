from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Tops, Bottoms, 
from application.forms import PostForm, UpdateAccountForm


@app.route('/')
@app.route('/home')
def home():
    outfitData = outfit.query.all()
    return render_template('home.html', title='Home', outfit=outfitData)

@app.route('/about')
def about():
    return render_template('about.html' , title='About')



@app.route('/outfit', methods=['GET', 'POST'])

def outfit():
    form = OutfitForm()
        outfitData = Outfits(
        style_oftop = form.style_oftop.data,
        colour_oftop = form.colour_oftop.data,
        style_ofbottom = form.style_ofbottom.data,
        colour_ofbottom = form.colour_ofbottom.data
                       
        )

        db.session.add(outfitData)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        print(form.errors)


    return render_template('outfit.html', title='Outfit', form=form)




