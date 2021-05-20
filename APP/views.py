from APP import app

from flask import render_template
from flask import request, redirect

import os

import pandas as pd

def AR(data):
    rating = data['Rating']
    star5 = 0
    star4 = 0
    star3 = 0
    star2 = 0
    star1 = 0
    for star in rating:
        if star==' 5 stars ':
            star5+=1
        if star==' 4 stars ':
            star4+=1
        if star==' 3 stars ':
            star3+=1
        if star==' 2 stars ':
            star2+=1
        if star==' 1 star ':
            star1+=1
        
    AR = (5*star5 + 4*star4 + 3*star3 + 2*star2 + 1*star1) / (star5 + star4 + star3 + star2 + star1)
    
    return AR

monalRV_df = pd.read_csv('Datasets\MonalData\Monal Review.csv')
monalContradictions = pd.read_csv('Datasets\MonalData\Monal_ReviewsOnlyContradictReviews_VaderPlusLexicon.csv')

jj_reviews = pd.read_csv('Datasets\JJ_Data\JJ_Reviews.csv')




@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template("index.html")

@app.route("/TheMonalResturant", methods=['GET', 'POST'])
def themonal():
    return render_template("monal.html")

@app.route("/junaidjamshed", methods=['GET', 'POST'])
def junaidjamshed():
    return render_template("junaid jamshed.html")

@app.route("/alfatah", methods=['GET', 'POST'])
def alfatah():
    return render_template("alfatah.html")

@app.route("/jaybeeicecream", methods=['GET', 'POST'])
def jaybeeicecream():
    return render_template("jaybee icecream.html")

@app.route("/savorfoods", methods=['GET', 'POST'])
def savorfoods():
    return render_template("savor foods.html")

@app.route("/street1cafe", methods=['GET', 'POST'])
def street1cafe():
    return render_template("street1.html")

@app.route("/themonalreviews", methods=['GET', 'POST'])
def monal_reviews():

    return render_template("monal_reviews.html", mrv= [monalRV_df.to_html(classes='data') ])

@app.route("/themonalcontradictions", methods=['GET', 'POST'])
def monal_contradictions():

    return render_template( "monal_contradictions.html", mcontra = [monalContradictions.to_html(classes='data')] )

@app.route("/themonalFairReviews", methods=['GET', 'POST'])
def monal_fair():
    mfair = pd.read_csv('Datasets\MonalData\Monal_Reviews_Fair_Reviews.csv')

    rating = AR(mfair)
    
    return render_template( "monalFairReviews.html", data = [mfair.to_html(classes='data')], ar = "{:.2f}".format(rating) )

@app.route("/junaidjamshedreviews", methods=['GET', 'POST'])
def jj():

    return render_template( "jj_reviews.html", jj = [jj_reviews.to_html(classes='data')] )

@app.route("/junaidjamshedcontradictions", methods=['GET', 'POST'])
def jj_contradictions():
    jj_contradictions = pd.read_csv('Datasets\JJ_Data\JJ_ReviewsOnlyContradictReviews_VaderPlusLexicon.csv')

    return render_template("jj_contradictions.html", jjcontra=[jj_contradictions.to_html(classes='data')])

@app.route("/jjFairReviews", methods=['GET', 'POST'])
def jj_fair():
    jfair = pd.read_csv('Datasets\JJ_Data\JJ_Reviews_Fair_Reviews.csv')
    rating = AR(jfair)
    return render_template( "jjFairReviews.html", data = [jfair.to_html(classes='data')], ar = "{:.2f}".format(rating) )

@app.route("/savorfoodreviews", methods=['GET', 'POST'])
def savorfoodreviews():
    savorfoodrev = pd.read_csv("Datasets\Savour_Foods_Data\Savour_Foods_Reviews.csv")

    return render_template("savorfoodrev.html", data=[savorfoodrev.to_html(classes='data')])

@app.route("/savorfoodcontradictions", methods=['GET', 'POST'])
def savorfoodcontr():
    savorfoodctr = pd.read_csv("Datasets\Savour_Foods_Data\Savour_Foods_ReviewsOnlyContradictReviews_VaderPlusLexicon.csv")

    return render_template("savorfoodctr.html", data=[savorfoodctr.to_html(classes='data')])


