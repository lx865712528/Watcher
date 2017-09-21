import json

from django.conf import settings


def load_subtask(task_id):
    file_path = settings.SUBTASK_DATA_BASE + "s%d" % int(task_id) + "/questions.json"
    q2p = {}
    with open(file_path, "r", encoding="utf-8") as f:
        all_qs = json.load(f)
        for key, value in all_qs.items():
            question = value["verbose_question"].strip()
            file_path = key.strip()
            q2p[question] = settings.SUBTASK_DATA_BASE + "s%d/CONLL/" % int(task_id) + file_path + ".conll"
    print("Load subtask %d done!" % task_id)
    return q2p
