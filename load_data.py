from datasets import load_dataset


def load_brighter(language= "eng"):

    dataset = load_dataset("brighter-dataset/BRIGHTER-emotion-categories", language)

    train_dataset = dataset["train"]

    texts = train_dataset["text"]
    labels = train_dataset["emotions"]

    return texts, labels

def load_all():
    languages = ["eng","deu", "rus", "chn"]

    data = {}

    for lang in languages:
        texts, labels = load_brighter(lang)
        data[lang] = {"texts": texts, "labels": labels}

    return data

def main():
    data = load_all()

    print(data.keys())
    print(data["eng"]["texts"][:5])
    print(data["eng"]["labels"][:5])
    print(data["deu"]["texts"][:5])
    print(data["deu"]["labels"][:5])
    print(data["rus"]["texts"][:5])
    print(data["rus"]["labels"][:5])
    print(data["chn"]["texts"][:5])
    print(data["chn"]["labels"][:5])

if __name__ == "__main__":
    main()



