from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pickle


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# load data
model = pickle.load(open("cf_recommender.model", 'rb'))
data = pickle.load(open("cf_recommender.df", 'rb'))


# search form
class SearchForm(FlaskForm):
    repository = StringField("Name of repository:", validators=[DataRequired()])
    submit = SubmitField("Get Similar Repositories")


def get_similar_repos(model, data, repo_name):

    # get index
    repo_idx = data.repo_id[data.repo == repo_name]

    # repo does not exist
    if len(repo_idx) == 0:
        return(None)

    # get similar items
    repo_idx = repo_idx.iloc[0]
    similar = model.similar_items(repo_idx, N=11)

    recs = []

    for item in similar:
        idx, score = item
        name = data.repo[data.repo_id == idx].iloc[0]
        if name != repo_name:
            recs.append({'name': name, 'score': score})

    return recs


@app.route("/")
def search():

    form = SearchForm()
    return render_template('search.html', form=form)


@app.route('/', methods=['POST'])
def result():

    repo = request.form['repository']
    recs = get_similar_repos(model, data, repo)
    return render_template('result.html', query=repo, recs=recs)


if __name__ == '__main__':
    app.run(debug=True)
