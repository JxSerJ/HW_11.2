import json
from classes.Candidate import Candidate


def load_candidates(path: str) -> dict:
    """
    JSON Data loader

    :param path: data-file path
    :return: data
    """
    with open(path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
        data_dict = {}
        for i in data:
            data_dict[i["id"]] = i
        return data_dict


def build_candidate_instances_and_skill_list(data: dict) -> tuple[dict, list]:
    """
    Object instance initializer (class Candidate)

    :param data: dictionary of candidates
    :return: list of objects and list of skills
    """
    candidate_dict = {}
    skill_list = []

    for candidate_id, candidate_data in data.items():
        candidate = Candidate(candidate_id=candidate_id, name=candidate_data["name"], avatar=candidate_data["picture"],
                              position=candidate_data["position"], gender=candidate_data["gender"],
                              age=candidate_data["age"], skills=candidate_data["skills"])
        skill_list.extend([skill.lower() for skill in candidate.skills.split(", ")])
        candidate_dict[candidate_id] = candidate

    skill_list = list(set(skill_list))

    return candidate_dict, skill_list


def get_candidate(candidate_dict: dict, candidate_id: int) -> Candidate:
    """
    Get Candidate instance by candidate id.

    :param candidate_dict: all candidates instances in dict
    :param candidate_id: candidate id
    :return: Candidate instance
    """
    for i in candidate_dict:
        if candidate_id == i:
            return candidate_dict[i]


def get_candidates_by_name(candidate_dict: dict, search_data_from_input: str) -> list[Candidate] or str:
    """
    Get list of Candidate instances by name. User input string is used for search.

    :param candidate_dict: all candidates instances in dict
    :param search_data_from_input: string which was acquired by flask app.
    :return: list of Candidate instances which meets the search data in .name field
    """

    found_candidate_list = []

    if search_data_from_input == "":
        return "no_input"

    for candidate in candidate_dict.values():
        if search_data_from_input in candidate.name.lower():
            found_candidate_list.append(candidate)
        else:
            continue
    if len(found_candidate_list) == 0:
        return "no_data"
    else:
        return found_candidate_list


def get_candidates_by_skill(candidate_dict: dict, search_data_from_input: str) -> set[Candidate] or str:
    """
    Get list of Candidate instances by skill. User input string is used for search.

    :param candidate_dict: all candidates instances in dict
    :param search_data_from_input: string which was acquired by flask app.
    :return: list of Candidate instances which meets the search data in .skills field
    """

    found_candidate_list = []

    if search_data_from_input == "":
        return "no_input"

    for candidate in candidate_dict.values():
        candidate_skills = candidate.skills.lower().split(", ")
        if search_data_from_input in candidate_skills:
            found_candidate_list.append(candidate)
        else:
            continue
    if len(found_candidate_list) == 0:
        return "no_data"
    else:
        return set(found_candidate_list)
