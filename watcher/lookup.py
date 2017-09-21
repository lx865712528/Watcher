from django.conf import settings


class CONLL():
    def __init__(self):
        self.title = "This is title"
        self.DCT = "YYYY-MM-DD"
        self.ID = "Unique ID"
        self.body = []


def look_up(question, subtask_id):
    if type(question) == tuple or type(question) == list:
        question = "".join(question)
    question = question.strip()
    subtask_dict = settings.SUBTASK[subtask_id]
    file_path = subtask_dict[question]
    print("Found in %s" % file_path)
    return parse(file_path)
    # return parse("/Users/liuxiao/MyResearches/SemEval2018Task5/trial_data/input/s1/CONLL/1-81781.conll")


def parse_document(document):
    ans = CONLL()
    ans.ID = document[0]
    ans.DCT = document[1][1]
    document = document[2:]
    sentence_segs = []
    body = []
    pos = 0
    while pos < len(document) and document[pos][2] == "TITLE":
        sentence_segs.append(document[pos][1])
        pos += 1
    ans.title = " ".join(sentence_segs)
    prev_sentence_id = "0"
    sentence_segs.clear()
    while pos < len(document):
        cnt_sentence_id = document[pos][0].split(".")[1]
        if cnt_sentence_id != prev_sentence_id and len(sentence_segs) > 0:
            body.append(" ".join(sentence_segs))
            sentence_segs.clear()
        if cnt_sentence_id == "XX":
            break
        sentence_segs.append(document[pos][1])
        prev_sentence_id = cnt_sentence_id
        pos += 1
    for line in body:
        if "NEWLINE" in line:
            segs = line.split("NEWLINE")
            for seg in segs:
                if len(seg) > 0:
                    ans.body.append(seg.strip())
    return ans


def parse(file_path):
    answer = []
    with open(file_path, "r", encoding="utf-8") as f:
        document = []
        for line in f:
            line = line.strip()
            if line.startswith("#begin document"):
                document.clear()
                document.append(line.replace("#begin document", "").strip()[1:-2])
            elif line == "#end document":
                document.append(["XX.XX.XX"])
                answer.append(parse_document(document))
            else:
                document.append(line.split("\t"))
    return answer