@app.route("/SavorFoodsFairReviews", methods=['GET', 'POST'])
def savor_fair():
    savorfair = pd.read_csv('Datasets\Savour_Foods_Data\Savour_Foods_Reviews_Fair_Reviews.csv')
    rating = AR(savorfair)
    return render_template( "savorfoodsfairreviews.html", data = [savorfair.to_html(classes='data')], ar = "{:.2f}".format(rating) )


@app.route("/alfatahreviews", methods=['GET', 'POST'])
def alfatahreviews():
    alfarev = pd.read_csv("Datasets\AL-Fatah_Data\AL-Fatah_Reviews.csv")

    return render_template("alfarev.html", data=[alfarev.to_html(classes='data')])


@app.route("/alfatahcontradictions", methods=['GET', 'POST'])
def alfatahcont():
    alfactr = pd.read_csv("Datasets\AL-Fatah_Data\AL_Fatah_ReviewsOnlyContradictReviews_VaderPlusLexicon.csv")

    return render_template("alfactr.html", data=[alfactr.to_html(classes='data')])

@app.route("/alfatahFairReviews", methods=['GET', 'POST'])
def alfatah_fair():
    alfafair = pd.read_csv('Datasets\AL-Fatah_Data\AL_Fatah_Reviews_Fair_Reviews.csv')
    rating = AR(alfafair)
    return render_template( "alfafairreviews.html", data = [alfafair.to_html(classes='data')], ar = "{:.2f}".format(rating) )


@app.route("/jaybeeicecreamreviews", methods=['GET', 'POST'])
def jbrev():
    jbrev = pd.read_csv("Datasets\Jay_Bee_Icecream_Data\Jay_Bee_Icecream_Reviews.csv")

    return render_template("jbrev.html", data=[jbrev.to_html(classes='data')])


@app.route("/jaybeeicecreamcontradictions", methods=['GET', 'POST'])
def jbctr():
    jbctr = pd.read_csv("Datasets\Jay_Bee_Icecream_Data\Jay_Bee_Icecream_ReviewsOnlyContradictReviews_VaderPlusLexicon.csv")

    return render_template("jbctr.html", data=[jbctr.to_html(classes='data')])


@app.route("/jaybeeicecreamFairReviews", methods=['GET', 'POST'])
def jb_fair():
    jbfair = pd.read_csv('Datasets\Jay_Bee_Icecream_Data\Jay_Bee_Icecream_Reviews_Fair_Reviews.csv')
    rating = AR(jbfair)
    return render_template( "jbfairreviews.html", data = [jbfair.to_html(classes='data')], ar = "{:.2f}".format(rating) )


@app.route("/street1cafereviews", methods=['GET', 'POST'])
def st1r():
    st1r = pd.read_csv("Datasets\Street_1_Cafe_Data\Street_1_Cafe_Reviews.csv")

    return render_template("st1reviews.html", data=[st1r.to_html(classes='data')])


@app.route("/street1cafecontradictions", methods=['GET', 'POST'])
def st1cont():
    st1c = pd.read_csv("Datasets\Street_1_Cafe_Data\Street1_Cafe_ReviewsOnlyContradictReviews_VaderPlusLexicon.csv")

    return render_template("st1cont.html", data=[st1c.to_html(classes='data')])

@app.route("/street1cafeFairReviews", methods=['GET', 'POST'])
def st_fair():
    stfair = pd.read_csv('Datasets\Street_1_Cafe_Data\Street1_Cafe_Reviews_Fair_Reviews.csv')
    rating = AR(stfair)
    return render_template( "stfairreviews.html", data = [stfair.to_html(classes='data')], ar = "{:.2f}".format(rating) )


@app.route("/SearchButton", methods=['GET', 'POST'])
def searchButton():
    try:
        name = request.form['search']
        return render_template(name + ".html")
    except (TypeError ,NameError):
            flash("Data Not Found")