from flask import Flask, render_template, request
from config import DATA_FILE_PATH
from utils import load_candidates, build_candidate_instances_and_skill_list, get_candidate, get_candidates_by_name,\
    get_candidates_by_skill

application = Flask(__name__)

candidates = load_candidates(DATA_FILE_PATH)
candidate_dict, skill_list = build_candidate_instances_and_skill_list(candidates)


@application.route("/elon", methods=["GET"])
def page_elon():
    return render_template('elon.html')


@application.route("/", methods=["GET"])
def page_index():
    return render_template('list.html', candidates=candidate_dict)


@application.route("/candidate/<int:candidate_id>", methods=["GET"])
def page_candidate(candidate_id):
    return render_template('candidate.html', candidate=get_candidate(candidate_dict, candidate_id))


@application.route("/search_by_name", methods=["GET", "POST"])
def page_search_by_name():
    if request.method == "POST":
        search_data = request.form.get("search_data_from_input").lower()
        return render_template('search_by_name.html', search_data=get_candidates_by_name(candidate_dict, search_data))
    return render_template('search_by_name.html')


@application.route("/search_by_skill", methods=["GET", "POST"])
def page_search_by_skill():
    if request.method == "POST":
        search_data = request.form.get("search_data_from_input").lower()
        return render_template('search_by_skill.html', search_data=get_candidates_by_skill(candidate_dict, search_data))
    return render_template('search_by_skill.html')


application.run(debug=True)
