from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

class BillForm(Form):
    amount = StringField("Bill amount: ")
    period = StringField("Bill period: ")

    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the house: ")
    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the house: ")

    button = SubmitField("Calculate")

class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform=bill_form)


class ResultsPage(MethodView):
    pass




app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form'))

app.run(debug=True)

